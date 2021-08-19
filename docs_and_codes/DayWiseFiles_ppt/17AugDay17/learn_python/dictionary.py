bio = {
	"name":"Siddhant",
	"age":20,
	"place": "MH"
}

#Fetch value
print(bio.get("name"))
print(bio["name"])

#Fetch all keys
print(bio.keys())

#Fetch all values
print(bio.values())

#Assignment
bio["name"] = "sid" #Change value of  name key:: Update Operation
bio["company"] = "CDAC" #Added new key
bio["a"] = "sid"
print(bio) #print dictionary

#Fetch all key and value
print(bio.items())
print("___________________________________________________")
#Update value in dictionary
bio["name"] = "Siddhant"
bio.update({"age":23})
print(bio)
bio.update({"email":"sid0308v@gmail.com"}) #If key is not there it'll update
print(bio)

#Remove
bio.pop("a")
print(bio)
bio.popitem() #Removes last inserted element
print(bio)
del bio["age"]
print(bio)
#bio.clear() #Empty the dictionary


#Iterate 

for i in bio.keys(): #Iterate through keys
	print(i)

for i in bio.values(): #iterate through keys
	print(i)

for i in bio.keys(): #iterate through keys and change values
	if i == "age":
		bio[i] = 54
	else:
		print("No change")
for i in bio: #Iterate through keys
	print(i)
	print(bio[i])

for i,j in bio.items(): #Iterate through keys and values
	print(f"Key : {i} => value : {j}")

#Copy
x = bio.copy() #Create another copy if dictionary
