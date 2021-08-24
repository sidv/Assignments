# 10 to 50 square
print([x*x for x in range(10,51)])

#10 to 50 square using map function
print([x for x in map(lambda x : x*x ,range(10,51))])

#10 to 50 even
print([x for x in range(10,51) if x%2 == 0])

#10 to 50 even using filter
print([x for x in filter(lambda x : x%2 == 0,range(10,51))])

#first three char ["Siddhant","Pavan","Ramya","Raja"]
print([x[0:3] for x in ["Siddhant","Pavan","Ramya","Raja"]])