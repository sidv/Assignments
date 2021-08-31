#write a program to generate lidt of number from 10 to 50,use map to find square of all number from list
lst=[]
for i in range (10,50):
      lst.append(i)

s_lst=list(map(lambda a: a*a,lst))
print(f" By lambda:{s_lst}")

print("____________________________________________________")
s_lst=[i*i for i in range(10,50)]
print(s_lst)
