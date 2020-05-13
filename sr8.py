polish_words = ['mama','tata','witam']
english_words = ['mother', 'father','hello']
print(polish_words[0])
print(english_words[0])
index = polish_words.index("mama")
print(english_words[index])
polish_word = input('Podaj wyraz\n')
try:
    index = polish_words.index(polish_word)
    print(english_words[index])
except:
    print('Słowa nie znaleziono\n')

dictionary = {'mama':'mother','tata':'father','witam':'hello'}
if polish_word in dictionary:
    print(dictionary[polish_word])
else:
    print('Nie znaleziono\n')