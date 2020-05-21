def is_it_quibc(number_1):
    return(round(pow(number,1.0/3.0),8) % 1 == 0)
try:
    number = int(input('Podaj liczbę: '))
    print('Jest sześcianem ?:', is_it_quibc(number))
except:
    print('Incorrect value!')