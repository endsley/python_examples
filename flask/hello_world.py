#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)



@app.route('/<string:page_name>/')
def render_static(page_name):
	print(page_name)
	return page_name
	#return render_template('%s.html' % page_name)</string:page_name>

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)

