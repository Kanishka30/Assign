import mysql.connector
import csv

mydb = mysql.connector.connect(
        host="localhost",
        user="assignment",
        passwd="password",
        database="Assignment"
)

mycursor = mydb.cursor()

with open ('dataset1.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        print(row)
