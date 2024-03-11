#python-basic-web-app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h2>Hello, Azure Web Apps!</h2>'

if __name__ == '__main__':
    app.run(debug=True)


