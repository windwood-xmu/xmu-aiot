from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello-world.html')

@app.route('/hello/<who>')
def hello_name(who: str):
    return render_template('hello-name.html', name=who)

@app.route('/helloall')
def hello_all():
    all:str = 'Every body'
    return render_template('hello-name.html', name=all)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
