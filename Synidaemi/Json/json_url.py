from flask import Flask, json
import urllib.request  # opnar leið að port 80

app = Flask(__name__)

# Tengjumst við internetið - 
with urllib.request.urlopen("http://apis.is/currency/lb") as url:
    gogn = json.loads(url.read().decode())

    print(gogn)
