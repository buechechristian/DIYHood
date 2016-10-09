#!venv/bin/python
# from flask import *
# from flask import Flask, render_template, request
# from home import *
from jsonGenerator import *
# import os
# import commands
# from mhacks.Critic.CriticModel.src.python import *
import json
import requests
import base64

#execfile("./Critic/CriticModel/src/python/get_critique.py")

#app = Flask(__name__)

def pic_encode():
	pic = "/Users/christianbueche/Desktop/mhacks/images/klee.jpg"
	with open(pic, "rb") as image_file:
		image = base64.b64encode(image_file.read())
		
		# print image[0:199]
		# print image[(len(image) - 200):(len(image) - 1)]
		# print encoded_string
	response = requests.get('http://127.0.0.1:5000/criticize?image=' + image)
	print response.json()


pic_encode()
