#write a program to generate list of numbers from 10 to 50 ,use filter to find all even number from lidt
lst=[]
for i in range (10,50):
      lst.append(i)

print(list(filter(lambda a: a%2 == 0,lst)))
