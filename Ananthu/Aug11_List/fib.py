print("Fibonacci between 100")

n = int(input("Enter a range : "))
a = 0
b = 1
while a < n:
	print(a)
	c = a + b
	a = b
	b = c

