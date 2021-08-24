#Menu driven Calculator
def print_menu():
	print("Press 1 for add")
	print("Press 2 for substract")
	print("Press 3 for multiply")
	print("Press 4 for division")
	print("Press 5 for floor division")
	print("Press 6 for modulus")
	print("Press 7 to exit")

def read_input():
	x = int(input("Enter number "))
	y = int(input("Enter number "))
	return x,y

def sum(x,y):
	return x + y

def substract(x,y):
	return x - y

def multiply(x,y):
        return x * y

def division(x,y):
        return x / y

def floor_division(x,y):
        return x // y

def modulus(x,y):
        return x % y
