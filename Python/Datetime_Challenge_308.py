

import datetime
from dateutil import tz

# Set up time zones
portland_tz = tz.gettz('America/Los_Angeles')
nyc_tz = tz.gettz('America/New_York')
london_tz = tz.gettz('Europe/London')

# Get the current time in each time zone
portland_time = datetime.datetime.now(portland_tz)
nyc_time = datetime.datetime.now(nyc_tz)
london_time = datetime.datetime.now(london_tz)

# Set up branch hours
branch_hours = {
    'Portland': ('09:00', '17:00', portland_tz),
    'New York City': ('09:00', '17:00', nyc_tz),
    'London': ('09:00', '17:00', london_tz)
}

# Check if each branch is open or closed
for branch, hours in branch_hours.items():
    open_time = datetime.datetime.strptime(hours[0], '%H:%M').time()
    close_time = datetime.datetime.strptime(hours[1], '%H:%M').time()
    tz = hours[2]
    branch_time = datetime.datetime.now(tz).time()

    if branch_time >= open_time and branch_time <= close_time:
        status = 'open'
    else:
        status = 'closed'

    print(f'{branch} is {status}.')
