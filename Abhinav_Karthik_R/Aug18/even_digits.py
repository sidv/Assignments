lst = []
for i in range(1000,3001):
    count = 0
    for j in str(i):
        if int(j)%2 == 0:
            count+=1
        if count == len(str(i)):
            lst.append(i)
print(str(lst)[1:-1])