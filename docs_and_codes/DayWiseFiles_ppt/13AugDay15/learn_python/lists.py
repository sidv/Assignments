	#	6	5	4	3	2	1		Negative indexing.Use -1,-2,-3... to access
	#	0	1	2	 3	4	5 		Postive indexing
frnds = ["Siddhant","Anubhav","Shweta","Rajat","Raja","Pavan"] #List of strings
nums = [10,20,30,40,50,60] #Numbers
mylst = ["Sid",20,10.5] #List with string number and float(decimal)
	#  0       1        2
nested = ["sid",[10,20],["Neha",30]] #Nested List

print(frnds) #printing list
print("______Accessing list element_____________________")
print(frnds[0]) #Siddhant
print(frnds[3]) #Rajat
print(frnds[-1]) #Rajat
#print(frnds[8]) #Error:IndexError: list index out of range

#Lets try on nested 
print(nested[1])
print(nested[-1])

#Slicing of list
print("___________Slicing of list_________________")
print(frnds[1:3]) #frnds[startIndex:endIndex] !End Index is alwys excluded
print(frnds[-3:-1]) # List fetches values in forward direction
print(frnds[:2]) #If you want to fetch from starting then don't need to mention the start Index
print(frnds[1:]) #If you want to fetch from some index to end index then don't need to mention the end Index
print(frnds[:]) #Whole list ['Siddhant', 'Anubhav', 'Shweta', 'Rajat']
print(frnds[:8]) #Whole list

#Steps:
print("________________Steps________________________")
print(frnds[1::2])
print(frnds[::-1]) #reverse the list

#Find length of frnds list
print(len(frnds))


        #  0       1        2
nested = ["sid",[10,20],["Neha",30]] #Nested List

print(len(nested))
print(nested[1]) #[10,20]
print(nested[1][1]) #20
print(nested[2][0]) #Neha
print(nested[0][1]) #i
print(nested[2][0][2]) #h
print(nested[1][1][1]) #Error TypeError: 'int' object is not subscriptable
	
#Square bracet with variable name Is called subscript
