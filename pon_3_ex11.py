def number_of_divisors(n):
    counter = 0
    for i in range(1,n+1):
        if n%i == 0:
            counter+=1
    return counter

print(number_of_divisors(9240))

