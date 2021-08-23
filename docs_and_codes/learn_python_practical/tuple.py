num = (10,20)
#Tuple is immutable
#We can store different data types inside it
data = (10, 20, ('sid', 20), 'Neha', ['Sid', 20, 30],20)
	#0   1       2        3           4
	#5   4       3        2           1 
#Fetch elements:
data[0]
print(data[1])
print(data[4])
print(data[-1])
#Length of tuple
print(len(data))

#How to create a empty tuple
x = ()

#For single element
x = (10,)

#Slicing
print(data[1:4])
print(data[:4])
print(data[3:])
print(data[:-3])

#Steps
data[::-1] # reverse The tuple
data[::-2]

#Count function
print(data.count(20))

#Find index 
print(data.index("Neha"))
print(data.index(("sid",20)))
print(data.index(20))

for i in data:
	print(i)



