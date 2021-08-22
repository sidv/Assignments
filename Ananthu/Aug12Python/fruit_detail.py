fruits = {} #Empty dictionary

while True:
	print("1. Add Fruit") 
	print("2. exit")
	ch = int(input("Enter your choice : "))
	if ch == 1:
		#Add fruit
		serial_no = int(input("Enter serial No : "))
		name = input("Enter fruit name : ")
		imp  = input("Enter imported from : ")
		imp_date = input("Enter import date : ")
		price = int(input("Enter the buy_price : "))
		temp ={
			"Fruit_name":name,
			"Imported_from":imp,
			"Imported_date":imp_date,
			"Price":price
			}
		fruits[serial_no] = temp
		print(fruits)

	elif ch == 2:
		break
