from  calc import  add
def main_menu():
    print("1. Addition")
    print("2. substaction:")
    print("3. multiplication")
    print("4. division")
    print("5. exit") 

while True:
	main_menu()
	ch = int(input("\tEnter your choice "))
	if ch == 1:
		a=int(input("enter a  num:"))
		b=int(input("enter a  num:"))
		print(add(a,b))

	elif ch == 2:
		a=int(input("enter a  num:"))
		b=int(input("enter a  num:"))
            	print(add(a,b))

	elif ch == 3:
		a=int(input("enter a  num:")
		b=int(input("enter a  num:")
		print(add(a,b))

	elif ch == 4:
		a=int(input("enter a  num:"))
		b=int(input("enter a  num:"))
		print(add(a,b))

	elif ch == 5:
		break
	else:
		print("\tInvalid choice")	




