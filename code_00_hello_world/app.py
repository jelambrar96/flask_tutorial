# import Flask package
from flask import Flask

# create an app object
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
