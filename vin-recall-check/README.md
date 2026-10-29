# VIN recall check

Checks a list of VINs for US and Canadian safety recalls, flags the urgent ones ("do not drive", "park outside") and
writes every recall to `recalls.csv`. Mistyped VINs get a suggested correction.

```
$ python recall_check.py vins.txt
1FTYR10U66PA41234  2006 FORD Ranger: 19 recalls, 4 urgent
    !! DO NOT DRIVE  18V022000 (US)  AIR BAGS:FRONTAL:PASSENGER SIDE:INFLATOR MODULE
    ...
KNDPB3ACXG7812345  2016 KIA Sportage: 6 recalls, 1 urgent
    !! PARK OUTSIDE  22V051000 (US)  SERVICE BRAKES, HYDRAULIC:ANTILOCK/TRACTION CONTROL/ELECTRONIC LIMITED SLIP:CONTROL UNIT/MODULE
1HGCM82633A004352  2003 HONDA Accord: 24 recalls, 0 urgent
...
```

## Setup

1. Subscribe to the free BASIC plan of the
   [Vehicle Data API on RapidAPI](https://rapidapi.com/shubhack319/api/vehicle-data-api-vin-decoder-recalls-safety-ratings)
   (200 requests a month) and copy your `X-RapidAPI-Key`.
2. Install and run:

```bash
pip install -r requirements.txt
export RAPIDAPI_KEY="your-key-here"
python recall_check.py vins.txt
```

`vins.txt` has one VIN per line; the sample has four, including one with a typo (letter O instead of zero) to show
the correction. To check your own vehicles, paste a spreadsheet column into the file. Blank lines and lowercase are
fine.

Each VIN costs one request (two if it is mistyped).

Recalls are listed per make, model and year. Always confirm with the manufacturer or a dealer whether a specific
vehicle has already been repaired.

Full walkthrough:
[Check a list of cars for safety recalls in Python](https://cleanfeeds.hashnode.dev/python-vin-recall-check).
