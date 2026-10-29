# Daily job alerts

Prints only the jobs posted since the last run, straight from companies' own career sites, filtered by keyword,
location, remote and minimum salary. Run it every morning from cron.

```
$ python job_alerts.py
Senior Analytics Engineer @ Betterup (Austin, TX) | 158,000-220,000 USD
  https://jobs.ashbyhq.com/betterup/72ad3a02-6d5c-47b5-9eae-1a39040f0bf9
Analytics Engineer @ Lovable (Boston) | 141,500-192,000 USD
  https://jobs.ashbyhq.com/lovable/d92292d5-a9f5-4637-9d86-77e95bf66970
...
```

## Setup

1. Subscribe to the free plan of the
   [Job Search API on RapidAPI](https://rapidapi.com/shubhack319/api/job-search-api-career-site-jobs) and copy your
   `X-RapidAPI-Key`.
2. Install and run:

```bash
pip install -r requirements.txt
export RAPIDAPI_KEY="your-key-here"
python job_alerts.py
```

The first run shows the last 7 days of jobs. After that, `last_run.json` remembers when it ran, so each run prints only
new postings.

## Change the search

Edit `SEARCH` at the top of `job_alerts.py`:

```python
SEARCH = {
    "keywords": "data engineer,analytics engineer",  # comma = OR
    "locations": "United States",
    "remote": "true",
    "min_salary": 120000,
    "salary_currency": "USD",
    "limit": 50,
}
```

## Run it daily

```bash
crontab -e
# every day at 08:00
0 8 * * * cd /path/to/job-alerts && RAPIDAPI_KEY=your-key python job_alerts.py >> alerts.log 2>&1
```

Full walkthrough: [Build a daily job alerts feed in Python](https://cleanfeeds.hashnode.dev/python-daily-job-alerts-api).
