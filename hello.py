#!/usr/bin/env python

import os
import sys
from flask import Flask, render_template,url_for

app = Flask(__name__)

#@app.route('/')
#def source():
#    html = "hello world!"
#    return html

@app.route('/')
def welcome():
    img = url_for('static',filename = 'cute_ted.jpg')
    img2 = url_for('static',filename = 'imagevsMean.png')
    logo = url_for('static',filename = 'logos.jpg')
    return render_template('welcome.html',logo = logo,img = img,img2 = img2)
#@app.route('/index.html', methods=['GET', 'POST'])
#def lionel():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run()
