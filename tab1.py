import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
from tkinter import messagebox

win=tk.Tk()

win.geometry("2000x1000")

conn=sql.connect('contact.db')

tab=ttk.Notebook(win)
tab1=ttk.Frame(tab)

def display():

	command='SELECT c.Contact_id,c.Fname,c.Mname,c.Lname,a.Address_type,a.Address,a.City,a.State,a.Zip,p.Phone_type,p.Area_code,p.PNumber,d.Date_type,d.Dates FROM CONTACT c, ADDRESS a, PHONE p, DATES d \
	WHERE c.Contact_id=a.Contact_id AND c.Contact_id=p.Contact_id AND c.Contact_id=d.Contact_id;'
	cur=conn.execute(command)
	details=cur.fetchall()

	rows=0
	col=0

	l1=tk.Label(tab1,text='id')
	l1.grid(row=0,column=0)

	l1=tk.Label(tab1,text='First Name')
	l1.grid(row=0,column=1)

	l1=tk.Label(tab1,text='Middle Name')
	l1.grid(row=0,column=2)

	l1=tk.Label(tab1,text='Last Name')
	l1.grid(row=0,column=3)

	l1=tk.Label(tab1,text='Address Type')
	l1.grid(row=0,column=4)

	l1=tk.Label(tab1,text='Address')
	l1.grid(row=0,column=5)

	l1=tk.Label(tab1,text='City')
	l1.grid(row=0,column=6)

	l1=tk.Label(tab1,text='State')
	l1.grid(row=0,column=7)

	l1=tk.Label(tab1,text='Zip')
	l1.grid(row=0,column=8)

	l1=tk.Label(tab1,text='Phone Type')
	l1.grid(row=0,column=9)

	l1=tk.Label(tab1,text='Area Code')
	l1.grid(row=0,column=10)

	l1=tk.Label(tab1,text='Phone Number')
	l1.grid(row=0,column=11)

	l1=tk.Label(tab1,text='Date Type')
	l1.grid(row=0,column=12)

	l1=tk.Label(tab1,text='Date')
	l1.grid(row=0,column=13)

	l1=tk.Label(tab1,text='Update')
	l1.grid(row=0,column=14)

	l1=tk.Label(tab1,text='Delete')
	l1.grid(row=0,column=15)


	rows+=1
	entries=list()


	for x in details:
		col=0
		rec=list()
		cid=0

		def del_rec():
			com1='DELETE FROM ADDRESS WHERE Contact_id={}'.format(cid)
			com2='DELETE FROM PHONE WHERE Contact_id={}'.format(cid)
			com3='DELETE FROM DATES WHERE Contact_id={}'.format(cid)
			com4='DELETE FROM CONTACT WHERE Contact_id={}'.format(cid)
			conn.execute(com1) 
			conn.execute(com2) 
			conn.execute(com3) 
			conn.execute(com4)
			messagebox.showinfo('Success','Record Deleted')

			conn.commit()

		for y in x:
			if(col==0):
				cid=y
			e35=tk.Entry(tab1)
			e35.insert('end',y)
			e35.grid(row=rows,column=col)
			rec.append(e35)
			tab1.columnconfigure(col,weight=1)
			col+=1
		entries.append(rec)
		button1=tk.Button(tab1,text='Update')
		button1.grid(row=rows,column=14)
		#tab1.columnconfigure(14,weight=1)
		col+=1
		button2=tk.Button(tab1,text='Delete',command=del_rec)
		button2.grid(row=rows,column=col)
		#tab1.columnconfigure(col,weight=1)
		rows+=1

	#tab1.grid_columnconfigure(0, pad=2)

display()

tab.add(tab1,text='Home')
tab.pack(expan=1, fill="both")

win.mainloop()