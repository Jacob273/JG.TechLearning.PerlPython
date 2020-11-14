from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

g = open('.\plan_zajec.ics','rb')

gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    
    if component.name == 'VEVENT':
        print(component['summary'])
g.close()