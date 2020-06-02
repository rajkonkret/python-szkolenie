is_prime = True
a = 790
for i in range(2,a):  
    if a%i==0:
        is_prime = False         
        break 
    
if is_prime:     
    print('TAK') 
else:     
    print('NIE')

score = 0
for i in range(1,a+1):
    if a%i==0:
        score+=1
if score==2:
    print("to jest liczba pierwsza")
else:
    print("nie")