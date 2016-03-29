"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def submit_form():
	return render_template('index.html')


@app.route('/login', methods=['POST'])
def submit_form_post():
	name = request.form('name')
	age = request.form('age')
	ninja = request.form('FavNinja')
	return render_template('index.html', name=name, age=age, ninja='Patrick Huston')

if __name__ == '__main__':
    app.run()
