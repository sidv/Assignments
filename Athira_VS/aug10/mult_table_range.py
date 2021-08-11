n = int(input("Enter a number: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))
if start > end:
    print("Invalid range!! Starting value of range greater than the ending value")
i = start
while i <= end:
    print(n, "*", i, "=", n*i)
    i += 1
