num = int(input("Enter the range"))
x = 0
y = 1
for i in range(num):
    sum = x +  y
    x = y
    y = sum
print(y)
