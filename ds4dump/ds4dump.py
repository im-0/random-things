#!/usr/bin/python3

import base64
import contextlib
import json.tool
import sys

import hid


_DS4_IDS = (
    (0x054c, 0x05c4),
    (0x054c, 0x09cc),
)
_BUF_SZ = 1024
_N_REPORTS = 8


def _open_dev(dev_path):
    dev = hid.device()
    dev.open_path(dev_path)
    return dev


def _dump(base_info):
    dev_path = base_info.pop('path')
    dev_info = dict(base=base_info)

    print(f'Opening device \"{dev_path.decode()}\"...', file=sys.stderr)
    with contextlib.closing(_open_dev(dev_path)) as dev:
        print(f'Done opening device \"{dev_path.decode()}\"', file=sys.stderr)

        print('Trying to read Bluetooth MAC address...', file=sys.stderr)
        mac = None

        try:
            data = bytes(dev.get_feature_report(0x81, _BUF_SZ))
            dev_info['report_0x81'] = base64.b64encode(data).decode()

            if len(data) == 7:
                mac = list(reversed(data[1:7]))
        except IOError:
            dev_info['report_0x81'] = None

        try:
            data = bytes(dev.get_feature_report(0x12, _BUF_SZ))
            dev_info['report_0x12'] = base64.b64encode(data).decode()

            if mac is None and len(data) == 16:
                mac = list(reversed(data[1:7]))
        except IOError:
            dev_info['report_0x12'] = None

        if mac is None:
            dev_info['mac'] = None
            print('No Bluetooth MAC address', file=sys.stderr)
        else:
            dev_info['mac'] = ':'.join(f'{b:02x}' for b in mac)
            print(f'Bluetooth MAC address: {dev_info["mac"]}', file=sys.stderr)

        print(f'Reading {_N_REPORTS} reports...', file=sys.stderr)
        dev_info['reports'] = []
        for _ in range(_N_REPORTS):
            report = bytes(dev.read(_BUF_SZ))
            dev_info['reports'].append(base64.b64encode(report).decode())
        print(f'Done reading {_N_REPORTS} reports', file=sys.stderr)

    return dev_info


def _main():
    print('Enumerating HID devices...', file=sys.stderr)
    devices = hid.enumerate()
    devices = [dev for dev in devices if (dev['vendor_id'], dev['product_id']) in _DS4_IDS]
    print(f'Done enumerating HID devices, got {len(devices)}', file=sys.stderr)
    devices = [_dump(dev) for dev in devices]

    json.dump(devices, sys.stdout, indent=4)
    sys.stdout.write('\n')
    sys.stdout.flush()


_main()
