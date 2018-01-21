import json
import pprint
import os
import sys
from pathlib import Path

import django
from django.utils.timezone import timedelta
from django.utils.dateparse import parse_datetime, parse_duration, parse_date

# Add project root and script root to $PYTHONPATH
project_root = Path(__file__).parent.parent.absolute()
sys.path.append(str(project_root))
# Load Django environment (settings, apps, db...)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrumtasks.settings")
django.setup()

from tasks.models import WorkingDay

with (project_root / 'wtv2.json').open() as f:
    data = json.load(f)

dailyentries = data['dailyentries']
for entry in dailyentries:
    print(entry)
    start = parse_datetime(entry['start'])
    total_time = parse_duration(entry['total_time'])
    date = parse_date(entry['date'])
    breaks = timedelta(minutes=entry['breaks'])
    WorkingDay.objects.create(date=date, entry=start, working_time=total_time,
                              breaks=breaks)
