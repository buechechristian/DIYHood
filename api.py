#!venv/bin/python
from flask import *
from flask import Flask, render_template, request
from flask.ext.cors import CORS, cross_origin
from home import *
from jsonGenerator import *
import os
import commands
import json
import base64
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

execfile("./Critic/CriticModel/src/python/get_critique.py")

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "localhost"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/criticize', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type'])
def get_caption():
	if not(request.args.has_key("image")):
		abort(404)
	image = request.args.get("image")
	image = image.replace(" ", "+")

	# print image[0:199]
	# print image[(len(image) - 200):(len(image) - 1)]

	#image is 64 encoded file - decode and save as imageToSave.png
	data = base64.b64decode(image)
	with open("imageToSave.png", "wb") as fh:
		fh.write(data)


	jsonMess = outputInfo('imageToSave.png')



	#print jsonMess
	if jsonMess is None:
		return make_response(jsonify({'error': 'Not found'}), 404)

	print jsonMess

	#cmdstring = "python Critic/CriticModel/src/python/get_critique.py '%s'" % (jsonMess)
	#critique = commands.getstatusoutput(cmdstring)[1]

	# Get analysis from Cognitive Services
	img_digest = json.loads(jsonMess)

	critique = get_critique(img_digest)
	# print critique

	jObject = dict()
	jObject['critique'] = critique
	jObject['accentColor'] = img_digest['color']['accentColor']
	return jsonify(jObject)
	#print cmdstring

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
	app.run(debug=True, port=3000)