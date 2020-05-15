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
    return render_template('about-me.html')

@app.route('/favorite-people')
def favorite():
     return render_template('favorite-people.html')
    

#start the server
if __name__ == "__main__":
    app.run()