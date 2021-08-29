
#1. Write a program to generate list of numbers from 10 to 50, Use map to find square of all numbers from list
		
lst =[]
square = list(map(lambda a:a*a,list(num for num in range(10,51))))
	
print(square)


#2. Write a program to generate list of numbers from 10 to 50, Use filter to find all even numbers from list

lst =[]
even =[num for num in range(10,51) if num%2 ==0]
print(even)

#3.Write a code to get first three chars of all strings from list ["Siddhant","Pavan","Ramya","Raja"]



lst = ["Siddhant","Pavan","Ramya","Raja"]

list = [ value[0:3] for value in lst ] 
print(list)
