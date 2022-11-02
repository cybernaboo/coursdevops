from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Happy birthday! Nabil'


app.run(host='0.0.0.0', port=5006)
