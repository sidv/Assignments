num = [1,2,3,4,5,6,7,8,9,10]
#filter even numbers
lst = list(filter(lambda a:a%2 ==0,num))
print(lst)
#map square of even no's
sq = list(map(lambda a : a*a,lst))
print(sq)
