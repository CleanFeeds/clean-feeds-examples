"""Daily job alerts: print the jobs posted since the last run that match your search.

    pip install requests
    export RAPIDAPI_KEY=...        # from the API's page on RapidAPI
    python job_alerts.py

Run it from cron (e.g. every morning) and only new jobs show up each time.
"""

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

HOST = "job-search-api-career-site-jobs.p.rapidapi.com"
URL = f"https://{HOST}/search"
HEADERS = {"X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""), "X-RapidAPI-Host": HOST}
STATE = Path("last_run.json")

SEARCH = {
    "keywords": "data engineer,analytics engineer",
    "locations": "United States",
    "remote": "true",
    "min_salary": 120000,
    "salary_currency": "USD",
    "limit": 50,
}


def new_jobs(since: str) -> list[dict]:
    params, jobs = {**SEARCH, "posted_after": since}, []
    while True:
        page = requests.get(URL, headers=HEADERS, params=params, timeout=90)
        page.raise_for_status()
        data = page.json()
        jobs += data["jobs"]
        if not data["meta"].get("nextCursor"):
            return jobs
        params["cursor"] = data["meta"]["nextCursor"]


def main() -> None:
    now = datetime.now(timezone.utc)
    first_run = (now - timedelta(days=7)).strftime("%Y-%m-%d")  # first run: the last week
    since = json.loads(STATE.read_text())["since"] if STATE.exists() else first_run
    jobs = new_jobs(since)
    for j in jobs:
        low, high = j.get("salaryMin"), j.get("salaryMax") or j.get("salaryMin")
        pay = f"{low:,.0f}-{high:,.0f} {j['salaryCurrency']}" if low else "salary n/a"
        print(f"{j['title']} @ {j['company']} ({j['location']}) | {pay}\n  {j['url']}")
    print(f"\n{len(jobs)} new jobs since {since}")
    STATE.write_text(json.dumps({"since": now.strftime("%Y-%m-%dT%H:%M:%SZ")}))


if __name__ == "__main__":
    main()
