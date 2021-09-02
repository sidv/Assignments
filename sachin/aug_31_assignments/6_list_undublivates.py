#6.write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set1 = set(a)
set2 = set(b)
print(list(set1.intersection(set2)))