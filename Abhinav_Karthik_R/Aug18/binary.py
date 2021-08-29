lst = []
binary = input("Enter comma seperated binary")
for i in binary.split(","):
    decimal = int(i,2)
    if decimal%5 == 0:
        lst.append(i)
print(",".join(lst))