from pon_3_ex11 import number_of_divisors
#import pon_3_ex11 as s
#print(s.number_of_divisors(5))
print(number_of_divisors(5))


#def is_prime(number):
#    return s.number_of_divisors(number) == 2

def is_prime(number):
    return number_of_divisors(number) == 2

print(is_prime(7))