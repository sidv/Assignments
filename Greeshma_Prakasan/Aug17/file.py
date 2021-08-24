def create(name):
	f = open(name,"x")
	f.close()
	print("successfully created")
	
def write_data(data,name):
	f = open(name,"w")
	f.write(data)
	f.close()
	
def delete_data(name):
	f = open(name,"w")
	f.truncate()
	f.close()
	print("successfully deleted")
	
def read_data(name):
	f = open(name,"r")
	print(f.read())
	f.close()

def copy(n1,n2):
	with open(n1,"r") as r1:
		with open(n2,"a") as r2:
			for l in r1:
				r2.write(l)
			print("copied successfully")
			
def find(n,s):
	with open(n,"r") as f:
		if s in f.read():
			print(f"{s} is present in the file")
		else:
			print(f"{s} is not in the file")
	
def compare(n1,n2):
	with open(n1,"r") as r1:
		with open(n2,"r") as r2:
			for i in r1:
				for j in r2:
					if i==j:
						print(i)
