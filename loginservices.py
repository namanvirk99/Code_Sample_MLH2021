import sys
sys.path.append('..')
from dl import user
from dl import dbconnection
import mysql.connector as mysql
class authenticate:
	@staticmethod
	def login(un,pa):
		conn=dbconnection.dbfile.connect()
		cursor=conn.cursor()
		query="select Username,Password from usermaster where (Username=%s and Password=%s)"
		cursor.execute(query,(un,pa, ))
		da=cursor.fetchall()
		if(len(da)!=0):
			return True
		else:
			return False
		cursor.close()
		conn.close()
		
	@staticmethod
	def forgot_password():
		pass
		
	@staticmethod
	def change_password(old,new,new1):
		conn=dbconnection.dbfile.connect()
		cursor=conn.cursor()
		query="select Password from usermaster where Password=%s"
		cursor.execute(query,(old, ))
		da=cursor.fetchall()
		if(len(da)!=0):
			if(new==new1):
				query1="update usermaster set Password=%s where Password=%s"
				cursor.execute(query1,(new,old, ))
				conn.commit()
				return 2
			else:
				return 1
		else:
			return 0
		
		cursor.close()	
		conn.close()
		
	@staticmethod
	def logout():
		exit()
			

		
		