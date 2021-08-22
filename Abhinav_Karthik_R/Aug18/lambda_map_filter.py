lst = [1,2,3,4,5,6,7,8,9,10]
a = list(map(lambda a: a * a,list((filter(lambda a: lst.index(a)%2 == 1, lst)))))
print(a)
