num="1,2,3,4,5,6,7,8,9"
sum = 0
count = 2
while count < len(num):
    print(num[count])
    sum += int(num[count])
    count += 4
print(sum)
