#+,-,*,/,//,%,**
#<,>,<=,>=,==,!=
#and,or
#in, is

a = "10"
b = 10
c = "Sid"
if type(a) is int:
	print("a is integer")
if type(b) is int:
	print("b is integer")
if type(c) is str:
	print("c is string")

frnds = ["Siddhant","Anubhav","Shweta","Rajat"]
if "Shweta" in frnds: # what_to_search in Where_to_search
	print("Found her")
else:
	print("She is not in the frnds list")
print("________________________________________________________________")
for i in frnds: #i is variable which is pointing to frnds elements in each iteration
	print(i)
print("________________________________________________________________")

#for "Shweta" in frnds:  #SyntaxError: cannot assign to literal
#	print("Hi")


a = "Shweta"
for a in frnds:
	print("Hi")

print(a)

if 't' in a:
	print("This name had t char")

a = "Shweta"
if a in frnds:
	print("Found her")
else:
	print("She is't here")

#while a in frnds: #Infinite loop
#	print("Hi")

nested  = ["sid",[10,20],["Neha",30]]

for i in nested:
	if type(i) is list: 
		for j in i :
        	        print(j)
	else:
		print(i)


#Not operator
print("______________________________________________________")
frnds = ["Siddhant","Anubhav","Shweta","Rajat"]

if type(frnds) is list:
	print("It is list")

if type(frnds) is not list:
	print("Correct the data type! You code is wrong")

data = ["Siddhant","Anubhav","Shweta","Rajat"]

if frnds is not data:
	print("They are at differnt location in memory")
else:
	print("They are same")


if a is not None: #a is not None and b is not None
	print("Now I am safe 'a' have some data") 
else:
	print("a has no data")


if "Sid" not in frnds:
	print("Sid is not in the frnds")
else:
	print("Sid is in the frnds")



#__________________________________________________________________
print("_________________________________________________________")
#increment /decrement
i=0
i = i + 1 #Increment i by 1 and assign it to again i
i = i + 1
#Shortcut for above operation
i=0
i+=1 #Increment by 1 and assign it to i:: i = i + 1
i+=2 #Increment by 2 and assign it to i:: i = i + 2

i = i-1
i-=1 #Decrement by 1 and assign it to i
i-=2 #Decrement by 2

i = i*2
i*=2

i/=2 # i = i/2

#Syntax: variable operator=Number


#a=1
#while a<10
#	print(2*a)
#	a+=3





































