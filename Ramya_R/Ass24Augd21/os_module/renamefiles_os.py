import os
import stat
import string

string = "abcdefghijklmnopqrstuvwxyz"
os.system("ls -l") #Runs linux command
print(os.name)
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("os_module")
os.chmod("createfiles_os.py",stat.S_IRWXU)
os.system("ls -l")
count=1
for i in string:
	os.rename(i+".txt",str(count)+i+".txt")
	count+=1
cw = os.getcwd()
print(os.path.split(cw))
#output
print(os.listdir())

