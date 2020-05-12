word = input('Podaj słowo\n')

# kajak
left = 0
right = len(word)-1

is_palindrome = True
while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break # konczy działąnie pętli bo na 100 % nie jest to palindrom
    left+=1
    right-=1
    print (left,right)

if is_palindrome:
    print('To jest palindrom')
else:
    print('Nie jest palindrom')

    
for i in range(0,len(word)//2+1):
    print (word[i])