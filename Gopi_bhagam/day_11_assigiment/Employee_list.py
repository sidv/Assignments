emp = [] 

while True:
        print("1. Add emp")
        print("2. Delete emp")
        print("3. Search emp")
        print("4. Change emp  name")
        print("5. Display emp")
        print("6.user enter:")
        ch = int(input("Enter your choice:"))
        if ch == 1:
                name = input("Enter name")
                emp.append(name)

        elif ch ==2:
                print("Choose name from this:")
                name = input("Enter name to delete")
                emp.remove(name)
        elif ch == 3:
                name = input("Enter name you want to search:")
                if name in emp:
                        print(name + " is in the list")
                else:
                        print(name + "not in the list")

        elif ch== 4:
                name = input("Enter the name:")
                index = emp.index(name)
                new_name = input("Enter new name")
                emp[index] = new_name

        elif ch == 5:
		 print(emp)
                for i in range(0,len(emp)):
                    print(f'{i+1}.{emp[i-1]}')

        elif ch == 6:
                if ch is None:
                print(" values here" )    
               
        elif ch == 7:
		print("Exit")
		break;
	else:
		print("Invalid Choice")      
        

