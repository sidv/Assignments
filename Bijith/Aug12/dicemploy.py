employ = {}
while True:
	print("1. add employee")
	print("2. exit")
	ch = int(input("enter your choice:"))
	if ch == 1:
		name=input("enter  name:")
		age=int(input("enter age:"))
		gender=input("enter gender:")
		place=input("enter place:")
		salary=int(input("enter salary:"))
		prev_comp=input("enter previous company:")
		
		employ["name"]=name
		employ["age"]=age
		employ["gender"]=gender
		employ["place"]=place
		employ["salary"]=salary
		employ["previous company"]=prev_comp
 
		print(employ)
	if ch == 2:
		break
		
