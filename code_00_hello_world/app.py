# import Flask package
from flask import Flask

# create an app object
app = Flask(__name__)

# define how app works when receive a petition on main index
# on this case only return a simple text
@app.route('/')
def hello_world():
    return 'Hello World!'
