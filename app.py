from flask import Flask,render_template

#import MySQL

app = Flask(__name__)
#import this to enable database connection
from flaskext.mysql import MySQL

# MySQL configurations



def conect():
	if conn:
		return "Connected to DB"
	else:
		return "DB Refused connection"

@app.route("/")
def home():
	return "hi you are on a dead link"

@app.route("/today")
def returnrecords():
	mysql = MySQL()
	data = cursor.fetchall()
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = ''
	app.config['MYSQL_DATABASE_DB'] = 'lori'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	mysql.init_app(app)
	conn = mysql.connect()
	cursor = conn.cursor()
	data = cursor.fetchall()
	return render_template("yes.html",data=data)
	if __name__ == '__main__':
		app.run()
		