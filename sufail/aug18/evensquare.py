num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda a:a%2==0 ,num))
square=list(map(lambda a : a*a ,even))
print(square)
