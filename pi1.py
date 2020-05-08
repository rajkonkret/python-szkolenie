n = int(input('podaj liczbę\n'))
sum = 0
sum2 = 0
for i in range(1,n+1):
    print(i)
    sum += i
    sum2 = sum2 + i 
print(sum)
print(sum2)

print((n+1)*n/2)