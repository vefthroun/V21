[Firebase](https://firebase.google.com/) er platform þróað af Google til að búa til vef- og símaöpp.
Firebase býður uppá [Realtime Database](https://firebase.google.com/docs/database?authuser=0) en með slíkan gagnagrunn getum við í rauntíma framkvæmt CRUD aðgerðir þ.e. að lesa, skrifa, eyða eða uppfæra gögn í gagnagrunn, sjá [kynningarmyndband](https://youtu.be/U5aeM5dvUpA).
<br>

---

#### Pyrebase viðbót (a simple python wrapper for the Firebase API)

- [Pyrebase4 viðbótin og aðgerðir](https://github.com/nhorvath/Pyrebase4#database)
   - sýndarumhverfi (venv): `pip install pyrebase4`
- [Introduction To Pyrebase Database](https://dev.to/gogamic/introduction-to-pyrebase-database-2mif)

---

#### Tutorials (vefgreinar)

- [Login með auth()](https://parasmani300.medium.com/pyrebase-firebase-in-flask-d249a065e0df)

---

#### Myndbönd

1. [Að búa til Firebase gagnagrunn (10 mín)](https://youtu.be/6c27DhyWfQI)
1. [Flask app tenging við Firebase gagnagrunn og að skrifa/lesa upplýsingar (13 mín)](https://youtu.be/NDCar59xGRI)
   - [kóðaskráin með myndbandinu](https://github.com/vefthroun/V21/blob/main/Synidaemi/Firebase/app.py)
   - í sýndarumhverfi (virtual env) þarf að sækja: `pip install pyrebase4`
   - Það þarf einnig að bæta við í `config` heitið á gagnagrunninum:<br> `"databaseURL": "https://nafnágagnagrunni.firebaseio.com"`
1. [html form og Firebase gagnagrunnur (14 mín)](https://youtu.be/wyWal1sG6Ms)
   - kóðaskrár fylgja ekki með
1. [Að sækja gögn úr Firebase gagnagrunn og setja í lista (14 mín)](https://youtu.be/64ocVeKm194)
   - ordered dictionary (dictionary í eldri útgáfum, fyrir Python 3.6 voru ekki raðaðir) 
   - [How to parse Pyrebase OrderedDict](https://stackoverflow.com/questions/51976401/how-to-parse-pyrebase-ordereddict/51989082)
   - [tuples](https://realpython.com/python-lists-tuples/#python-tuples)
1. [Að eyða og uppfæra gögn í Firebase gagnagrunni (12 mín)]()
   - [kóðaskráin með myndbandinu](https://github.com/vefthroun/V21/blob/main/Synidaemi/Firebase/app2.py)

<!--
- [Firebase Real Time Database and Flask (27 mín)](https://www.youtube.com/watch?t=1&v=aojoWWMN1r0&feature=youtu.be)
-->
