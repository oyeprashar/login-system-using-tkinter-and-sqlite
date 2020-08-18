from tkinter import *
import sqlite3
conn = sqlite3.connect("login_dabase.db")
c = conn.cursor()
c.execute("""CREATE TABLE logindata(
		user_name text,
		password text

	)""")

conn.commit()
conn.close()
