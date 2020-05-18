
def multiply(x,y):
    return x*y
def pitagoras(a,b,c):
    if a<0 or b<0 or c<0 :
        return False
    array = [a,b,c]
    array.sort()

    #if array[0] *array[0]+array[1]*array[1]==array[2]*array[2] :
     #   return True
    #else: 
     #   return False

    return array[0]*array[0]  +array[1]*array[1] == array[2]*array[2]

first_number = int(input('Podaj liczbę pierwszą'))
seond_number = int(input('Podaj liczbe drugą'))

print(multiply(x=first_number,y=seond_number))
print(multiply(y=first_number,x=seond_number))

try:
    f_n = input('Podaj bok a\n')
    if int(f_n):
        f_n =int(f_n)
+except ValueError:
    if not f_n:
        print('Brak boku')
    else:
        print('not int')
s_n = int(input('Podaj bok b\n'))
th_n = int(input('Podaj bok c\n'))

print(pitagoras(f_n,s_n,th_n))

