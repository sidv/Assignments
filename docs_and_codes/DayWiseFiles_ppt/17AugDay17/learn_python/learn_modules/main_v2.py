#If you want to import certain function or variable from module  in the main code
#from  modulename import function/variable

from hello import welcome
from hello import data
name = input("Enter your name")
welcome(name)
print(data)
