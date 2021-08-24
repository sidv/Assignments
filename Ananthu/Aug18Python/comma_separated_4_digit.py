items = []
num = [x for x in input(
    "Enter 4 digit binary number with comma separated : ").split(',')]
for item in num:
    x = int(item, 2)
    if not x % 5:
        items.append(item)
print(','.join(items))
