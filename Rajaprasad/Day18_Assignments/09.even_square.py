lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda a: a**2, list(filter(lambda a: not a % 2, lst)))))
