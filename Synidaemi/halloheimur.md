## Halló heimur með (innbyggðum vef miðlara)
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/

```python
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application. Don't worry about that __name__ object, it's just a convention.
app = Flask(__name__)


# route() maps what you type in the browser (the url) to a Python function.
# @app.route() (@ er decorator í python) bindur fallið index() við URL. 
# Whenever a browser requests a URL, the associated function is called and the return value is sent back to the browser
@app.route('/')
def index():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return 'Hello, World!'

# This starts the web app 
if __name__ == '__main__':
    # run, starts a built-in development server
    app.run(debug=True, use_reloader=True)   
            # debug=True. debug er nytsamlegt í vefþróun, gefur skýrari villuskilaboð.
            # use_reloader. use_reloader=True þýðir að þú þarft ekki að endurkeyra python skrá stöðugt þegar þú gerir kóðabreytingar. 
     
# Keyrðu python skránna í CLI(cmd/terminal) og skoðaðu url í vafra (localhost)
```

#### Nánari skýringar

- Flask API documentation [`Flask(__name__)`](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask)
- Decorators[`@app.route('/')`](https://github.com/vefthroun/V21/blob/main/Efnistok/decorators.md)
- Python documentation [`__main__`](https://docs.python.org/3/library/__main__.html)
- Stack Overflow [`if __name__ == '__main__':`](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

---
 
### Aðrir stillingar

- Stillum uhverfisbreytu: `$env:FLASK_APP = "app.py"`
- Keyrum app: `flask run`


