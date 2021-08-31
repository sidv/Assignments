#to print square of given range

print([x ** 2 for x in range(1,51)])

#use map

print([x for x in map(lambda x : x **2 , range(1,51))])

#to print even number using filter

print([x for x in filter(lambda x : x%2==0 ,range(1,50))])

