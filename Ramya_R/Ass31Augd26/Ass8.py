
#8.Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

lst = []

for i in range(10):
	num = int(input("Enter num: "))
	lst.append(num)
print(lst)

def new_lst(lst):
	return(list(set(lst)))	
print(new_lst(lst))
	

