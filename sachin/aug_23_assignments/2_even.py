#2. Write a program to generate list of numbers from 10 to 50, Use filter to find all even numbers from list


even = [value for value in range(10, 50) if value %2 == 0 ]
print(even)