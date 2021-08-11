start = int(input("Enter start of range"))
end = int(input("Enter end of range"))
if(start%2 == 0):
    for i in range(start,end+1,2):
        print(i)
else:
    for i in range(start+1,end+1,2):
        print(i)