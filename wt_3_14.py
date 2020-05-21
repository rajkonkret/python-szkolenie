from pon_3_ex11 import number_of_divisors
number = 0
max = 0
for i in range(100000,1,-1):
    result = number_of_divisors(i)
    if result > max:
        max = result
        number = i
        print(max," ",i)

print(max," ",number)