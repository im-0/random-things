# ds4dump

## Samples

Chinese clone #1:

```json
{
    "base": {
        "vendor_id": 1356,
        "product_id": 1476,
        "serial_number": "",
        "release_number": 256,
        "manufacturer_string": "Sony Computer Entertainment",
        "product_string": "Wireless Controller",
        "usage_page": 0,
        "usage": 0,
        "interface_number": 0
    },
    "report_0x81": null,
    "report_0x12": "EuDijfJBjAglABNx2n0aAA==",
    "mac": "8c:41:f2:8d:e2:e0",
    "reports": [
        "AYCAgIAIAMwAAHMTAOn/+f/t/1QA8h5PBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIANQAAF8WAOr/+f/v/0QAhh+FBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIANwAAEsZAO7/+f/z/ygAjyDCBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAOQAADccAPL/+P/3/x8A2iDRBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAOwAACMfAPL/+P/3/xkApyCfBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAPQAAA8iAO//+P/1/yIAvSCbBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAPwAAPskAO//+P/y/zcAbiCUBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAQAAOcnAO3/+P/r/14ARB9sBQAAAAAAGwAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA=="
    ]
}
```

Chinese clone #2 (causes kernel crash in 5.10.12):

```json
{
    "base": {
        "vendor_id": 1356,
        "product_id": 1476,
        "serial_number": "",
        "release_number": 256,
        "manufacturer_string": "Sony Computer Entertainment",
        "product_string": "Wireless controller",
        "usage_page": 0,
        "usage": 0,
        "interface_number": 0
    },
    "report_0x81": null,
    "report_0x12": null,
    "mac": null,
    "reports": [
        "AYCAgIAIAAAAAPQEAP3/BwDv/zP4Ex7qBQAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAEIMAPr/BwDw/zf4KB7uBQAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAJATAPf/BgDv/0j4Jh7sBQAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAN4aAPL/BwDs/1f4GR7qBQAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAACwiAO3/BwDp/1b4Eh74BQAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAHopAO7/CADn/1L4Hx4UBgAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAMgwAPX/BwDq/zH4AR4aBgAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA==",
        "AYCAgIAIAAAAAGQ/AO//CADm/1T4Ah4MBgAAAAAAGgAAAACAAAAAgAAAAACAAAAAgAAAAACAAAAAgAAAAACAAA=="
    ]
}
```

## Diff

```
00000000: 01 80 80 80 80 08 00 cc 00 00 73 13 00 e9 ff f9  ..........s.....  #1
00000000: 01 80 80 80 80 08 00 00 00 00 f4 04 00 fd ff 07  ................  #2
          ^^ report type
                                        ^^ ^^ timestamp
                                                 ^^ ^^ gyroscope X 0
                                                       ^^ gyroscope X 1

00000010: ff ed ff 54 00 f2 1e 4f 05 00 00 00 00 00 1b 00  ...T...O........  #1
00000010: 00 ef ff 33 f8 13 1e ea 05 00 00 00 00 00 1a 00  ...3............  #2
          ^^ gyroscope X 1
             ^^ ^^ gyroscope X 2
                   ^^ ^^ gyroscope X 3
                         ^^ ^^ gyroscope X 4
                               ^^ ^^ gyroscope X 5
                                                    ^^ battery state

00000020: 00 00 00 80 00 00 00 80 00 00 00 00 80 00 00 00  ................  #1
00000020: 00 00 00 80 00 00 00 80 00 00 00 00 80 00 00 00  ................  #2
             ^^ number of touch events
                ^^ touch event #0 timestamp
                   ^^ ^^ ^^ ^^ touch event #0 data
                               ^^ touch event #1 timestamp
                                  ^^ ^^ ^^ ^^ touch event #1 data
                                              ^^ touch event #2 timestamp
                                                 ^^ ^^ ^^ touch event #2 data

00000030: 80 00 00 00 00 80 00 00 00 80 00 00 00 00 80 00  ................  #1
00000030: 80 00 00 00 00 80 00 00 00 80 00 00 00 00 80 00  ................  #2
          ^^ touch event #2 data
             ^^ touch event #3 timestamp
                ^^ ^^ ^^ ^^ touch event #3 data
```
