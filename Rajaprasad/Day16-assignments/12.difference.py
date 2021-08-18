f = open('file1.txt', 'r')
print(f.read())
f2 = open('data2.txt', 'r')
print(f2.read())
print(set(f.read()).difference(set(f2.read())))

f.close()
f2.close()
