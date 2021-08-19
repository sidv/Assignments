"""
Syntax: #Creating class
class Classname: #Generally Write classname first letter upper case
	variables=0
	another_var = ""
	def ___init___():
		statements
	def another_func():
		statements

object = Classname() #Creating object
"""
class Student:
	name=""
	age=0
	standard=""
	dob=""
	grade=""
	def __init__(self):
		pass
	def eval_grade(self):
		if self.grade == "A":
			print("Top of the class")
		elif self.grade == "B":
			print("Just Passed")
		else:
			print("Fail")

st1 = Student()
st2 = Student()
print(f"{id(st1)} => {st1}")
print(f"{id(st2)} => {st2}")

st1.name ="Siddhant" #Syntax to access attribute object.attribute
st1.age=10
st1.standard="5"
st1.dob="4August 2010"
st1.grade="B"


st2.name ="Pavan" #Syntax to access attribute object.attribute
st2.age=10
st2.standard="5"
st2.dob="10August 2011"
st2.grade="A"

print(f"Name => {st1.name}")
st1.eval_grade() #syntax to call function object.method()

print(f"Name => {st2.name}")
st2.eval_grade()
