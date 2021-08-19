



def sum(x,y,z=0):
	print(x+y+z)


sum(10,20)
sum(10,20,30)


def process_data(name,age,salry,company=""):
	tax = 0.10* salry
	print(f"My name is {name} and age is {age} and i pay tax{tax}")
	print(company)

process_data(age=20,name="sid",salry=3000)
process_data(age=23,name="Pavan",salry=4000,company="UST")
