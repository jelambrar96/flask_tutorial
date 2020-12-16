# Code 00

```python

# import Flask package
from flask import Flask

# create an app object
app = Flask(__name__)

# define how app works when receive a petition on main index
# on this case only return a simple text
@app.route('/')
def hello_world():
    return 'Hello World!'

```




To run flask application, we need to run the following line:


```bash
flask run
```

If you need to change port of  flask application you can `--port` argument. look this example:

```bash
flask run --port 6000
```

Additionally, you can change host to be able to receive request from another devices.

```bash
flask run --host 0.0.0.0
```

To check if server is working, you can access to this url [http://localhost:5000](http://localhost:5000)

Note. if you have changed port, you need to change port. On the same way, if you are trying to acces from another device you need to replace *localhost* by *ip device*.

