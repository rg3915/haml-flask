from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def run():
    names = [
        {
            'id': 1,
            'name': 'Regis',
            'email': 'regis@email.com'
        },
        {
            'id': 2,
            'name': 'Abel',
            'email': 'abel@hotmail.com'
        },
        {
            'id': 3,
            'name': 'Fernanda',
            'email': 'fernanda@gmail.com'
        },
    ]
    return render_template("index.html", names=names)
