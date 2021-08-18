'''
1. Write a program to generate list of numbers from 10 to 50, Use map to find square of all numbers from list
2. Write a program to generate list of numbers from 10 to 50, Use filter to find all even numbers from list
3. Write a code to get first three chars of all strings from list
["Siddhant","Pavan","Ramya","Raja"]

'''
lst = []
lst1 = []
for i in range (10,50):
	lst.append(i)
	lst1.append(i)
print("Use map to find square")
print(list(map(lambda a: a*a,lst)))

print("Use filter to find all even numbers")
print(list(filter(lambda a:a%2==0,lst1)))

print("first three chars")

lst2 = ["Siddhant","Pavan","Ramya","Raja"]
print(list(map(lambda a:a[:3],lst2)))
