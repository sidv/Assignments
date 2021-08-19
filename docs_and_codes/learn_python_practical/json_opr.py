import json #Use json module #in-built module

#dictionary
d = {
	"name":"Siddhant",
	"age":10,
	"gender":"Male"
}

print(d)
print(type(d))

#Convert dictionary to json
j = json.dumps(d)
print(j)
print(type(j))

#Converts json to dictionary
x = json.loads(j)
print(x)
print(type(x))
