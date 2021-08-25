lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: not x % 2, list(map(lambda x: x**2,lst)))))
