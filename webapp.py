# Kelvin Murphy


import flask as fl


app = fl.Flask(__name__)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/ToDo", methods=["GET", "POST"])
def perms():
	ToDo = (fl.request.values["userinput"])
	return ToDo

if __name__ == "__main__":
    app.run()