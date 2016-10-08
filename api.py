#!venv/bin/python
from flask import *
from flask import Flask, render_template, request
from home import *
from artcriticcv import *

app = Flask(__name__)

@app.route('/criticize', methods=['GET'])
def get_caption():
	if not(request.args.has_key("image")):
		abort(404)
	image = request.args.get("image")
	jsonMess = outputInfo(image)
	print jsonMess

	#do some more stuff

	return



if __name__ == '__main__':
	app.run(debug=True)