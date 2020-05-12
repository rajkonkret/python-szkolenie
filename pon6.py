ns = []
sum = 0
size = int(input('Podaj ile liczb\n'))
for i in range(1,size+1):
    print(len(ns))
    element = int(input('Podaj liczbe\n'))
    ns.append(element)
    sum+=element
print('suma: ',sum)

size = int(input('Podaj ile liczb\n'))
ns2 = []
for i in range(1,size+1):
    element = int(input('Podaj liczbe\n'))
    ns2.append(element)
# w jaki sposób odczytywać elementy listy
for value in ns2:
    print(value)

for index,value in enumerate(ns2):
    print(index,value)
