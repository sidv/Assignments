num1 = input("Enter number")
num2 = input("Enter number")
#Write if else in single  line
#syntax true_expression if condition_epxression else false_expression
res = num1 if num1 > num2 else num2
print(res)

name = input("Enter name")
if not name.isupper():
	print(name.upper())
else:
	print(name.lower())

res = name.upper() if not name.isupper() else name.lower()
print(res)

inp = input("Enter something")
inp = int(inp) if inp.isdigit() else inp
print(inp)

lst = ["10","sid","20","Pavan"]
list(map(lambda x: int(x) if x.isdigit() else x ,lst))
