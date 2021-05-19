import sys
sys.path.append('..')
import socket
from bll import loginservices,UMS_Services
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from dl import user
class mainframe:
	def __init__(self):
		self.root3=tk.Tk()
		self.root3.geometry("500x400")
		
		menubar=Menu(self.root3)
		logout=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="Logout",menu=logout)
		logout.add_command(label="Logout",command=loginservices.authenticate.logout)
		logout.add_command(label="Change Password",command=self.cp)
	
		edit=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="UMS",menu=edit)
		edit.add_command(label="Manage User",command=self.new)
		edit.add_command(label="Manage Profile",command=self.profile)
		
		chat=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="Chat",menu=chat)
		
		server=Menu(menubar,tearoff=0)
		menubar.add_cascade(label="Server",menu=server)
		server.add_command(label="Start Server",command=self.ss)
		server.add_command(label="Stop Server")
		
		self.root3.config(menu=menubar)
		self.root3.mainloop()
	
	def cp(self):
		obj1=b()
		obj1.change()
	def new(self):
		obj=a()
		obj.manageuser()
	def profile(self):
		obj2=manageprofile()
		obj2.mp()
	def ss(self):
		obj3=startserver()
		obj3.sts()
		
class b:
	def change(self):
		self.root2=tk.Tk()
		self.root2.geometry("500x400")
		tk.Label(self.root2,text="old password").grid(row='0',column='0',padx='40',pady='20')
		tk.Label(self.root2,text="new password").grid(row='1',column='0')
		tk.Label(self.root2,text="confirm").grid(row='2',column='0',pady='20')
		self.oldpass=tk.Entry(self.root2,show="*")
		self.oldpass.grid(row="0",column="1")
		self.newpass=tk.Entry(self.root2,show="*")
		self.newpass.grid(row="1",column="1")
		self.new1pass=tk.Entry(self.root2,show="*")
		self.new1pass.grid(row="2",column="1")
		self.submit=tk.Button(self.root2,text="Submit",command=self.abc)
		self.submit.grid(row='3',column='0',pady='10')
		self.cancel=tk.Button(self.root2,text="Cancel")
		self.cancel.grid(row='3',column='1',pady='10')
		self.root2.mainloop()
	def abc(self):
		old=self.oldpass.get()
		new=self.newpass.get()
		new1=self.new1pass.get()
		result=loginservices.authenticate.change_password(old,new,new1)
		if(result==0):
			messagebox.showinfo("Status","Old Password didn't match!!")
		elif(result==1):
			messagebox.showinfo("Status","New Password don't match!!")
		else:
			messagebox.showinfo("Status","Password Changed")
class a:
	def manageuser(self):
		self.root1=tk.Tk()
		self.root1.geometry("500x400")
		
		tk.Label(self.root1,text="User ID").grid(row='0',column='0')
		tk.Label(self.root1,text="Username").grid(row='1',column='0')
		tk.Label(self.root1,text="Usertype").grid(row='2',column='0')
		tk.Label(self.root1,text="Userstatus").grid(row='3',column='0')
		tk.Label(self.root1,text="Name").grid(row='4',column='0')
		tk.Label(self.root1,text="Email").grid(row='5',column='0')
		tk.Label(self.root1,text="Contact").grid(row='6',column='0')
		tk.Label(self.root1,text="Address").grid(row='7',column='0')
		tk.Label(self.root1,text="Gender").grid(row='8',column='0')
		self.usertype=tk.StringVar()
		self.usertype.set("Admin")
		self.ut=tk.OptionMenu(self.root1,self.usertype,"Admin","User")
		self.ut.grid(row=2,column=1)
		self.v=tk.StringVar(self.root1)
		self.v.set("0")
		self.r1=tk.Radiobutton(self.root1,text="Male",variable=self.v,value="0")
		self.r1.grid(row='8',column='1')
		self.r2=tk.Radiobutton(self.root1,text="Female",variable=self.v,value="1")
		self.r2.grid(row='8',column='2')
		self.v1=tk.StringVar(self.root1)
		self.v1.set("0")
		self.r3=tk.Radiobutton(self.root1,text="Active",variable=self.v1,value="0")
		self.r3.grid(row='3',column='1')
		self.r4=tk.Radiobutton(self.root1,text="Inactive",variable=self.v1,value="1")
		self.r4.grid(row='3',column='2')
		tkvar=StringVar(self.root1)
		optionlist={"Admin","User"}
		tkvar.set("Admin")
		self.first=tk.Button(self.root1,text="First",command=self.first_btn_click)
		self.first.grid(row='9',column='0')
		self.previous=tk.Button(self.root1,text="Previous",command=self.previous_btn_click)
		self.previous.grid(row='9',column='1')
		self.next=tk.Button(self.root1,text="Next",command=self.next_btn_click)
		self.next.grid(row='9',column='2')
		self.last=tk.Button(self.root1,text="Last",command=self.last_btn_click)
		self.last.grid(row='9',column='3')
		self.add=tk.Button(self.root1,text="Add",command=self.add_btn_click)
		self.add.grid(row='10',column='0')
		self.edit=tk.Button(self.root1,text="Edit",command=self.edit_btn_click)
		self.edit.grid(row='10',column='1')
		self.save=tk.Button(self.root1,text="Save",command=self.save_btn_click)
		self.save.grid(row='10',column='2')
		self.cancel=tk.Button(self.root1,text="Cancel",command=self.cancel_btn_click)
		self.cancel.grid(row='10',column='3')
		self.Userid=tk.Entry(self.root1)
		self.Userid.grid(row="0",column="1")
		self.Username=tk.Entry(self.root1)
		self.Username.grid(row="1",column="1")
		self.Name=tk.Entry(self.root1)
		self.Name.grid(row="4",column="1")
		self.Email=tk.Entry(self.root1)
		self.Email.grid(row="5",column="1")
		self.Contact=tk.Entry(self.root1)
		self.Contact.grid(row="6",column="1")
		self.Address=tk.Text(self.root1,height=4,width=15)
		self.Address.grid(row=7,column=1)
		self.userlist=UMS_Services.UMS.viewall()
		self.current_index=0
		self.addeditflag="view"
		self.save.config(state=DISABLED)
		self.showRecord()
		self.root1.mainloop()
	def enableAll(self):
		self.Userid.config(state=NORMAL)
		self.Username.config(state=NORMAL)
		self.Name.config(state=NORMAL)
		self.Email.config(state=NORMAL)
		self.Contact.config(state=NORMAL)
		self.Address.config(state=NORMAL)
		self.r1.config(state=NORMAL)
		self.r2.config(state=NORMAL)
		self.r3.config(state=NORMAL)
		self.r4.config(state=NORMAL)
		self.ut.config(state=NORMAL)
	def disableAll(self):
		self.Userid.config(state=DISABLED)
		self.Username.config(state=DISABLED)
		self.Name.config(state=DISABLED)
		self.Email.config(state=DISABLED)
		self.Contact.config(state=DISABLED)
		self.Address.config(state=DISABLED)
		self.r1.config(state=DISABLED)
		self.r2.config(state=DISABLED)
		self.r3.config(state=DISABLED)
		self.r4.config(state=DISABLED)
		self.ut.config(state=DISABLED)
	def showRecord(self):
		a.enableAll(self)
		user=self.userlist[self.current_index]
		self.Userid.delete(0,END)
		self.Userid.insert(0,str(user.getUserid()))
		self.Username.delete(0,END)
		self.Username.insert(0,str(user.getUsername()))
		self.usertype.set(user.getUsertype())
		if user.getUserstatus()==1:
			self.v1.set("1")
		else:
			self.v1.set("0")
		self.Name.delete(0,END)
		self.Name.insert(0,str(user.getName()))
		if user.getGender()==0:
			self.v.set("0")
		else:
			self.v.set("1")
		self.Email.delete(0,END)
		self.Email.insert(0,str(user.getEmail()))
		self.Contact.delete(0,END)
		self.Contact.insert(0,str(user.getContact()))
		self.Address.delete(1.0,END)
		self.Address.insert(1.0,str(user.getAddress()))
		self.first.config(state=NORMAL)
		self.previous.config(state=NORMAL)
		self.next.config(state=NORMAL)
		self.last.config(state=NORMAL)
		if(self.current_index==0):
			self.first.config(state=DISABLED)
			self.previous.config(state=DISABLED)
		if(self.current_index==len(self.userlist)-1):
			self.last.config(state=DISABLED)
			self.next.config(state=DISABLED)
		a.disableAll(self)
	def first_btn_click(self):
		self.current_index=0
		self.showRecord()
	def previous_btn_click(self):
		self.current_index-=1
		self.showRecord()
	def next_btn_click(self):
		self.current_index+=1
		self.showRecord()
	def last_btn_click(self):
		self.current_index=len(self.userlist)-1
		self.showRecord()
	def add_btn_click(self):
		a.enableAll(self)
		self.save.config(state=NORMAL)
		self.Userid.delete(0,END)
		self.Username.delete(0,END)
		self.Name.delete(0,END)
		self.Email.delete(0,END)
		self.Contact.delete(0,END)
		self.Address.delete(1.0,END)
		self.Userid.config(state=DISABLED)
		self.first.config(state=DISABLED)
		self.previous.config(state=DISABLED)
		self.next.config(state=DISABLED)
		self.last.config(state=DISABLED)
		self.v1.set("0")
		self.v.set("0")
		self.usertype.set("Admin")
		self.addeditflag="add"
	def edit_btn_click(self):
		a.enableAll(self)
		self.save.config(state=NORMAL)
		self.Userid.config(state=DISABLED)
		self.first.config(state=DISABLED)
		self.previous.config(state=DISABLED)
		self.next.config(state=DISABLED)
		self.last.config(state=DISABLED)
		self.addeditflag="edit"
		
	def save_btn_click(self):
		usr=user.User()
		usr.setUsername(self.Username.get())
		usr.setUsertype(self.usertype.get())
		usr.setUserstatus(int(self.v1.get()))
		usr.setName(self.Name.get())
		usr.setEmail(self.Email.get())
		usr.setContact(self.Contact.get())
		usr.setAddress(self.Address.get(1.0,"end"))
		usr.setGender(int(self.v.get()))
		if self.addeditflag=="add":
			usr.setUsername(self.Username.get())
			usr.setPassword("user")
			if UMS_Services.UMS.add(usr)==False:
				messagebox.showinfo("Add User","User record added Succesfully, default password is 'user'")
			else:
				messagebox.showerror("Add User","User record already exists")
		elif self.addeditflag=="edit":
			self.Userid.config(state=NORMAL)
			usr.setUserid(self.Userid.get())
			self.Userid.config(state=DISABLED)
			if UMS_Services.UMS.update(usr):
				messagebox.showinfo("Edit user record","User record updated successfully")
			else:
				messagebox.showerror("Edit user record","Error")
		self.save.config(state=DISABLED)
		self.add.config(state=NORMAL)
		self.edit.config(state=NORMAL)
		self.userlist=UMS_Services.UMS.viewall()
		if self.addeditflag=="add":
			self.current_index=len(self.userlist)-1
		self.addeditflag="view"
		self.showRecord()
	def cancel_btn_click(self):
		self.root1.destroy()
		
class manageprofile:
	def mp(self):
		self.root=tk.Tk()
		self.root.title("Manage User")
		self.root.geometry("500x400")
		tk.Label(self.root,text="User ID",anchor="w").grid(row=0,column=0,padx=30)
		tk.Label(self.root,text="Username",anchor="w").grid(row=1,column=0)
		tk.Label(self.root,text="Name",anchor="w").grid(row=2,column=0)
		tk.Label(self.root,text="Email",anchor="w").grid(row=3,column=0)
		tk.Label(self.root,text="Contact",anchor="w").grid(row=4,column=0)
		tk.Label(self.root,text="Gender",anchor="w").grid(row=5,column=0)
		tk.Label(self.root,text="Address",anchor="w").grid(row=6,column=0)
		self.userid=tk.Entry(self.root)
		self.userid.grid(row=0,column=1)
		self.username=tk.Entry(self.root)
		self.username.grid(row=1,column=1)
		self.name=tk.Entry(self.root)
		self.name.grid(row=2,column=1)
		self.email=tk.Entry(self.root)
		self.email.grid(row=3,column=1)
		self.contact=tk.Entry(self.root)
		self.contact.grid(row=4,column=1)
		self.gender=tk.StringVar()
		self.gender.set("0")
		self.g0=tk.Radiobutton(self.root,text="Male",variable=self.gender,value="0")
		self.g0.grid(row=5,column=1)
		self.g1=tk.Radiobutton(self.root,text="Female",variable=self.gender,value="1")
		self.g1.grid(row=5,column=2)
		self.address=tk.Text(self.root,height=4,width=15)
		self.address.grid(row=6,column=1)
		self.btn_edit=tk.Button(self.root,text="Edit",width=10,command=self.btn_edit_clicked)
		self.btn_edit.grid(row=7,column=0,pady=20)
		self.btn_save=tk.Button(self.root,text="Save",width=10,command=self.btn_save_clicked)
		self.btn_save.grid(row=7,column=1)
		self.btn_cancel=tk.Button(self.root,text="Cancel",width=10,command=self.btn_cancel_clicked)
		self.btn_cancel.grid(row=7,column=2)
		self.userlist=UMS_Services.UMS.viewall()
		self.current_index=0
		self.btn_save.config(state="disabled")
		self.showrecord()
		self.root.mainloop()
	
	def enableALL(self):
		self.userid.config(state="normal")
		self.username.config(state="normal")
		self.name.config(state="normal")
		self.email.config(state="normal")
		self.contact.config(state="normal")
		self.g0.config(state="normal")
		self.g1.config(state="normal")
		self.address.config(state="normal")
		
	def disableALL(self):
		self.userid.config(state="disabled")
		self.username.config(state="disabled")
		self.name.config(state="disabled")
		self.email.config(state="disabled")
		self.contact.config(state="disabled")
		self.g0.config(state="disabled")
		self.g1.config(state="disabled")
		self.address.config(state="disabled")
	
	def showrecord(self):
		self.enableALL()
		usr=self.userlist[self.current_index]
		self.userid.delete(0,"end")
		self.userid.insert(0,str(usr.getUserid()))
		self.username.delete(0,"end")
		self.username.insert(0,usr.getUsername())
		self.name.delete(0,"end")
		self.name.insert(0,usr.getName())
		self.email.delete(0,"end")
		self.email.insert(0,usr.getEmail())
		self.contact.delete(0,"end")
		self.contact.insert(0,usr.getContact())
		if usr.getGender()==0:
			self.gender.set("0")
		else:
			self.gender.set("1")
		self.address.delete(1.0,"end")
		self.address.insert(1.0,usr.getAddress())
		self.disableALL()
		
	def btn_edit_clicked(self):
		self.enableALL()
		self.btn_save.config(state="normal")
		self.userid.config(state="disabled")
		self.username.config(state="disabled")
		self.btn_edit.config(state="disabled")
	def btn_save_clicked(self):
		self.userid.config(state="normal")
		usr=UMS.search(self.userid.get())
		self.userid.config(state="disabled")
		usr.setName(self.name.get())
		usr.setEmail(self.email.get())
		usr.setContact(self.contact.get())
		usr.setAddress(self.address.get(1.0,"end"))
		usr.setGender(int(self.gender.get()))
		if UMS_Services.UMS.update(usr):
			messagebox.showinfo("Edit user record","User record updated successfully")
		else:
			messagebox.showerror("Edit user record","Error")
		self.btn_save.config(state="disabled")
		self.btn_edit.config(state="normal")
		self.userlist=UMS_Services.UMS.viewall()
		self.showrecord()
	def btn_cancel_clicked(self):
		self.root.destroy()
		
class startserver:
	def sts(self):
		self.root=tk.Tk()
		self.root.title("Start Server")
		self.root.geometry("500x400")
		tk.Label(self.root,text="Port No.").grid(row=0,column=0,padx=30)
		self.portno=tk.Entry(self.root)
		self.portno.grid(row=0,column=1)
		self.start=tk.Button(self.root,text="Start",width=10,pady=20,command=self.stse)
		self.start.grid(row=2,column=1)
		
	def stse(self):
		self.s=socket.socket()
		self.s.bind(("",int(self.portno.get())))
		self.label.config(text="socket server created")
		self.s.listen(1)
		self.label.config(text="waiting for client request")
		self.conn,self.addr=self.s.accept()
		self.label.config(text="connected to"+str(self.addr))
		self.conn.close()
		
mainframe()
		
		