import csv
import MySQLdb

book = csv.reader("dataset1.csv")

connection = MySQLdb.connect (host = "localhost", user = "root", db = "Assignment")

cursor = connection.cursor()

with open ('dataset1.csv','r') as csvfile:
	csvreader= csv.reader(csvfile)
	next(csvreader)
	for row in csvreader:
		print (row)
		sql = "INSERT INTO tab_1(ID, Cities,Pincode,Office_ID) VALUES (%s, %s, %s, %s)"
		cursor.execute(sql,(int (row[0]),row[1],int (row[2]),row[3]))
		connection.commit()
print("Commit")

