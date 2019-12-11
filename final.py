from tkinter import *
from tkinter import ttk
import mysql.connector as mc
import os

mydb=mc.connect(
    host='localhost',
    user='root',
    password='password',
    database='app_store',
	auth_plugin='mysql_native_password'
)
mycursor=mydb.cursor()

creds = 'tempfile.temp'


def Signup():
	global pwordE
	global nameE
	global roots
	roots = Tk()
	roots.title('Signup')
	instruction = Label(roots, text='Please Enter new Credentials')
	instruction.grid(row=0, column=0, sticky=E)
	nameL = Label(roots, text='New Username: ')
	pwordL = Label(roots,text='New Password: ')
	nameL.grid(row=1, column=0, sticky=W)
	pwordL.grid(row=2, column=0, sticky=W)
	nameE = Entry(roots)
	pwordE = Entry(roots, show='*')
	nameE.grid(row=1, column=1)
	pwordE.grid(row=2, column=1)
	signupButton = Button(roots, text='Signup', command=FSSignup)
	signupButton.grid(columnspan=2, sticky=W)
	roots.mainloop()


def FSSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())
		f.write('\n')
		f.write(pwordE.get())
		f.close()
	roots.destroy()
	Login()


def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

def Login():
	global nameEL
	global pwordEL
	global rootA
	rootA = Tk()
	rootA.title('Login')
	instruction = Label(rootA, text='Please Login\n')
	instruction.grid(sticky=E)
	nameL = Label(rootA, text='Username: ')
	pwordL = Label(rootA, text='Password: ')
	nameL.grid(row=1, sticky=W)
	pwordL.grid(row=2, sticky=W)
	nameEL = Entry(rootA)
	pwordEL = Entry(rootA, show='*')
	nameEL.grid(row=1, column=1)
	pwordEL.grid(row=2, column=1)
	loginB = Button(rootA, text='Login', command=CheckLogin)
	loginB.grid(columnspan=2, sticky=W)
	rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser)
	rmuser.grid(columnspan=2, sticky=W)
	rootA.mainloop()


def Table(title, c_id):
	root = Tk()
	root.title(title)
	mycursor.execute("SELECT * FROM app WHERE c_id="+str(c_id))
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(root)
	treeview["column"] = ["app_id","app_name","description","cost","size","c_id"]
	treeview["show"] = "headings"
	for i in treeview["column"]:
		treeview.heading(i, text = i)
	for i in range(len(treeview["column"])):
		treeview.column('#'+str(i+1), stretch=YES, minwidth=50, width=120)
	treeview.config(height=len(row))
	treeview.pack()
	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2],r[3],r[4],r[5]))
		index+=1
	root.mainloop()


def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()
	if (nameEL.get() == uname) and (pwordEL.get() == pword):
		cc_id=IntVar
		ccategory_name=StringVar
		rootA.destroy()
		def option(x):
			if x==list0[0]:
				Table('utilities', 1)
			elif x==list0[1]:
				Table('books', 2)
			elif x==list0[2]:
				Table('education', 3)
			elif x==list0[3]:
				Table('entertainment', 4)
			elif x==list0[4]:
				Table('finance', 5)
			elif x==list0[5]:
				Table('food', 6)
			elif x==list0[6]:
				Table('health', 7)
			elif x==list0[7]:
				Table('kids', 8)
			elif x==list0[8]:
				Table('lifestyle', 9)
			elif x==list0[9]:
				Table('music', 10)
			elif x==list0[10]:
				Table('games', 11)
			elif x==list0[11]:
				Table('social', 12)
			elif x==list0[12]:
				Table('productivity', 13)
		root=Tk()
		root.geometry("700x500")
		root.resizable(False,False)
		topF = Frame(root,width=700,height=100,bg="black").place(x=0,y=0)
		leftF = Frame(root,width=350,height=300,bg="#B2B1B1").place(x=0,y=100)
		rightF1 = Frame(root,width=350,height=300,bg="#B2B1B1").place(x=350,y=100)
		bottomF = Frame(root,width=700,height=100,bg="black").place(x=0,y=400)

		root.title("MAIN WINDOW")
		Label(topF,text="APP STORE DATABASE",width=28,font=("bold",40),fg="#B2B1B1",bg="black").place(x=0,y=10)
		Label(leftF,text="CATEGORY",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=100)

		list0=['utilities','books','education','entertainment','finanace','food and drinks','health and fitness','kids','lifestyle','music','games','social networking','productivity']
		c=StringVar()
		c.set('---click here to select---')
		droplist=OptionMenu(root,c,*list0,command=option)
		droplist.config(width=22)
		droplist.place(x=40,y=140)

		Label(root,text="INSERT NEW RECORDS",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=100)
		Button(rightF1,text="click here",width=25,command=insert_app_details).place(x=400,y=140)

		Label(root,text="INSERT DEVELOPER DETAILS",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=200)
		Button(rightF1,text="click here",width=25,command=inser_dev_details).place(x=400,y=240)

		Label(root,text="DELETE",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=300)
		Button(rightF1,text="click here",width=25,command=delete_details).place(x=400,y=340)

		Label(root,text="DEVELOPER DETAILS",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=300)
		Button(rightF1,text="click here",width=25,command=dev_details).place(x=40,y=340)

		Label(root,text="TOPCHART",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=200)
		Button(rightF1,text="click here",width=25,command=top_chart).place(x=40,y=240)

		Label(root,width=3,height=20,bg="black").place(x=340,y=100)
		Button(bottomF,text="SHOW ALL ;)",width=30,command=show_all,relief=GROOVE).place(x=200,y=430)

		root.mainloop()
	else:
		r = Tk()
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()

def inser_dev_details():
	def submit_dev():
		mycursor.execute("INSERT INTO developer (d_id, dev_name, website, app_id) VALUES (%s, '%s', '%s', %s)" % (e8.get(), e9.get(), e10.get(), e11.get()))
		mydb.commit()
		root15.destroy()
	root15 = Tk()
	root15.title("INSERT DEVELOPER DETAILS")
	root15.resizable(False,False)
	Label(root15,text="ENTER THE DEVELOPER ID").grid(row=7,column=0)
	Label(root15,text="ENTER THE DEVELOPER NAME").grid(row=8,column=0)
	Label(root15,text="ENTER THE WEBSITE").grid(row=9,column=0)
	Label(root15,text="ENTER THE APP ID").grid(row=10,column=0)
	e8 = Entry(root15)
	e8.grid(row=7,column=1)
	e9 = Entry(root15)
	e9.grid(row=8,column=1)
	e10 = Entry(root15)
	e10.grid(row=9,column=1)
	e11 = Entry(root15)
	e11.grid(row=10,column=1)
	Button(root15,text="SUBMIT",width=25,command=submit_dev).grid(row=11,column=0,columnspan=2)
	root15.mainloop()


def insert_app_details():
	def submit_app():
		# mycursor.execute("DELIMITER$$ CREATE TRIGGER insert_trigger BEFORE INSERT ON app FOR EACH ROW BEGIN DECLARE rowcount INT; SELECT COUNT(*) INTO rowcount FROM app; IF rowcount > 0 THEN UPDATE  END$$  DELIMITER")
		mycursor.execute("INSERT INTO app (app_id, app_name, description, cost, size, c_id) VALUES (%s, '%s', '%s', '%s', '%s', %s)" % (e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e1.get()))
		mydb.commit()
		root14.destroy()
	root14 = Tk()
	root14.title("INSERT APP DETAILS")
	root14.resizable(False,False)
	Label(root14,text="ENTER CATEGORY ID").grid(row=0,column=0)
	Label(root14,text="ENTER THE APP ID").grid(row=2,column=0)
	Label(root14,text="ENTER THE APP NAME").grid(row=3,column=0)
	Label(root14,text="ENTER THE APP DESCRIPTION").grid(row=4,column=0)
	Label(root14,text="ENTER THE COST OF THE APP").grid(row=5,column=0)
	Label(root14,text="ENTER THE SIZE OF THE APP").grid(row=6,column=0)
	e1 = Entry(root14)
	e1.grid(row=0,column=1)
	e3 = Entry(root14)
	e3.grid(row=2,column=1)
	e4 = Entry(root14)
	e4.grid(row=3,column=1)
	e5 = Entry(root14)
	e5.grid(row=4,column=1)
	e6 = Entry(root14)
	e6.grid(row=5,column=1)
	e7 = Entry(root14)
	e7.grid(row=6,column=1)
	Button(root14,text="SUBMIT",width=25,command=submit_app).grid(row=11,column=0,columnspan=2)
	root14.mainloop()


def delete_details():
	def delete_func():
		mycursor.execute("DELETE FROM app WHERE app_id = %s" % (e1.get()))
		mydb.commit()
		root15.destroy()
	root15=Tk()
	root15.title("DELETE DETAILS")
	root15.resizable(False,False)
	Label(root15,text="ENTER THE app_id").grid(row=2,column=0)
	e1 = Entry(root15,text="ENTER app_id TO BE DELETE")
	e1.grid(row=2,column=1)
	Button(root15,text="CLICK HERE TO DELETE",width=25, command = delete_func).grid(row=4,column=0,columnspan=2)
	root15.mainloop()


def dev_details():

	root99=Tk()
	root99.title("DEVELOPER DETAILS")
	root99.resizable(False,False)
	mycursor.execute("SELECT * FROM developer")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(root99)
	treeview["column"]=["dev_id","dev_name","website","app_id"]
	treeview["show"]="headings"
	for i in treeview["column"]:
		treeview.heading(i, text = i)
	for i in range(len(treeview["column"])):
		treeview.column('#'+str(i+1),stretch=YES, minwidth=50, width=120)
	treeview.config(height=len(row))
	treeview.pack()
	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2],r[3]))
		index+=1
	root99.mainloop()


def top_chart():
	root88=Tk()
	root88.title("TOPCHART")
	root88.resizable(False,False)
	mycursor.execute("SELECT * FROM topchart WHERE download_count > 50000 AND rating > 4")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(root88)
	treeview["column"]=["app_id","rating","d_count"]
	treeview["show"]="headings"
	for i in treeview["column"]:
		treeview.heading(i, text = i)

	for i in range(len(treeview["column"])):
		treeview.column('#'+str(i+1), stretch = YES, minwidth = 50, width = 120)
	treeview.config(height=len(row))
	treeview.pack()
	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2]))
		index+=1
	root88.mainloop()


def show_all():
	rootFinal=Tk()
	rootFinal.title("ALL")
	mycursor.execute("DROP VIEW show_all")
	mycursor.execute("CREATE VIEW show_all AS SELECT app_name, cost, size, category_name, rating, download_count FROM app, category, topchart where app.c_id = category.c_id and app.app_id = topchart.app_id")
	mycursor.execute("SELECT * FROM show_all;")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(rootFinal)
	treeview["column"]=["app_name","cost","size","category_name", "rating", "download_count"]
	treeview["show"]="headings"
	for i in treeview["column"]:
		treeview.heading(i, text = i)

	for i in range(len(treeview["column"])):
		treeview.column('#'+str(i+1), stretch=YES, minwidth=50, width=120)
	treeview.config(height=len(row))
	treeview.pack()
	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2],r[3],r[4],r[5]))
		index+=1
	rootFinal.mainloop()


if os.path.isfile(creds):
	Login()
else:
	Signup()

