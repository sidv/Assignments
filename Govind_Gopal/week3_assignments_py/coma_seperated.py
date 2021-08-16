lst2 = [] 
txt = (input("Enter a comma seperated sequence of numbers"))
lst = txt.split(",")
print (lst)
for i in lst:
	lst2.append(int(i))
print (f"The sum of the numbers are {sum(lst2)}")
