
cars = {"Audi","BMW","Skoda","Maruti","Innova"}

print(cars) #printing set
print(type(cars)) #Printing type of the cars
print(len(cars)) #length of the cars

#Fetch All elements of cars
for i in cars:
	print(i)

#Particular elements
"Audi" in cars
"Maruti" not in cars

#Copy 
x = cars #Both of them are pointing to same memory location
x= cars.copy()

#Add new element
cars.add("Swift")
print(cars)

#Remove element from set
cars.pop() #Remove random element from set
cars.remove("Swift") #If the element is not there it'll raise error
#cars.remove("XYZ") # KeyError: 'XYZ'
cars.discard("XYZ")  #If the element is not there it'll not raise error
print(cars)

#Clear the set(Empty)
#cars.clear()

#Set Operation
print("_______________________Set Operations_______________________")







car_data1= {"Civic","Swift","Innova","BMW","Ferari"}
car_data2 = {"Maruti","Skoda","BMW","Ferari"}
car_data3 = {"Bugatti","Dogde"}
car_data4 = {"Swift","Innova"}


#Subset
print(car_data4.issubset(car_data1)) #It checks whether car_data4 is subset of car_data1 or not.Returns True or False
print(car_data3.issubset(car_data2))

#Superset
print(car_data4.issuperset(car_data1)) #Testing car_data4 is superset of car_data1
print(car_data4.issuperset(car_data3))

#A.issuperset(B)
#car_data1.issuperset(car_data4)

print("__________Intersection_____________")
#Intersection
print(car_data1.intersection(car_data2)) #Intersection of car_data1 and car_data2
print(car_data4.intersection(car_data2)) #Interection of car_data4 and car_data2
print(car_data4.intersection(car_data1)) #Intersection of car_data4 and car_data1
print(car_data3.intersection(car_data4)) #Intersection of car_data3 with car_data4
print(car_data3.intersection(car_data3)) #Intersecrtion with itself


print("_____________Union_________________")
#Union
print(car_data1.union(car_data2)) 
print(car_data3.union(car_data4))

#Difference 
#A.difference(B) returns elements of A set which are not in  set B 
print("_____________Difference____________")
print(car_data1.difference(car_data2))
print(car_data4.difference(car_data3))

#Symmetric differnce
#A.symmetric_difference(B) returns elements of both A and B which are not common or not in each other
print(car_data1.symmetric_difference(car_data2))

print("__________Disjoint__________________")
#Disjoint set #Means both set are not connected
print(car_data4.isdisjoint(car_data2))
print(car_data3.isdisjoint(car_data4))
print(car_data1.isdisjoint(car_data4))

#Update
print(car_data4.update(car_data3)) #Update car_data3 element into car_data4
print(car_data3)
print(car_data4)
#Intersection update
print(car_data1.intersection_update(car_data2)) 
print(car_data1)
print(car_data2)

#Adding
print("______Adding BMW to data4____________")
car_data4.add("BMW")
print(car_data1)
print(car_data4)

#Difference update
print("____________Difference Update_______________")
print(car_data4.difference_update(car_data1))
print(car_data1)
print(car_data4)


#Adding
print("______Adding SUV to data1____________")
car_data1.add("SUV")
print(car_data1)
print("_______________________________________________")
#Symmeteric difference update
print(car_data1.symmetric_difference(car_data2))
print(car_data1.symmetric_difference_update(car_data2))
print(car_data1)
print(car_data2)

if car_data1.intersection(car_data2) == set():
	print("They are disjoint set")
else:
	print("They are not disjoint set")

x = car_data1.intersection(car_data4)
if x == set():
	print("They are disjoint")
else:
	print("This is not disjoint")

if len(x) == 0:
	print("They are disjoint")
else:
	print("They are not disjoint")


#Create Empty set
data = set()

































