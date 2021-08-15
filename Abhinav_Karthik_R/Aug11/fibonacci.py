rang = int(input("Enter the range"))
first = 0
second = 1
print("The fibonacci sequence is :")
for i in range(rang):
    print(first)
    sum = first + second
    first = second
    second = sum
