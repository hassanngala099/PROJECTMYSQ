from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
	return "hi you are on a dead link"

if __name__ == "__main__":
    app.run()