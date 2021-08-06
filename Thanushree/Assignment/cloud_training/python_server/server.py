from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hi! From Thanu"
@app.route("/data")
def data():
	return "This is data"

if __name__=="__main__":
	app.run(host='0.0.0.0',port=4000)
