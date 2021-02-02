from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

# sækjum gögn úr Json skrá, slóðin þarf að vera frá vefrót að JSON skrá, 
# hér er ég með directory (möppu) sem heitir v3 sem ég geymi app.py kóðann og frettir.json skrá.
with open('v3/frettir.json', "r") as skra:
    data = json.load(skra)  # data = dictonary
# print(data["frettir"][0]["hofundur"]) # Guðmundur

@app.route('/')
@app.route('/index')
def index():
    # sækjum gildi (querystring) ?add=true ef það var sent frá /add route 
    # added inniheldur None (default) eða true 
    added = request.args.get('add')
    return render_template('index.html', added=added)

@app.route('/add')
def add():
    # Uppfærum data dictionary, bætum við fréttafærslu (handvirkt).
    data['frettir'].append({"id":"3","titill":"fyrirsögn 3","innihald":"innihald fréttar 3","hofundur":"hofundur nr. 3","netfang": "3@tskoli.is", "mynd": "3.png"})
    
    # Skrifum í JSON skrá
    with open('v3/frettir.json', "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile,ensure_ascii=False)  
        skra.close() 

    # Við verðum að skila einhverju, förum aftur á forsíðu en látum vita að búið er að bæta við frétt með querystring breytu
    return redirect("/index?add=true")  

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
