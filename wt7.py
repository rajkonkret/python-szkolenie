import random

numbers = []
output = []
for i in range (1,50):
    numbers.append(i)

#numbers = range(1,50)
for j in range(0,6):
    element = int(random.randint(1,len(numbers)-1))
    temp  = numbers.pop(element)
    print(temp)
  
    
