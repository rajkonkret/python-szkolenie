from flask import Flask
from flask import render_template
from flask import request
from question import Question

app = Flask(__name__)
questions = []
questions.append(Question(0,'Czy Flask to biblioteka mobilna?',False))
questions.append(Question(1,'Czy petla for jest w Pythonie?',True))
questions.append(Question(2,'Czy 4/2 to 2 w Pythonie?',False))
questions.append(Question(3,'Czy w if potrzebny jest ;?',False))
questions.append(Question(4,'Czy Linkedin wykorzystuje Flask?',True))
questions.append(Question(5,'Czy 9%2 to 1?',True))
@app.route("/")
def index():
    return render_template('index.html',questions=questions)
@app.route("/result",methods=['POST'])
def result():
    answers = request.form.items()
    points = 0
    for number,answer in answers:
        if answer =='tak':
            is_true = True
        else:
            is_true = False
        if is_true == questions[int(number)].is_correct:
            points+=1 ## points = points+1
    return render_template('results.html',points=points,questions=questions)

if __name__=='__main__':
    app.run(debug=True,port=4000)