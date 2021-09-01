b = list(range(10,50))
print("_________________list of square________________")
d=list(map(lambda a:a*a,b))
print(d)




print("________________________________filter even number______________")
e=list(filter(lambda a:a%2==0,b))
print(e)
