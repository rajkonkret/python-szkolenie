#
#dzielniki liczby od 1 do n
#

for i in range(5,101):
    number_of_divisors = 0
    for j in range(1,i+1):
        if i%j == 0:
            number_of_divisors+=1
    if number_of_divisors >= 4:
        print(str(i)+' ma conajmniej 4 dzielniki '+str(number_of_divisors))