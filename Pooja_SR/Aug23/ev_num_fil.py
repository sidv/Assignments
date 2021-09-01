#write a program to generate list of numbers from 10 to 50 ,use filter to find all even number from list
lst=[]
for i in range (10,50):
      lst.append(i)

lst=list(filter(lambda a: a%2 == 0,lst))
print(f"By lambda: {lst}")
print("__________________________________________________________________________________________________________________________")

e_lst=[i for i in range(10,50) if i%2==0]
print(e_lst)

