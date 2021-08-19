#Map iterates on each element of the iteratable object and returns the value according to function

#Filter iterates on each element of the iteratable object and returns when elements only when the condition is true

lst = [2,3,4,5,6,7,8,9]
"""
lst1 =[]
for i in x:
	lst1.append(i*i)
"""
#map(function,list)
lst1 =list(map(lambda a: a*a ,lst))
print(lst1)

lst = list(map(lambda a: str(a),lst))
print(lst)
lst = ["Siddhant","Pavan","Ramya","Thanushree"]
"""
lst = list(map(lambda a: a.upper(),lst))
print(lst)
"""
lst = list(map(lambda a: a.swapcase(),lst))
print(lst)

def convert(a):
	if a%2 == 0:
		return a*a
	else:
		return a*a*a

lst=[2,3,4,5,6,7,8]

lst = list(map(convert,lst ))
lst = list(map(lambda a: convert(a),lst))
print(lst)


lst = [2,3,4,4,56,7,8,9]
#filter( function,list)
#filter function must be evaluated to true or false
"""
lst = list(filter(lambda a: a%2 == 0,lst ))
print(lst)
"""
lst = list(map(lambda a: a*a ,list(filter(lambda a: a%2 == 0 ,lst))))
print(lst)


lst = ["Siddhant","Pavan","Ramya","Raja"]

print(list(filter(lambda a: a[-1] == "a",lst)))

print(list(map(lambda a: a[-1] == "a",lst)))

bio = {
	"name":"Siddhant",
	"age":45,
	"salary":2000
}

print(list(filter(lambda a: a == str(45),bio.values())))



students = {
	"1":{
		"name":"Siddhant",
		"age":30,
		"salary":2000
		},
	"2":{
		"name":"Pavan",
		"age":24,
		"salary":3000
		},
	"3":{
                "name":"Gopi",
                "age":20,
                "salary":5000
                },
	"4":{
                "name":"Sachin",
                "age":31,
                "salary":3000
                }
}

name = input("Enter the name")
filter( lambda a: a["name"] == name, students.values())


lst=list(filter(lambda a: a["age"] > 25,students.values())) #Iterate through values
print(lst)
lst = tuple(filter(lambda a: a["salary"]*0.10 >=300, students.values())) #Itaerate through values
print(lst)

def update_salary(sal):
	for i in students.items():
		pass
	
list(map(lambda a: a["salary"]*0.10+a["salary"] ,students.values())) #Iterating through values and fetching all salaries
lst = list(map( lambda a : (a[0] , a[1].update({"salary":a[1]["salary"]*0.10+a[1]["salary"] }), a[1]) ,students.items() )) #Getting new dictionary by iterating through dictionary.items() function
#print(list(map( lambda a: (a[0],a[1] ) , students.items() )))
print(list(map(lambda a: (a[0],a[2]),lst)))







































