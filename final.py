from tkinter import *
from tkinter import ttk
import mysql.connector as mc
import os

mydb=mc.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='app_store'
)
mycursor=mydb.cursor()

creds = 'tempfile.temp'


app_table = ["app_id","app_name","description","cost","size","c_id"]
dev_table = ["dev_id","dev_name","website","app_id"]
top_chart_table = ["app_id","rating","d_count"]
show_all_table = ["app_id","app_name","description","cost","size","c_id"]

def put(*args):
    cid=cc_id.get()
    categoryname=ccategory_name.get()
    mycursor.execute("insert into category(c_id,category_name)\
                            values('"+str(cid)+"','"+categoryname+"')")
    mycursor.execute("commit")
    mydb.close()


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


def option(x):
	if x==list0[0]:
		Table('utilities', 0, app_table)
	elif x==list0[1]:
		Table('books', 1, app_table)
	elif x==list0[2]:
		Table('education', 2, app_table)
	elif x==list0[3]:
		Table('entertainment', 3, app_table)
	elif x==list0[4]:
		Table('finance', 4, app_table)
	elif x==list0[5]:
		Table('food', 5, app_table)
	elif x==list0[6]:
		Table('health', 6, app_table)
	elif x==list0[7]:
		Table('kids', 7, app_table)
	elif x==list0[8]:
		Table('lifestyle', 8, app_table)
	elif x==list0[9]:
		Table('music', 9, app_table)
	elif x==list0[10]:
		Table('games', 10, app_table)
	elif x==list0[11]:
		Table('social', 11, app_table)
	elif x==list0[12]:
		Table('productivity', 12, app_table)

		
def Table(title, c_id, table):
	root = Tk()
	root.title(title)
	mycursor.execute("SELECT * FROM app WHEREww c_id="+str(c_id))
	row=mycursor.fetchall()
	mydb.commit()

	treeview=ttk.Treeview(root)
	treeview["column"] = table
	treeview["show"] = "headings"

	for i in table:
		treeview.heading(i, text = i)
		
	for i in range(len(table)):
		if (i == 0) or (i == 5):
			treeview.column('#'+str(i+1), width = 90)
		else:
			treeview.column('#'+str(i+1), stretch=YES, minwidth=50, width=120)
	treeview.config(height=len(row))
	treeview.pack()

	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2],r[3],r[4],r[5]))
		index+=1
	root.mainloop()		
		
def insert_details():
	appid=StringVar()
	appname=StringVar()
	descriptionvar=StringVar()
	costvar=StringVar()
	sizevar=StringVar()
	categoryid=StringVar()
	categoryname=StringVar()
	def submit():
		app_id_var=appid.get()
		app_name_var=appname.get()
		description_var=descriptionvar.get()
		cost_var=costvar.get()
		size_var=sizevar.get()
		category_id_var=categoryid.get()
		mycursor.execute("""INSERT INTO app (app_id,app_name,description,cost,size,c_id) VALUES('app_id_var','app_name_var','description_var','cost_var','size_var',category_id_var)""")
		mydb.commit()

	root14=Tk()
	root14.title("INSERT DETAILS")
	root14.resizable(False,False)

	label5=Label(root14,text="ENTER CATEGORY ID").grid(row=0,column=0)
	label6=Label(root14,text="ENTER CATEGORY NAME").grid(row=1,column=0)
	label11=Label(root14,text="ENTER THE APP ID").grid(row=2,column=0)
	label7=Label(root14,text="ENTER THE APP NAME").grid(row=3,column=0)
	label8=Label(root14,text="ENTER THE APP DESCRIPTION").grid(row=4,column=0)
	label9=Label(root14,text="ENTER THE COST OF THE APP").grid(row=5,column=0)
	label10=Label(root14,text="ENTER THE SIZE OF THE APP").grid(row=6,column=0)
	label12=Label(root14,text="ENTER THE DEVELOPER ID").grid(row=7,column=0)
	label13=Label(root14,text="ENTER THE DEVELOPER NAME").grid(row=8,column=0)
	label14=Label(root14,text="ENTER THE WEBSITE").grid(row=9,column=0)
	label15=Label(root14,text="ENTER THE EMAIL").grid(row=10,column=0)
	

	entry5=Entry(root14,textvariable=categoryid).grid(row=0,column=1)
	entry6=Entry(root14,textvariable=categoryname).grid(row=1,column=1)
	entry11=Entry(root14,textvariable=appid).grid(row=2,column=1)
	entry7=Entry(root14,textvariable=appname).grid(row=3,column=1)
	entry8=Entry(root14,textvariable=descriptionvar).grid(row=4,column=1)
	entry9=Entry(root14,textvariable=costvar).grid(row=5,column=1)
	entry10=Entry(root14,textvariable=sizevar).grid(row=6,column=1)
	entry15=Entry(root14).grid(row=7,column=1)
	entry12=Entry(root14).grid(row=8,column=1)
	entry13=Entry(root14).grid(row=9,column=1)
	entry14=Entry(root14).grid(row=10,column=1)

	button56=Button(root14,text="SUBMIT",width=25,command=submit).grid(row=11,column=0,columnspan=2)

	root14.mainloop()

def delete_details():
	
	root15=Tk()
	root15.title("DELETE DETAILS")
	root15.resizable(False,False)

	label12=Label(root15,text="DELETE RECENT INSERTION").grid(row=0,column=0)
	button1=Button(root15,text="CLICK HERE",width=25).grid(row=0,column=1)

	label2=Label(root15,text="ENTER THE app_id").grid(row=2,column=0)
	entry2=Entry(root15,text="ENTER app_id TO BE DELETE").grid(row=2,column=1)
	button2=Button(root15,text="CLICK HERE TO DELETE",width=25).grid(row=4,column=0,columnspan=2)

	root15.mainloop()


def dev_details():

	root99=Tk()
	root99.title("DEVELOPER DETAILS")
	root99.resizable(False,False)

	mycursor.execute("SELECT * FROM dev")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(root99)
	treeview["column"]=["dev_id","dev_name","website","app_id"]
	treeview["show"]="headings"

	treeview.heading("dev_id",text="dev_id")
	treeview.heading("dev_name",text="dev_name")
	treeview.heading("website",text="website")
	treeview.heading("app_id",text="app_id")

	treeview.column('#1',width=90)
	treeview.column('#2',stretch=YES, minwidth=50, width=120)
	treeview.column('#3',stretch=YES, minwidth=50, width=120)
	treeview.column('#4',width=90)

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
	mycursor.execute("SELECT * FROM topchart")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(root88)
	treeview["column"]=["app_id","rating","d_count"]
	treeview["show"]="headings"

	treeview.heading("app_id",text="app_id")
	treeview.heading("rating",text="rating")
	treeview.heading("d_count",text="d_count")

	treeview.column('#1',width=90)
	treeview.column('#2',stretch=YES, minwidth=50, width=120)
	treeview.column('#3',stretch=YES, minwidth=50, width=120)
	

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

	mycursor.execute("SELECT * FROM app")
	row=mycursor.fetchall()
	mydb.commit()
	treeview=ttk.Treeview(rootFinal)
	treeview["column"]=["app_id","app_name","description","cost","size","c_id"]
	treeview["show"]="headings"

	treeview.heading("app_id",text="app_id")
	treeview.heading("app_name",text="app_name")
	treeview.heading("description",text="description")
	treeview.heading("cost",text="cost")
	treeview.heading("size",text="size")
	treeview.heading("c_id",text="c_id")

	treeview.column('#1',width=90)
	treeview.column('#2',stretch=YES, minwidth=50, width=120)
	treeview.column('#3',stretch=YES, minwidth=50, width=120)
	treeview.column('#4',stretch=YES, minwidth=50, width=120)
	treeview.column('#5',stretch=YES, minwidth=50, width=120)
	treeview.column('#6',width=90)

	treeview.config(height=len(row))
	treeview.pack()
	index=0
	for r in row:
		treeview.insert('','end',text=str(index),values=(r[0],r[1],r[2],r[3],r[4],r[5]))
		index+=1

	rootFinal.mainloop()

def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()
	if (nameEL.get() == uname) and (pwordEL.get() == pword):
		cc_id=IntVar
		ccategory_name=StringVar
		rootA.destroy()

		root=Tk()
		root.geometry("700x500")
		root.resizable(False,False)

		topF=Frame(root,width=700,height=100,bg="black").place(x=0,y=0)
		leftF=Frame(root,width=350,height=300,bg="#B2B1B1").place(x=0,y=100)
		rightF1=Frame(root,width=350,height=300,bg="#B2B1B1").place(x=350,y=100)
		bottomF=Frame(root,width=700,height=100,bg="black").place(x=0,y=400)

		root.title("MAIN WINDOW")
		labelmain=Label(topF,text="APP STORE DATABASE",width=28,font=("bold",40),fg="#B2B1B1",bg="black").place(x=0,y=10)
		label0=Label(leftF,text="CATEGORY",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=100)

		list0=['utilities','books','education','entertainment','finanace','food and drinks','health and fitness','kids','lifestyle','music','games','social networking','productivity'];
		c=StringVar()
		c.set('---click here to select---')
		droplist=OptionMenu(root,c,*list0,command=option)
		droplist.config(width=22)
		droplist.place(x=40,y=140)
		
		label1=Label(root,text="INSERT NEW RECORDS",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=100)
		b20=Button(rightF1,text="click here",width=25,command=insert_details).place(x=400,y=140)
		label2=Label(root,text="DELETE",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=200)
		b21=Button(rightF1,text="click here",width=25,command=delete_details).place(x=400,y=240)
		label3=Label(root,text="DEVELOPER DETAILS",width=38,fg="#B2B1B1",bg="#414141").place(x=350,y=300)
		b22=Button(rightF1,text="click here",width=25,command=dev_details).place(x=400,y=340)
		label4=Label(root,text="USER DETAILS",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=300)
		b23=Button(rightF1,text="click here",width=25,command=dev_details).place(x=40,y=340)
		label5=Label(root,text="TOPCHART",width=38,fg="#B2B1B1",bg="#414141").place(x=0,y=200)
		b24=Button(rightF1,text="click here",width=25,command=top_chart).place(x=40,y=240)
		label6=Label(root,width=3,height=20,bg="black").place(x=340,y=100)
		button_all=Button(bottomF,text="SHOW ALL ;)",width=30,command=show_all,relief=GROOVE).place(x=200,y=430)
		root.mainloop()
	else:
		r = Tk()
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()



def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

if os.path.isfile(creds):
	Login()
else:
	Signup()

