from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sensor-index.html')

@app.route('/wendu')
def temperature():
    temperature = 35
    return render_template('sensor-wendu.html', temperature=temperature)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
