import datetime
from dateutil.relativedelta import relativedelta
print(datetime.date.today())

class Book:
    def __init__(self, title, author, number_of_page, date):
        self.title = title
        self.author = author
        self.number_of_page = number_of_page
        self.date = date
    def __repr__(self):
        return self.title + ' ' + str(self.date)
    def get_days(self):
        td = (datetime.date.today() - self.date).days
        return td

def get_date(book):
    return book.date

books = []     
dt = datetime.date(2010,1,1)
dt2 = datetime.date(2010,1,28)
dt3 = datetime.date(2014,7,28)

book1 = Book('DScience', 'raj',55, dt)
book2 = Book('Python od podstaw', 'rajkonkret', 155, dt2)
book3 = Book('Python od podstaw TRZY', 'rajkonkret strum ', 789, dt3)

print (book1.get_days())
print(type(books))
books.append(book2)
books.append(book1)
books.append(book3)

print(books)
for i in books:
    print(i.title + 'is old ' + str(i.get_days()) + ' days.')

books.sort(key=get_date)
print('The oldest is: ' + str(books[-1]))


