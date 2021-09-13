from calc import Calc
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c_obj = Calc(a,b)
print(c_obj.add())
print(c_obj.sub())
print(c_obj.mul())
print(c_obj.div())

