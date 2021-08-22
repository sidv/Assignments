lst = []
for i in range(10, 50):
    lst.append(i)

print(list(map(lambda a: a**2, (filter(lambda a: a % 2 == 0, lst)))))
