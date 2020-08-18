from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk 


root = Tk()
root.title("Postoffice")
root.geometry('200x200')
root.resizable(width=False,height=False)
background_image = ImageTk.PhotoImage(Image.open("login_back.jpg"))
back_label = Label(image=background_image)
back_label.place(x=0, y=0, relwidth=1, relheight=1)
conn = sqlite3.connect('login_dabase.db')
c = conn.cursor()


def login():
	username_login = username_entry.get()
	password_login = password_entry.get()
	
	conn = sqlite3.connect('login_dabase.db')
	c = conn.cursor()
	c.execute('SELECT * FROM logindata')
	records = c.fetchall()
	
	conn.commit()
	conn.close()
	k=0
	for (a,b) in records:
		if username_login==a and password_login==b:
			k = 1
		if k == 1:
			loginwindow = Tk()
			success_label = Label(loginwindow,text="Sucessfully logged in") 
			success_label.grid(row=0,column=0)

		else:
			messagebox.showerror("Error","Incorrect Credentials")
				
def create_account():
	entered_username = username_entry_new.get()
	entered_password = password_entry_new.get()
	conn = sqlite3.connect('login_dabase.db')
	c = conn.cursor()
	c.execute('INSERT INTO logindata VALUES(:username,:password)',
		{
		'username':entered_username,
		'password':entered_password
		})
	conn.commit()
	conn.close()
	signupwindow.destroy()

def signup_command():
	global username_entry_new
	global password_entry_new
	global signupwindow
	signupwindow = Tk()
	signupwindow.geometry('220x200')
	# background_image2 = ImageTk.PhotoImage(Image.open("signup_pic.jpg"))
	# back_label2 = Label(image=background_image2)
	# back_label2.place(x=0, y=0, relwidth=1, relheight=1)
	username_entry_new = Entry(signupwindow)
	username_entry_new.grid(row=0,column=1,pady=5)
	username_label_new = Label(signupwindow,text='Username ')
	username_label_new.grid(row=0,column=0)
	password_entry_new = Entry(signupwindow)
	password_entry_new = Entry(signupwindow, show='*')

	password_entry_new.grid(row=1,column=1,pady=5)
	password_label_new = Label(signupwindow,text='Password ')
	password_label_new.grid(row=1,column=0)
	signup_button_new = Button(signupwindow,text="Create account",command=create_account)
	signup_button_new.grid(row=2,column=0,columnspan=2,ipadx=40)


username_entry = Entry(root)
username_entry.grid(row=0,column=1,pady=5)
username_label = Label(root,text='Username ')
username_label.grid(row=0,column=0)
password_entry = Entry(root)
password_entry = Entry(root, show='*')

password_entry.grid(row=1,column=1,pady=5)
password_label = Label(root,text='Password ')
password_label.grid(row=1,column=0)
login_button = Button(root,text="Login",command=login)
login_button.grid(row=2,column=0,columnspan=2,ipadx=60)
signup_button = Button(root,text="Signup",command=signup_command)
signup_button.grid(row=3,column=0,columnspan=2,ipadx=57,pady=(5,0))

conn.commit()
conn.close()
root.mainloop()


