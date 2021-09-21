#9. Database status:
#	-Show info of database
#Fields('Threads_connected,Threads_created,Threads_running,'Uptime',Queries,Max_used_connections)


import MySQLdb as mysql
import time
import json

db = mysql.connect(host = "localhost",user="root",passwd="root",db="INFORMATION_SCHEMA")
cur = db.cursor()




def database_info():
	cur.execute('SHOW DATABASES')
	res = cur.fetchall() #fetch data
	for i in res:
		print(i)

	
	
def fields():
	cur.execute('SHOW STATUS')
	res = cur.fetchall() #fetch data
	r = dict(res)
	print(f"Threads_connected: {r['Threads_connected']}")	
	print(f"Threads_created: {r['Threads_created']}")
	print(f"Threads_running: {r['Threads_running']}")
	print(f"uptime: {r['Uptime']}")
	print(f"Queries: {r['Queries']}")
	print(f"Max_used_connections: {r['Max_used_connections']}")

	
def process_lists():
	cur.execute('use information_schema')
	cur.execute('select * from tables')
	res = cur.fetchall() #fetch data
	for i in res:
		print(i)

def main_menu():
	print("1.show info of database")
	print("2.show fields")
	print("3.show process lists")
	print("4.exit")

while True:
	main_menu()
	ch = input("Enter your choice : ")
	if ch == "1":
		#show info of databases
		database_info()
		pass
	elif ch == "2":
		fields()
		#show fields
		pass
	elif ch == "3":
		#show process lists
		process_lists()
		pass
	elif ch == "4":
		break;
	else:
		print("Enter correct option")



db.close()
