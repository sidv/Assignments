#1 write a code to store fruit details in dictionary(fruit_name,rate,imported_from,import_date,buy_price)take input from user
fruit={}
while True:
	#add fruit_name
	print("add fruit details")
	name=input("enter fruit name")
	rate=int(input("enter fruit rate"))
	import_from=input("enter importer_from")
	import_date=input("enter import_date")
	buy_price=int(input("enter buy_price"))
	fruit ={
		"name":name,
		"rate":rate,
		"import_from":import_from,
		"import_date":import_date,
		"buy_price":buy_price,
		}
	print(fruit)
	break;
