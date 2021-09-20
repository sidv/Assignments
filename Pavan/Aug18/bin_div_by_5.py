lst = input("Enter the comma separated binary numbers: ").strip().split(",")

for num in lst:
    if int(num, 2) % 5 == 0:
        print(num)
