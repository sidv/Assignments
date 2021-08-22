fruits = {}

while True:
	print("1. Add fruit")
	print("2. Exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		fruit_name = input("Enter fruit name")
		rate = int(input("Enter rate"))
		imported_from = input("Enter the imported form")

		fruits['fruit_name'] = fruit_name
		fruits['rate'] = rate
		fruits['imported_from'] = imported_from

	print(fruits)
	if ch == 2:
		break

