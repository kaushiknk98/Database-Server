import pandas as pd
import sqlite3 as sql

text=pd.read_csv('data.csv')
conn=sql.connect('contact.db')
cid=0
aid=0
pid=0
did=0
for i in range(len(text)):
	cid+=1
	command1='INSERT INTO CONTACT (Contact_id, Fname, Mname, Lname) VALUES ({},\'{}\',\'{}\',\'{}\');'.format(cid,text[i]['first_name'],text[i]['middle_name'],text[i]['last_name'])
	aid+=1
	command2='INSERT INTO ADDRESS (Address_id, Contact_id, Address_type, Address, City, State, Zip) VALUES ({},{},\'{}\',\'{}\',\'{}\',\'{}\',{});'.format(aid,cid,'home',text[i]['home_address'],text[i]['home_city'],text[i]['home_state'],text[i]['home_zip'])
	pid+=1
	ph=text[i]['home_phone']
	ph=ph.split('-')
	acode=int(ph[0])
	phone=''
	phone=phone+ph[1]+ph[2]
	phone=int(phone)
	command3='INSERT INTO PHONE (Phone_id, Contact_id, Phone_type, Area_code, PNumber) VALUES ({},{},\'{}\',{},{});',format(pid,cid,'home',acode,phone)
	did+=1
	command4='INSERT INTO DATES (Date_id, Contact_id, Date_type, dates) VALUES ({},{},\'{}\',\'{}\');'.format(did,cid,'birthday',text[i]['birth_date'])

	conn.execute(command1)
	conn.commit()

	conn.execute(command2)
	conn.commit()

	conn.execute(command3)
	conn.commit()

	conn.execute(command4)
	conn.commit()