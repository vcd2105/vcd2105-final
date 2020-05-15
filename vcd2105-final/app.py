# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    return render_template('index.html')

@app.route('/about-me')
def about():
    return'</p>Victoria loves cycling and has completed several long<]/p>'
    '</p>distance rides in NYC, including the 65 mile Velocity</p>'
    '</p>ride which raised money for cancer research, as well as</p>'
    '<p>the final NYC century.</p>'

@app.route('/favorite-people')
def favorite():
     return <img src="static/favoritepeople.jpeg" alt="Favorites">
    

#start the server
if __name__ == "__main__":
    app.run()