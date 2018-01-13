#!/bin/env python

from flask import Flask, url_for
#from swf.consts import *
#from swf.tag import *
#from swf.movie import SWF



app = Flask(__name__)

@app.route('/')
def root():
    return open("index.html").read()



@app.route('/game.swf')
def game():
    return app.open_resource("Ballgame.swf").read()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
