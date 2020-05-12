import random as r
available_answer = ("tak","nie")
answer_index = int(r.randint(0,1))
print(available_answer[answer_index])
your_answer = input('Podaj odpowiedź\n')

while your_answer!=available_answer[answer_index]:
    your_answer = input('Podaj odpowiedź\n')

