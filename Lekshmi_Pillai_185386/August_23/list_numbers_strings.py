#Use Comprehensions or functions
def menu():
	print("1. Generate list of numbers from 10 to 50, Use map to find square of all numbers from list ")
	print("2. Generate list of numbers from 10 to 50, Use filter to find all even numbers from list")
	print("3. Get first three chars of all strings from list")

while True:
	menu()
	ch = int(input("Enter the choice : "))
	if ch == 1:
		lst =[]
		square_number = list(map(lambda x:x*x,list(num for num in range(10,51))))
		print(square_number)
	elif ch == 2:
		lst =[]
		even_number =[num for num in range(10,51) if num%2 ==0]
		print(even_number)
	elif ch == 3:
		lst = ["Siddhant","Pavan","Ramya","Raja"]
		three_list = [i[:3] for i in lst]
		print(three_list)
	elif ch == 4:
		print("Exit")
		break
	else:
		print("Invalid Choice")
