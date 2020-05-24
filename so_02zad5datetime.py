import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
print (date.today())
class Query:
    def __init__(self, username, date):
        self.username = username
        self.date = date
    def __repr__(self):
        return self.username + ' ' + self.date
    def is_old(self):
        date_after_two_week = self.date + relativedelta(days=14)
        return (date_after_two_week < datetime.date.today())

dt = datetime.date(2020,2,20)
q1 = Query('radek', dt)
print(q1.is_old())
