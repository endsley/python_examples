#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)


#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
#
#cred = credentials.Certificate('./static/json/pledgeforhumanity.json')
#firebase_admin.initialize_app(cred)
#db = firestore.client()
#
#
#doc_ref = db.collection(u'users').document(u'abcde')
#doc_ref.set({ u'first': u'Ada', u'last': u'Lovelace', u'born': 1815 })
#
#users_ref = db.collection(u'users')
#for doc in users_ref.stream():
#	print(u'{} => {}'.format(doc.id, doc.to_dict()))
#
#
#import pdb; pdb.set_trace()





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

