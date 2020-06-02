from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/car")
def car():
    return render_template('car.html')

@app.route("/cars")
def display_car():
    name = request.args.get('car')
    color = request.args.get('color')
    return render_template('cars.html', name=name, color=color)

@app.route("/form")
def display_form():
    return render_template('form.html')

@app.route("/form2", methods=["POST"])
def form2():
    items = request.form.items()
    email = 'test'
    for argument, value in items:
        print(argument)
        if argument == 'email':
            email = value
    return render_template('form2.html', email=email)
if __name__=='__main__':
    app.run(debug=True)