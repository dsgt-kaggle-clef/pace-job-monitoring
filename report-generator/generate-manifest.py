#!/usr/bin/env python
from pathlib import Path
import json


def get_id(filename: Path, suffixes: list[str]) -> str:
    name = filename.name
    for suffix in suffixes:
        name = name.replace(suffix, "")
    return name.split("-")[1]


static = Path(__file__).parent / "static"
logs = static / "logs"
manifest = static / "manifest.json"

# get a list of all the job ids in the current job directory
log_suffixes = [".out", ".log"]
reports = [log for log in logs.glob("Report-*") if log.suffix in log_suffixes]
job_ids = sorted(
    [
        {
            "path": f"logs/{report.name}",
            "jobid": get_id(report, log_suffixes),
        }
        for report in reports
    ],
    key=lambda x: x["jobid"],
)
if not job_ids:
    raise ValueError("No job ids found in the logs directory.")
data = json.dumps(job_ids, indent=2)
manifest.write_text(data)
print(data)
