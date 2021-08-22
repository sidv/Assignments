print("Simple FRUIT SHOP")

item={}

item["fruit_name"] = input("Enter the name of the fruit.\n")
item["Rate"]=int(input("Enter the rate.\n"))
item["imported_from"]=input("Enter the place where it was Imported.\n")
item["import_date"]=input("Enter the import date.\n")
item["buy_price"]=input("Enter the  buy price.\n")

for i in item.keys():
	print(f"{i} {item[i]}")
