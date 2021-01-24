# Þurfum þennan
from flask import Flask, json

# Tengjumst við skránna bekkur.json (verður að vera til)
with open("bekkur.json","r") as skra:
    gogn = json.load(skra)

# Kíkjum i breytuna gogn
print(gogn)




