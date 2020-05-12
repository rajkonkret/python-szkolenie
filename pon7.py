import random
numbers = []
numbersset = set()
while len(numbers)!=6:
    number = random.randint(1,50)
    if not number in numbers:
        numbers.append(number)
numbers.sort()
print(numbers)

while len(numbersset)!=6:
    num = random.randint(1,49)
    numbersset.add(num)
print(numbersset)
print(sorted(numbersset))
