limit = int(input("Enter limit"))
first,second,sum = 1,1,2
lst = [str(first),str(second)]
for i in range(2,limit):
    lst.append(str(sum))
    first = second
    second = sum
    sum = first+second
s = ","
s = s.join(lst)
print(s)