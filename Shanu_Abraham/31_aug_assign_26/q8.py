#Write a program (function!) that takes a list and returns a new list 
#that contains all the elements of the first list minus all the duplicates.


def lis_data(lst):
	lst_new =list(set(lst))
	return lst_new

lst1 = [4,6,2,2,2,66,7,3,3,3]
print("list with duplicate elements",lst1)
new_lst = lis_data(lst1)
print("The new list is",new_lst)
	
