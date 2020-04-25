import calendar
name = input('podaj imię\n'.lower())
if name[-1] == 'a':
  print('Imię żeńskie')
else:
  print("męskie")

calendar.setfirstweekday(calendar.MONDAY)
print(calendar.monthcalendar(2016,2))
weekday = calendar.weekday(2016,2,1)
print(calendar.day_name[weekday])
print(calendar.weekheader(5))
print(calendar.day_name[0])
print(calendar.prmonth(2020,4,5,0))
print(calendar.prmonth(2016,2,7))
#wyświetlenie ostatniej cyfry
print(2054 % 10)
number = int (input("Podaj liczbe\n"))
print(number%10)
dict = {
  "first":"pierwszy",
  "end":"koniec",
  "tea":"herbata",
  "dog":"pies"
}

print(dict)
word = input ("podaj wyraz\n")
print (dict[word])

for i in range(20,0,-1):
  print(i)
import random as r
for i in range(0,10):
  print("*",end='')

print("\n")
print ("*"*10)
users =['ad','fg','yu','gry']
print(r.choice(users))