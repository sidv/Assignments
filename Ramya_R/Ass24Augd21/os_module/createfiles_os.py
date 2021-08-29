import os
import stat
import string

os.system("ls -l") #Runs linux command
print(os.name)
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("os_module")
os.chmod("createfiles_os.py",stat.S_IRWXU)
os.system("ls -l")
for i in string.ascii_lowercase:
	with open(i + ".txt","w") as f:
		f.writelines(i)
cw = os.getcwd()
print(os.path.split(cw))

print(os.listdir())
#os.remove("a.txt")
print(os.listdir())
