# name: app.py
# date: some beatiful day
# version: 2.0

from flask import Flask, jsonify, make_response, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/status')
def status():
	return make_response(jsonify(
		app="my flask applicaiton",
		status=200), 200)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

