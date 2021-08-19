frnds = ["Siddhant","Ramya","Thanushreee","Bhargav","Gopi"]
    #	     0		1	2	     3     4
len(frnds) #Use len function to find the length of list
print(len(frnds))

#Append data to the list
frnds.append("Shanu") #listVariable.append(data):: This always append at the end of list
print(frnds)

#Insert at certain index
frnds.insert(2,"Sid") #listvariable.insert(index,data)::After inserting  It'll move other data forward
print(frnds)
frnds.insert(7,"Raja") #If you going for out of range index it'll simply append data at end
print(frnds)

#Find index of first occurance of data
frnds.index("Sid")
#frnds.index("jhgjh") #ValueError: 'jhgjh' is not in list :: If data in List

#Remove element
frnds.pop() #Removes data from end
#frnds.pop("Sid") #Error: TypeError: 'str' object cannot be interpreted as an integer
res = frnds.pop(2) #Sid  This function returns value after removing element
#If index is out of range then IndexError

#frnds.remove() #TypeError: remove() takes exactly one argument (0 given)
frnds.remove("Bhargav") #It'll remove that data and it'll not return anything. If element is not there you'll get ValueError
#res = frnds.remove(4) #Error

#Reverse the list
frnds.reverse() #Reverse the list in memory and it does not return anything


#Get count of data in List
print(frnds.count("Raja"))

#Get Copy of list
x = frnds #Points to same location
#Use copy function to get another location
x = frnds.copy()
