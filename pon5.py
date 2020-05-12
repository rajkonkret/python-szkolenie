numbers = [1,3,4,5,6]
ns = []
print(len(numbers))
print(numbers)
for i in numbers:
    print(str(i),end=' ')
print(numbers[::-1])

size = int(input('Podaj ile liczb\n'))
for i in range(1,size+1):
    print(len(ns))
    element = int(input('Podaj liczbe\n'))
    ns.append(element)
ns.reverse()
print(ns)

ns = ns[::-1]
print(ns)

ns.sort()
print(ns)