from flask import Flask, render_template, json
app = Flask(__name__)

# sækjum gögn úr Json skrá, slóðin þarf að vera frá vefrót að JSON skrá, 
# hér er ég með directory (möppu) sem heitir v3 sem ég geymi app.py kóðann og frettir.json skrá.
with open('v3/frettir.json', "r") as skra:
    data = json.load(skra)  # data = dictonary

@app.route('/')
@app.route('/index')
def index():
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]
    return render_template('frettir.html', title="Verkefni 3.2", frettalisti=data["frettir"], nav=nav)

@app.errorhandler(404)
def pagenotfound(error):
    # 404.html er óútfært
    return render_template('404.html'), 404

@app.errorhandler(500)
def servernotfound(error):
    # 500.html er óútfært
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
