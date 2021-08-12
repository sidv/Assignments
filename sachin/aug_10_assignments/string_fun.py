"1.Perform addition of all numbers in the string"

num="1,2,3,4,5,6,7,8,9"

num_all = num[0::2]
total = 0
for i in range(0, len(num_all)):
    total = total + int(num_all[i])

print(total)



