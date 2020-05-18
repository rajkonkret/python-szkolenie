# Mamy duza liczbe argumentow funkcji
# latwo o bledy w kolejnosci
# ROZWIAZANIE 1
def hi(first_name,last_name):
    print(first_name,last_name)
    # ta funkcja nic nie zwraca, zwraca None
hi(last_name='Makaruk',first_name='Michal')
hi('Makaruk','Michal') # zle wpisane dane
# ROZWIAZANIE 2
# **- specjalne oznaczenie
def hello(**arguments): # będzie dictionary
    # arguments zamieniony jest na dictionary, dict
    print(type(arguments))
    print(arguments['name'])
    print(arguments['surname'])
hello(name='Michal',surname='Makaruk')
hello(**{'surname': 'Makaruk','name': 'Michal'})


def bye(args):
    print(args['name'])
    print(args['surname'])

bye({'name':'radek','surname':'janiak'})

def bye_bye(*args): #będzie lista
    for i in args:
        print(i)

bye_bye(1,2,3,10) # tak naprawdę zamienia na tupla

