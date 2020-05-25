import datetime as d
class Book:
    def __init__(self, title, author, page, date):
        self.title = title
        self.author = author
        self.page = page
        self.date = date
    def get_days(self):
        return (d.date.today() - self.date).days
    def __repr__(self):
        return self.title + ' ' + str(self.date)

example_date = d.date(2020,2,2)
print(example_date, d.date.today())
dt = d.date(2010,1,1)
dt2 = d.date(2010,1,28)
dt3 = d.date(2014,7,28)
book1 = Book('DScience', 'raj',55, dt)
book2 = Book('Python od podstaw', 'rajkonkret', 155, dt2)
book3 = Book('Python od podstaw TRZY', 'rajkonkret strum ', 789, dt3)
books = []
books.append(book2)
books.append(book1)
books.append(book3)