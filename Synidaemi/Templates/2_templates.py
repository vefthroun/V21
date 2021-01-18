# sækjum einnig render_template
from flask import Flask, render_template

app = Flask(__name__)

"""
Einfalt Jinja template
"""

@app.route('/')
def index():
    # data
    user = {'username': 'nemandi'}
    # skilum html skránni index.html sem er vistuð í templates möppu (þurfum ekki að vísa í) með gögnum frá dictionary.
    return render_template('tmp1.html', title='Home', user=user)


# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
