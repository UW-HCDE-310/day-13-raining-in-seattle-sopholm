import urllib

from flask import Flask

raining_in_seattle = Flask(__name__)


@raining_in_seattle.route('/')
def index():

	with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
		is_it_raining_in_seattle = response.read().decode()

	if is_it_raining_in_seattle == "true":
		return("Yes!")
	else:
		return("No!")

	def is_it_raining_in_seattle():
		with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
			is_it_raining_in_seattle = response.read().decode()

		if is_it_raining_in_seattle == "true":
			return True
		else:
			return False
