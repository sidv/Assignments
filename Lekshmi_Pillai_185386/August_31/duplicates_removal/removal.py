"""
8.Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
 
"""
import random

lst = []
def return_removal_lst(data_val):
	return list(set(data_val))

for i in range(20):
	lst.append(int(input("Enter the number : ")))

print(return_removal_lst(lst))
