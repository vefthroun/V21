## Halló heimur með (innbyggðum vef miðlara)

```python
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application
app = Flask(__name__)

# route that calls a Python function. A route maps what you type in the browser (the url) to a Python function.
@app.route('/')
def index():
    # fallið skilar hér streng sem er sendur til biðlara (e. client) í vafra.
    return 'Hello, World!'

# This starts the web app 
if __name__ == '__main__':
    app.run()
 
# Keyrðu python skránna og skoðaðu url í vafra
```
---

#### Aðrir möguleikar

```python
# This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.
# reloader True þýðir að þú þarft ekki að endurkeyra python skrá stöðugt þegar þú gerir kóðabreytingar. 
app.run(debug=True, use_reloader=True)  
```
Sjá einnig: 
- Stillum uhverfisbreytu: `$env:FLASK_APP = "app.py"`
- Keyrum app: `flask run`

Linkar:
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/
