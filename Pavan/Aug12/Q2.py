item={}

item["Name"] = input("Enter the Name of the Employee.\n")
item["Age"]=int(input("Enter the age.\n"))
item["Place"]=input("Enter the place where employee resides.\n")
item["Salary"]=int(input("Enter the salary.\n"))
item["Previous_company"]=input("Enter the previous company.\n")

for i in item.keys():
        print(f"{i} {item[i]}")
