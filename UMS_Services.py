import sys
sys.path.append('..')
from dl import user
from dl import dbconnection
class UMS:
	@staticmethod
	def add(user):
		result=False
		cnx=dbconnection.dbfile.connect()
		cursor=cnx.cursor()
		query="insert into usermaster values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		data=[]
		data.append(user.getUserid())
		data.append(user.getUsername())
		data.append(user.getPassword())
		data.append(user.getUsertype())
		data.append(user.getUserstatus())
		data.append(user.getName())
		data.append(user.getEmail())
		data.append(user.getContact())
		data.append(user.getAddress())
		data.append(user.getGender())
		cursor.execute(query,data)
		if(cursor.rowcount==1):
			result==True
		cnx.commit()
		cursor.close()
		cnx.close()
		return result
	@staticmethod	
	def viewall():
		userlist=[]
		cnx=dbconnection.dbfile.connect()
		cursor=cnx.cursor()
		cursor.execute("select * from usermaster")
		for row in cursor:
			data=user.User()
			data.setUserid(int(row[0]))
			data.setUsername((row[1]))
			data.setPassword((row[2]))
			data.setUsertype((row[3]))
			data.setUserstatus((row[4]))
			data.setName((row[5]))
			data.setEmail((row[6]))
			data.setContact((row[7]))
			data.setAddress((row[8]))
			data.setGender((row[9]))
			userlist.append(data)
		cursor.close()
		cnx.close()
		return userlist
	@staticmethod
	def update(user):
		un=user.getUserid()
		uname=user.getUsername()
		type=user.getUsertype()
		status=user.getUserstatus()
		name=user.getName()
		email=user.getEmail()
		contact=user.getContact()
		address=user.getAddress()
		gender=user.getGender()
		cnx=dbconnection.dbfile.connect()
		cursor=cnx.cursor()
		query="update  usermaster set Username=%s,Usertype=%s,Userstatus=%s,Name=%s,Email=%s,Contact=%s,Address=%s,Gender=%s where Userid=%s"
		cursor.execute(query,(uname,type,status,name,email,contact,address,gender,un, ))
		cnx.commit()
		cursor.close()
		cnx.close()
		return True
	
