import os
string = 'abczefghijklmnopqrstuvwxyz'
for i in string:
    files = '/home/superuser/learn_python/Aug24/file'

    files += i+'.txt'

    os.mknod(files)
print("All files created successfully !")
