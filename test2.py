import csv
import MySQLdb

book = csv.reader("dataset2.csv")


connection = MySQLdb.connect (host = "localhost", user ="root", db = "Assignment")

cursor = connection.cursor()

with open ('dataset2.csv','r') as csvfile:
	csvreader= csv.reader(csvfile)
	next(csvreader)
	for row in csvreader:
		print (row)
		sql = "INSERT INTO tab_2(ID,Office_ID,Population) VALUES (%s, %s, %s)"
		cursor.execute(sql,(int (row[0]),row[1],int (row[2])))
		connection.commit()
print("Commit")

