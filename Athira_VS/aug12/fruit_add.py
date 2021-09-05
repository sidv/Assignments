fruit = {}

name = input("Enter fruit name:")
rate = input("Enter rate: ")
imp_from = input("Enter the place it is imported from: ")
imp_date = input("Enter the import date: ")
buy_price = input("Enter the bought price: ")

fruit["name"] = name
fruit["rate"] = rate
fruit["imported_from"] = imp_from
fruit["import_date"] = imp_date
fruit["buy_price"] = buy_price

for key, value in fruit.items():
    print(f"{key}  :  {value}")
