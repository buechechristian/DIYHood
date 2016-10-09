#!venv/bin/python
from flask import *
from flask import Flask, render_template, request
from home import *
from jsonGenerator import *
import os
import commands
# from mhacks.Critic.CriticModel.src.python import *
import json

execfile("./Critic/CriticModel/src/python/get_critique.py")

app = Flask(__name__)

@app.route('/criticize', methods=['GET'])
def get_caption():
	if not(request.args.has_key("image")):
		abort(404)
	image = request.args.get("image")
	# print image
	jsonMess = outputInfo(image)
	#print jsonMess
	if jsonMess is None:
		return make_response(jsonify({'error': 'Not found'}), 404)

	#print jsonMess

	#cmdstring = "python Critic/CriticModel/src/python/get_critique.py '%s'" % (jsonMess)
	#critique = commands.getstatusoutput(cmdstring)[1]
	critique = get_critique(json.loads(jsonMess))
	# print critique

	jObject = dict()
	jObject['critique'] = critique
	return jsonify(jObject)
	#print cmdstring

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
	app.run(debug=True)