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
	def __init__(self,name="",age=0,standard="",dob="",grade=""):
		self.name = name
		self.age = age
		self.standard = standard
		self.dob= dob
		self.grade= grade


	def eval_grade(self):
		if self.grade == "A":
			return "Top of the class"
		elif self.grade == "B":
			return "Just Passed"
		else:
			return "Fail"

st1 = Student("Sid",20,"8","4Aug","A")
st2 = Student("Pavan",10,"7","5Aug","A")
print(f"{id(st1)} => {st1}")
print(f"{id(st2)} => {st2}")

print(f"Name => {st1.name} -> {st1.eval_grade()}")

print(f"Name => {st2.name} -> {st2.eval_grade()}")
