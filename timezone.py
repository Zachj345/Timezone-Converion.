import pytz
from datetime import datetime
from difflib import get_close_matches


usercontinent = input(
    'What continent are you located on? (if you live in the United States type "US/us"): ').title()
print()
userarea = input(
    'Now please tell us the region in which you reside, if none just type enter: ').title().replace(' ', '_')
print()


class TimezoneCalculator:
    def __init__(self, continent, country):
        self.continent = continent
        self.country = country
        self.utc = pytz.utc

    def special_cases(self, name):
        res = get_close_matches(name, pytz.all_timezones, cutoff=0.8)[0]
        print(res)
        print()
        return res

    def convert(self):
        utc_time = self.utc.localize(datetime.utcnow())
        try:
            name_for_tz = self.continent + '/' + self.country
            name = TimezoneCalculator.special_cases(self, name_for_tz)
            user_tz = pytz.timezone(name)
            format = '%m-%d-%Y, %I:%M:%S %p %Z%z'
            res = utc_time.astimezone(user_tz)
            return res.strftime(format)
        except (pytz.exceptions.UnknownTimeZoneError, IndexError):
            return 'enter a vaild timezone please, or possibly check your spelling'


obj = TimezoneCalculator(usercontinent, userarea)
print(obj.convert())
