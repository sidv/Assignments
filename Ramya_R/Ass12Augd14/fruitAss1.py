fruits = {} #Empty dictionary
#Add fruit
serial_no = input("Enter serial No: ")
name = input("Enter name: ")
rate = int(input("Enter rate: "))
imp_from = input("Enter place imported from: ")
imp_date = input("Enter date when it is imported: ")
buy_price = input("Enter buy price: ")
temp ={
	"name":name,
	"rate":rate,
	"imp_from":imp_from,
	"imp_date":imp_date,
	"buy_price":buy_price
	}
fruits[serial_no] = temp

print(temp)

#for serial,fruit in fruits.items():
#			print(f"{serial} | {fruit['name']}")
