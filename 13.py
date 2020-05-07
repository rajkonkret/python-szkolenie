#zgadywanie liczby
# 1 liczba jest stała
# liczba będzie losowana
# dajemy podpowiedzi
import random
number = int( input('Podaj liczbę\n'))
secret_number = random.randrange(1,10)

while number != secret_number:
    if number>secret_number:
        number = int( input('Błędna liczba. Podaj jeszcze raz liczbę. jest za duża\n'))
    else:
        number = int( input('Błędna liczba. Podaj jeszcze raz liczbę. jest za mała\n'))


print("Udało Ci się")