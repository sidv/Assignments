items = []
num = [x for x int (input(
    "Enter 4digit binary number with comma separated : ").split(',')])
for item in num:
    x = int(item, 2)
    if not x % 5:
        items.append(item)
print(','.join(items))
