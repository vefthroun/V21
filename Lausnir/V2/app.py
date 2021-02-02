from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# A 
@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/ktsida/<kt>')
def ktsum(kt):
    summa = 0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html' , kt=kt , summa=summa)
# B
# listi (array)
'''
frettir = [
    ["0","fyrirsögn 0","Innihald 0","höfundur 0"]
]
'''
frettir = [
    ["0",
     "Flórens veldur usla á Flórída", "Það er bara helv... vesen á fellibylnum og allt í klessu í Flórída.  Milljónir manna þurftu að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Flórensar...", 
     "dsg@frettir.is"], 
    ["1",
    "Veiðin er dræm þetta haustið", 
     "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", 
     "est@frettir.is"],
    ["2",
    "Ólafía stendur sig vel", 
     "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", 
     "htg@frettir.is"],
    ["3",
    "Ísland dottið úr leik", 
     "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", 
     "dsg@frettir.is"]
    ]

print(type(frettir))

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frettir=frettir)

@app.route('/frett/<int:id>')
def news(id):
    return render_template('frett.html', frett=frettir[id],nr=id)

# Stöðluð villuskilaboð

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template('servererror.html'), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)