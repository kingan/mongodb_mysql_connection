import mysql.connector
cnx = mysql.connector.connect(user='root',host='127.0.0.1',database='python_database')
cursor = cnx.cursor()
add_record = ("INSERT INTO python_table (_id, age, name) VALUES (2,24,'John')")
cursor.execute(add_record)


query = ("SELECT * FROM python_table")
a = cursor.execute(query)

         
from pymongo import MongoClient

client = MongoClient('grv-db01', 27017) 
db = client['djnNews']

record = db.collection.find_one()

add_record = ("INSERT INTO python_table ("+ (", ".join(record.keys())) + ") VALUES (" + (", ".join(record.values()))  +")")
add_record[:57] +"'"+ add_record[57:61] + "'" + add_record[61:]

cursor.close()
cnx.close()
