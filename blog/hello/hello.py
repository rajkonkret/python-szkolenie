from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    name = request.args.get('name')
    surname = request.args.get('surname')
    age = request.args.get('age')
    return render_template('result.html', name=name, surname=surname,age=age)

if __name__=='__main__':
    app.run(debug=True)