#!/usr/bin/env python

from flask import Flask
app = Flask(pychess)

@app.route("/")
def hello():
	return "Hello World !"
