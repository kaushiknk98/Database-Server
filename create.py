import sqlite3 as sql

conn=sql.connect('contact.db')

command='CREATE TABLE CONTACT (\
	Contact_id INTEGER PRIMARY KEY,\
	Fname VARCHAR(15), \
	Mname VARCHAR(15),\
	Lname VARCHAR(15));'

if conn.execute(command):
	print("Contact table established successfully")

command='CREATE TABLE ADDRESS (\
	Address_id INTEGER PRIMARY KEY,\
	Contact_id INTEGER REFERENCES CONTACT(Contact_id),\
	Address_type VARCHAR(10),\
	Address VARCHAR(30),\
	City VARCHAR(12),\
	State VARCHAR(12),\
	Zip INTEGER);'

if conn.execute(command):
	print("Address table established successfully")

command='CREATE TABLE PHONE(\
	Phone_id INTEGER PRIMARY KEY,\
	Contact_id INTEGER REFERENCES CONTACT(Contact_id),\
	Phone_type VARCHAR(10),\
	Area_code INTEGER,\
	PNumber INTEGER(7));'

if conn.execute(command):
	print("Phone table established successfully")

command='CREATE TABLE DATES (\
	Date_id INTEGER PRIMARY KEY,\
	Contact_id INTEGER REFERENCES CONTACT(Contact_id),\
	Date_Type VARCHAR(10),\
	Dates DATE);'

if conn.execute(command):
	print("Date table established successfully")
