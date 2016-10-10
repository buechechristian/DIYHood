from flask import *
# from test import *


home = Blueprint('home', __name__, template_folder="templates")

@home.route('/', methods=['GET'])
def get_caption():
	return render_template("index.html", caption="", caption_bool=False)

@home.route('/', methods = ['POST'])
def post_route():
	picurl = request.form['picurl']
	outputDict = outputInfo(picurl)


	# use colors and tags to input as seeds

	# autocorrect

	# replace colors with outputColors and nouns with Tags

	#to avoid compiler error
	caption = ""

	return render_template("index.html", caption=caption, caption_bool=False)

@home.route('/result', methods=['GET'])
def get_result():
	return render_template("result.html")

@home.route('/howitworks', methods=['GET'])
def get_how_it_works():
	return render_template("howitworks.html")