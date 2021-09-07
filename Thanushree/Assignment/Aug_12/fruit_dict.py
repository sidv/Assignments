fruit_details = {}
while True:
	print("1. Add fruit details to fruit store")
	print("2. Display all fruit store") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		sl_no = int(input("Enter fruit details to store in dictionary:"))
		f_name = input("Enter fruit name")
		f_rate = input("Enter fruit rate")
		imp_frm = input("Enter fruit imported from")
		imp_date = input("Enter fruit imported date")
		by_price = input("Enter fruit buy price") 
		temp ={
			"fname":f_name,
			"frate":f_rate,
			"import_from":imp_frm,
			"import_date":imp_date,
			"buy_price":by_price
			}
		fruit_details[sl_no] = temp
	elif ch == 2:
		print(fruit_details)
	elif ch == 6:
		break
