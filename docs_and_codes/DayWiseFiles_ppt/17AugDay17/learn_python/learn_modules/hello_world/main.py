#import hello #write filename don't write .py Filename hello.py

#if modulename is big you can craete alias of the module
import hello as h

x = input("enter your name")
h.welcome(x)  #modulename.functionname() to call the function
print(h.data)
