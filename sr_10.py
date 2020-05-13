n = int((input('Podaj liczbę elementów\n')))
list = []

for i in range(1,n+1):
    number = int(input('Podaj liczbę\n'))
    list.append(number)
print(list)
print(max(list))
print(sorted(list))

max = list[0]
for value in list:
    if value > max:
        max=value
print(max)
