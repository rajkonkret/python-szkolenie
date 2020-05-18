def is_even(number):
    return number%2==0

number = int(input('Podaj liczbe'))
print(is_even(number))

mask = (1 << 2) - 1
little = number & mask
print(mask)
