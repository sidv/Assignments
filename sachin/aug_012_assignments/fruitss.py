

"""1.Write a code to store fruit details in dictionary
(fruit_name,rate,imported_from,import_date,buy_price)
Take input from user"""


fruits = {} 

while True:
    print("1. Add fruits")
    print("2. display")
    print("3. exit")
    ch = int(input("Enter your choice"))
    if ch == 1:		
        fruit_id = int(input("enter the fruit id :"))
        name = input("Enter fruit name : ")
        rate = int(input("Enter Rate : "))
        imported_from = input("Enter imported_from : ")
        import_date = input("Enter the import_date : ")
        buy_price = input("Enter buy_price : ")

        temp ={
            "Name":name,
            "Rate":rate,
            "Imported_from":imported_from,
            "Import_date":import_date,
            "Buy_price":buy_price
            }
        fruits[fruit_id] = temp

    elif ch == 2 :
        print(fruits)
    elif ch == 3 : 
        break
    else : 
        print("Invalid ")