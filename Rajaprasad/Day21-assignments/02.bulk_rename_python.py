# Python program to explain os.rename() method

# importing os module
import os

count = 0
# Source file path
string = 'abczefghijklmnopqrstuvwxyz'
for i in string:
    file = '/home/raja/workspace/python/Day21-assignments/file/'
    source = file + i+'.txt'
    # print(src_files)

    # destination file path
    count += 1
    destination = file + str(count) + i + '.txt'
    print(destination)
    os.rename(source, destination)


print("Source path renamed to destination path successfully.")
