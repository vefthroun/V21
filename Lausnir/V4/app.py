from flask import Flask, render_template
import json, urllib.request 
from datetime import datetime

app = Flask(__name__)

# bensínstöðvar json skrá 
with urllib.request.urlopen("https://apis.is/petrol/") as url:
    gogn = json.loads(url.read().decode()) 
"""
{
	"results": [{
		"bensin95": 198.4,
		"bensin95_discount": null,
		"company": "Atlantsolía",
		"diesel": 193.9,
		"diesel_discount": null,
		"geo": {
			"lat": 65.69913,
			"lon": -18.135231
		},
		"key": "ao_000",
		"name": "Baldursnes Akureyri"
	}, { 
    ...
    }],
	"timestampApis": "2021-02-05T09:29:02.317",
	"timestampPriceChanges": "2020-12-11T18:00:04.733",
	"timestampPriceCheck": ""
}
"""

# Listi yfir alla söluaðila 
def companyList():
    companies = []
    for item in gogn["results"]:	
        if item["company"] not in companies:    # einkvæmur listi
            companies.append(item["company"])   # bætum fyrirtæki við listann
    return companies  # skilum lista

companies = companyList() # söluaðilar, listi 

# Finna lægsta verðið (bensin95 og diesel)
def minPrice(gastype):
    minPetrolPrice = 10000  # einhver há tala
    company = None
    address = None
    for i in gogn['results']:  
        if i[gastype] is not None:
            if i[gastype] < minPetrolPrice:
                minPetrolPrice = i[gastype]
                company = i['company']
                address = i['name']
    return { "gastype": gastype, "minPetrolPrice": minPetrolPrice, "company": company, "address": address }

# Date and time
date = gogn['timestampApis']    # '2021-02-04T22:50:15.468' in yy-MM-dd HH:mm:ss,SSS 
dagsetning = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y. kl: %H:%M')

# forsíðan 
@app.route('/') 
def index():
    bensin95 = minPrice("bensin95")     # lægsta verðið ág 95 okt , dictionary
    diesel = minPrice("diesel")         # lægsta verðið á dísel, dictionary
    return render_template('index.html', dagsetning=dagsetning, companies=companies, gaslist=[bensin95, diesel])

# söluaðili 
@app.route('/company/<company>')
def soluadili(company):
    bensinstodvar = []
    for item in gogn['results']:
        if item["company"] == company:
            bensinstodvar.append({ "name": item["name"], "key": item["key"]})
    return render_template('company.html', company=company, bensinstodvar=bensinstodvar, dagsetning=dagsetning, companies=companies)

# bensínstöð
@app.route('/bensinstod/<key>')
def info(key):
    return render_template('bensinstod.html', bensinstodvar=gogn["results"], key=key, dagsetning=dagsetning, companies=companies)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)