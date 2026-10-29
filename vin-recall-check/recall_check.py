"""Check a list of VINs for safety recalls (US + Canada) and flag the urgent ones.

Usage:  export RAPIDAPI_KEY=...   then   python recall_check.py vins.txt
vins.txt has one VIN per line. Writes recalls.csv next to it.
"""
import csv
import os
import sys

import requests

HOST = "vehicle-data-api-vin-decoder-recalls-safety-ratings.p.rapidapi.com"
BASE = f"https://{HOST}"
HEADERS = {"X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""), "X-RapidAPI-Host": HOST}


def call(path, **params):
    r = requests.get(BASE + path, params=params, headers=HEADERS, timeout=60)
    body = r.json()
    if r.status_code != 200:
        raise ValueError(body.get("error") or body.get("message") or f"HTTP {r.status_code}")
    return body["data"]


def recalls_for(vin):
    """Recalls for one VIN; if the VIN is mistyped, say what is wrong and suggest a fix."""
    try:
        return call("/recalls", vin=vin, country="us,ca")
    except ValueError as e:
        check = call(f"/vin/{vin}/validate")
        if check["valid"]:
            raise
        hint = f" Did you mean {check['suggestions'][0]}?" if check["suggestions"] else ""
        raise ValueError(" ".join(check["problems"]) + hint) from e


def flags(r):
    out = []
    if r["doNotDrive"]:
        out.append("DO NOT DRIVE")
    if r["parkOutside"]:
        out.append("PARK OUTSIDE")
    return ", ".join(out)


def main(path):
    vins = [line.strip().upper() for line in open(path) if line.strip()]
    rows = []
    for vin in vins:
        try:
            data = recalls_for(vin)
        except ValueError as e:
            print(f"{vin}  ERROR: {e}")
            continue
        v = data["vehicle"]
        print(f"{vin}  {v['year']} {v['make']} {v['model']}: {data['count']} recalls, {data['urgentCount']} urgent")
        for r in data["recalls"]:
            if r["urgent"]:
                print(f"    !! {flags(r)}  {r['campaignNumber']} ({r['country'].upper()})  {r['component']}")
            rows.append({"vin": vin, "year": v["year"], "make": v["make"], "model": v["model"],
                         "country": r["country"], "campaign": r["campaignNumber"], "date": r["reportDate"],
                         "component": r["component"], "urgent": r["urgent"], "flags": flags(r),
                         "remedy_status": r["remedyStatus"], "summary": (r["summary"] or "").strip()})
    out = os.path.join(os.path.dirname(os.path.abspath(path)), "recalls.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["vin", "year", "make", "model", "country", "campaign", "date",
                                               "component", "urgent", "flags", "remedy_status", "summary"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n{len(rows)} recalls for {len(vins)} VINs written to {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "vins.txt")
