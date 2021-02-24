from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(8) # hver beiðni (request) fær random session lykil 
#print(os.urandom(8)) 

# tengin við Firebase Realtime database á firebase.google.com 
config = {
    "apiKey": "AIzaSyBdJjj-rcjvE5AM7RzH80xcaWrM7v5uL1s",
    "authDomain": "verk5-42253.firebaseapp.com",
    "databaseURL": "https://verk5-42253.firebaseio.com",
    "projectId": "verk5-42253",
    "storageBucket": "verk5-42253.appspot.com",
    "messagingSenderId": "650416347994",
    "appId": "1:650416347994:web:62392a4f894e5a61213163",
    "measurementId": "G-6HJ4S9D5CW"
}

fb = pyrebase.initialize_app(config)
db = fb.database()

@app.route('/')
def index():
    # skrifum hnút (node) sem heitir users í gagnagrunn - keyrum (run) aðeins 1. sinni 
    # db.child("users").push({"usr":"Toto", "pwd":"OZ"}) 
    return render_template('index.html')

@app.route('/login', methods=['Get','POST'])
def login():
    login = False
    if request.method == 'POST':

        usr = request.form['usrname']
        pwd = request.form['pswd']

        # tjékka á db er user til?
        u = db.child('users').get().val()
        lst = list(u.items())
        for i in lst:
            if usr == i[1]['usr'] and pwd == i[1]['pwd']:
                login = True
                break
        if login:
            # user fær session id
            session['logged_in'] = usr
            return redirect('/topsecret')
        else:
            return render_template('nologin.html') 
    else:
        return render_template('nomethod.html')            

@app.route('/topsecret')
def secret():
    if 'logged_in' in session:
        return render_template('topsecret.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

# skrá í db
@app.route('/doregister', methods=['GET','POST'])
def doregister():
    usernames = []
    if request.method == 'POST':
        usr = request.form['usrname']
        pwd = request.form['pswd']
        # tjékka á db er user til?
        u = db.child('users').get().val()
        lst = list(u.items())
        for i in lst:
            usernames.append(i[1]['usr'])

        if usr not in usernames:
            db.child('users').push({'usr':usr,'pwd':pwd}) #nýr notandi í db
            return render_template("registered.html")
        else:
            return render_template('userexist.html')
    else:
        return render_template('nomethod.html')   

# villuskilaboð 

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('server_not_found.html'), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
