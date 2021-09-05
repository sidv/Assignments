
#6.Take two lists, say for example these two:	
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]	
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]	
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = set(a)
y=set(b)
z=list(x.intersection(y)) #common between the lists 
#z=list(x.union(y))	#all elements in lists without duplicates
print(z)
