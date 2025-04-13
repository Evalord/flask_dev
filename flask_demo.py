from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def index():
	return("hello world")

def username(name):
	return(f"username:{name}")
app.add_url_rule ("/hello/<name>", username)

if __name__ == "__main__":
	app.run(debug = True)


