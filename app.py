from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'lori'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#creating a request handler
@app.route("/")
def index():
	return "Hi There Welcome <b>to  Client Lori End Products"


@app.route("/db",methods=['GET','POST'])
def data():
	#CREATE CURSOR
	#conn=mysql.connect
	#conn = mysql.connect()

	#cur=mysql.connect.cursor()
	#cur = conn.cursor()
	cursor=mysql.connect().cursor()



	#cur.execute("SELECT * FROM Records")
	query1= "SELECT * FROM Records"
	cursor.execute(query1)

	#commit ro DB
	data2=cursor.fetchall()
	return render_template("db.html",data=data2)






if __name__ == '__main__':
	app.run(host='localhost', debug=True)
		