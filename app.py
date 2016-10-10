#!venv/bin/python
from flask import *
from flask import Flask, render_template, request
from home import *
import jinja2

app = Flask(__name__, template_folder="templates")
app.register_blueprint(home)


if __name__ == '__main__':
	app.run(debug=True)