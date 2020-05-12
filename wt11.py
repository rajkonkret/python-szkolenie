numbers = []
lenght = int(input("Podaj długos tablicy\n"))
for u in range(0,lenght):
    element = int(input('Podaj liczbę\n'))
    numbers.append(element)

numbers.sort()
print(numbers[-1])
print(numbers)
