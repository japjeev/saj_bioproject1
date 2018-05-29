from flask import Flask, render_template
app = Flask(__name__, static_folder='C:\sajapp\static')

@app.route("/")
def index():
	return render_template('head.html')

@app.route("/summary")
def summary():
	return render_template('summary.html')

@app.route("/lung")
def lung():
	return render_template('lung.html')

@app.route("/breast")
def breast():
	return render_template('breast.html')

@app.route("/colorectal")
def colorectal():
	return render_template('colorectal.html')

app.run(host='0.0.0.0', port=5000)

