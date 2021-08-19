def search_student_menu():
	print("\t1.Search by name")
	print("\t2.Search by age")
	print("\t3.Search by stream")
	print("\t4.exit")

def search_st_by_name():
	name = input("\t\tEnter name ")	
	found = False
	for i in students.values():
		if i["name"] == name: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
			break
	if found == False :
		print("\t\tNot found")

def search_st_by_age():
	age = int(input("\t\tEnter age"))
	for i in students.values():
		if i["age"] == age: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
	if found == False :
		print("\t\tNot found")
	
def search_st_by_stream():
	stream = input("\t\tEnter stream")
	for i in students.values():
		if i["stream"] == stream: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
	if found == False :
		print("\t\tNot found")


def search_student():
		
	while True:
		search_student_menu()
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			#Search by name
			search_st_by_name()
		elif ch == 2:
			#Search by age
			search_st_by_age()
		elif ch == 3:
			#serach by stream
			search_st_by_stream()
		elif ch == 4:
			#exit
			break
		else:
			print("Invalid choice")	

