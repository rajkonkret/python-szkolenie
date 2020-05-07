import matplotlib.pyplot as p
x = [1,4,7]
y = [3,2,10]
print('Test')
a = int( input('Podaj liczbę 1\n'))
b = int( input('Podaj liczbę 2\n'))
c = int( input('Podaj liczbę 3\n'))

if a>b:
    max = a # a jest kandydatem na maxa
    print(a)
else:
    max = b # b jest kandydatem na maxa
    print(b)
if c>max:
    max = c
print('max = {}'.format(max))
word = input('Podaj wyraz czy jest palindromem\n')
reversed_string = word[::-1]
if word = reversed_string:
    print('Ten wyraz jest palindromem')
else:
    print('Ten wyraz nie jest palindromem')
print(reversed_string)

#p.plot(x,y)
#p.show()

