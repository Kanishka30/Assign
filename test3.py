import MySQLdb
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
	c = MySQLdb.connect(host='localhost',user='root',db='Assignment')
	cursor=c.cursor()
	SQL="use Assignment;"
	cursor.execute(SQL)
	SQL="select * from tab_4;"
	cursor.execute(SQL)
	results=cursor.fetchall()
	return str(results)
if __name__ == '__main__':  
	app.run(host='127.0.0.1',port=8000)
