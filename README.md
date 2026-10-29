# Clean Feeds API examples

Small, runnable Python scripts for the Clean Feeds data APIs. Each folder has one script, a sample input and a README.

> **Disclosure:** I built these APIs. Both have free plans, and every script here works on them.

| Example | What it does | API |
|---|---|---|
| [job-alerts](job-alerts/) | Daily job alerts: prints only the jobs posted since the last run, filtered by keyword, location, remote and minimum salary. Run it from cron. | Job Search API |
| [vin-recall-check](vin-recall-check/) | Checks a list of VINs for US and Canadian safety recalls, flags "do not drive" and "park outside" ones, and writes a CSV. | Vehicle Data API |

## Quick start

```bash
git clone https://github.com/CleanFeeds/clean-feeds-examples.git
cd clean-feeds-examples/vin-recall-check
pip install -r requirements.txt
export RAPIDAPI_KEY="your-key-here"   # free plan, see below
python recall_check.py vins.txt
```

## The APIs

**Job Search API.** 700,000+ open jobs read directly from company career sites (Greenhouse, Lever, Ashby, Workday,
SmartRecruiters and more), refreshed daily, with closed jobs removed. Search by keyword, location, remote, seniority
and salary, or list every open job at one company.
[RapidAPI](https://rapidapi.com/shubhack319/api/job-search-api-career-site-jobs) ·
[Zyla](https://zylalabs.com/api-marketplace/other/career+site+job+search+api/14418) ·
[API.market](https://api.market/store/clean-feeds/job-search)

**Vehicle Data API.** VIN decoding plus US (NHTSA) and Canadian (Transport Canada) recalls, owner complaints, NHTSA
crash ratings and EPA fuel economy. Batch up to 50 VINs per call; mistyped VINs get a suggested correction.
[RapidAPI](https://rapidapi.com/shubhack319/api/vehicle-data-api-vin-decoder-recalls-safety-ratings) ·
[Zyla](https://zylalabs.com/api-marketplace/automotive+%26+vehicle+data/vin+decoder+and+vehicle+recalls+api/14497) ·
[API.market](https://api.market/store/clean-feeds/vehicle-data)

The scripts use RapidAPI keys. On Zyla or API.market only the host and the key header change.

## Tutorials

- [Build a daily job alerts feed in Python](https://cleanfeeds.hashnode.dev/python-daily-job-alerts-api)
- [Check a list of cars for safety recalls in Python](https://cleanfeeds.hashnode.dev/python-vin-recall-check)
- [Get every open job from any company's career page](https://cleanfeeds.hashnode.dev/get-every-open-job-from-any-company-s-career-page-no-html-scraping)

## License

MIT. Issues and pull requests are welcome.
