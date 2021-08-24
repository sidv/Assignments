n = input("Enter the no's : ")
li = n.split(",")

l = list(filter(lambda a:int(a)%5==0,li))

print(",".join(l))
