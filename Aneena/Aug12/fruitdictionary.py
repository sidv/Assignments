#Write a code to store fruit details in dictionary(fruit_name,rate,imported_from,import_date,buy_price)
#Take input from user
fruit = {}
while True:

	print("1.Add fruit details")
	name=input("Enter the fruit name\n")
	rate=int(input("enter the rate"))
	imported_from=input("enter the place")
	import_date=int(input("Enter the date"))
	buy_price=int(input("Enter the buy price"))
	fruit =  {
		"name" : name,
		"rate" : rate,
		"imported_from" : imported_from,
		"import_date" : import_date,
		"buy_price" : buy_price
		}
	print(fruit)
	break;	
		
	
