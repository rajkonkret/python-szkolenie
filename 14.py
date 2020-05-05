word = input('Podaj wyraz \n')
if word == 'Akademia':
    print('Podałeś poprawne hasło')
else:
    print('nie')

try:
    age = int(input('Podaj wiek\n'))
    print('Twój wiek to: ', age)
except:
    print('To nie jest wiek')