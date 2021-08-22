from student import Student


"""
st = Student()
st.insert()
print(st.name)
#print(st.__username)
st.display()
print("________")
st.xyz()
#print(st._role)
#st.u_display()
#print(st.__gender)

"""



st = [] #List of objects

def menu():
	print("1.Add student")
	print("2.Display student")

while True:
	menu()
	ch = int(input("Enter Choice: "))
	if ch == 1:
		#Add student
		st.append(Student())
		st[-1].insert()
	elif ch == 2:
		#display student
		for i in st:
			i.display()
	else:
		print("Invalid choice")

