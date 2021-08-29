def square_num():
        for i in range(10,50,2):
                yield i
x = square_num()
print(type(x))
res=list(filter(lambda a : a%2==0 , x))
print(res)


print('********************&&&&compreshension*********************')
'''filter'''
print([x for x in filter(lambda x : x%2 == 0,range(10,51))])

print([x for x in range(10,51) if x%2 == 0])
