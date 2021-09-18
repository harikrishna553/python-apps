from datetime import datetime, timedelta

def diff_in_days(date1, date2):
    diff = date1 - date2
    return diff.days

date2 = datetime(1988, 6, 6)
date1 = datetime.today()

print (diff_in_days(date1, date2))