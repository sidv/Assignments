from fruit_store import fruits

def add_fruit():
	f_id = input("Enter fruit id: ")
	f_name = input("Enter fruit name: ")
	f_rate = input("ENter fruit rate: ")
	fruits[f_id] ={
			"name" :f_name,
			"rate":f_rate
		}

def delete_fruit():
	f_id = input("Enter fruit id: ")
	del fruits[f_id]

def display_fruits():
	for i in fruits.values():
		print(f"{i['name']} | {i['rate']}")
