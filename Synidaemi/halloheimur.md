## Halló heimur 
- https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Halló heimur með innbyggðum flask server

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

# This starts the web app at port 81. 
app.run(host='0.0.0.0', port=81)

# Keyrðu python skránna og skoðaðu url http://localhost:81/ í vafra
```
