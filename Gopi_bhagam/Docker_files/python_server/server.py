from  flask  import Flask
app =Flask (_name_)

@app.route(“/”)
def hello ():
	return  “hi from  sid ”
@app.route(“/”)
def data ():
	return  “this is data  ”
if _name_ == “__main__  ”:
	app.run(host='0.0.0.0',port=4000)


