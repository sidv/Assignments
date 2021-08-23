seq = input("Enter comma seperated five numbers")
sum = 0
for i in seq[0:9:2]:
    sum = sum + int(i)
print(sum)