def palindrome(word):
    left = 0
    right = len(word)-1
    is_palindrome = True
    while left<right:
        if word[left]!=word[right]:
            is_palindrome = False
            break    
        left+=1
        right-=1
    return is_palindrome

word = input('Podaj wyraz:\n')

if palindrome(word):
    print('palindrom')
else:
    print('nie jest palindromem')