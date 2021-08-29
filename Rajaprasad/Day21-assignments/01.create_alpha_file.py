import os
string = 'abczefghijklmnopqrstuvwxyz'
for i in string:
    files = '/home/raja/workspace/python/Day21-assignments/file/'
    files += i+'.txt'

    os.mknod(files)
print("All files created successfully !")
