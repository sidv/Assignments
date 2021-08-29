#Write a program to generate list of numbers from 10 to 50,
#Use filter to find all even numbers from list

lst =[x for x in range(10,51)]
print(lst)
even_lst = list(filter(lambda x : lst.index(x)%2 == 0,lst))
print(even_lst)
