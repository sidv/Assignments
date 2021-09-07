#program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def lst_data(lst):
	lst_new =list(set(lst))
	return lst_new
lst1 = [4,6,2,2,2,66,7,3,3,3]
print("List with duplicate elements\n:",lst1)
new_lst = lst_data(lst1)
print("New list:\n",new_lst)
	
