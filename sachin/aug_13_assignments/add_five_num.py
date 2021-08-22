#2.Write a python code which accepts a sequence of comma seperated five numbers and find the addition of all of them


five_num = input("Enter the numbers with comma seperated :")

rem_coma = five_num.split(",")
total = 0 
for i in rem_coma:
    total = total + int(i)
print("total amount : ",total)    