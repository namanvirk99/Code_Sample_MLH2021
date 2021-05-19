import sys
sys.path.append('..')
from bll import loginservices
import tkinter as tk
from tkinter import messagebox
from tkinter import *


class gui:
	def __init__(self):
		self.root=tk.Tk()
		self.root.geometry("500x400")
		tk.Label(self.root,text="username").grid(row='0',column='0',padx='40',pady='20')
		tk.Label(self.root,text="password").grid(row='1',column='0')

		self.v1=tk.Entry(self.root)
		self.v1.grid(row="0",column="1")

		self.v2=tk.Entry(self.root,show="*")
		self.v2.grid(row="1",column="1")
		
		self.res=tk.Button(self.root,text="Login",command=self.btn_login_clicked)
		self.res.grid(row='2',column='0',pady='10')
		
		self.cl=tk.Button(self.root,text="Cancel",command=self.clear)
		self.cl.grid(row='2',column='1',pady='10')
		
		self.root.mainloop()

	def btn_login_clicked(self):
		un=self.v1.get()
		pa=self.v2.get()
		a=loginservices.authenticate.login(un,pa)
		if(a==True):
			messagebox.showinfo("login","Login Successful!!")
			import mainframes
		else:
			messagebox.showinfo("login","Login Failed!!  Try Again!!")
	
	def clear(self):
		self.root.destroy()

gui()


