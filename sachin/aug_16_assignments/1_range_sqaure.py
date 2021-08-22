#1. Write a program to generate list of numbers from 10 to 50, Use map to find square of all numbers from list

lst = []


for i in range(10,50):
    lst.append(i)



print(list(map(lambda a: a**2, lst)))