string = input("Enter a string")
alcount , dicount = 0,0
for i in string:
    if i.isalpha():
        alcount += 1
    elif i.isdigit():
        dicount += 1
    else:
        pass

print("No of aphabets ",alcount)
print("No of digits ",dicount)
