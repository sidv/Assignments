fruits = {} #Empty dictionary

while True:
	print("1. Add fruit") 
	print("2. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add fruit
		fruit_name = input("Enter fruit name")
		rate = int(input("Enter rate"))
		imported_from = input("Enter the imported from")

		fruits['fruit_name']= fruit_name
		fruits['rate'] = rate
		fruits['imported_from']=imported_from

	print(fruits)
