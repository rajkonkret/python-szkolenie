
quiz = {
    'Czy Polska leży w Europie': 'tak',
        'Czy 2+2=5': "nie",
        'Czy Python to język programowania?':'tak'
        }
questions = quiz.keys()
score =0
for question in quiz:
    #print(i)


#for question in  questions:
    answer = input(question + '\n').lower()
    if answer == quiz[question]:
        print('Poprawna odpowiedź')
        score+=1
print("Zdobyłeś pkt: ",score)