a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# method 1
cmn = []
for i in a:
    for x in b:
        if x == i:
            if x not in cmn:
                cmn.append(x)

print(cmn)

# method 2
print(list(set([i if x in cmn else cmn.append(x)
      for i in a for x in b if x == i])))
