from calc import Calculator
import add
import sub
import mul
import div
import sys

print(sys.argv)
if sys.argv[1] == "1":
	obj = Calculator(1,2)
	add.add(obj.return_a(),obj.return_b())
elif sys.argv[1] == "2":
	obj = Calculator(4,2)
	sub.sub(obj.return_a(),obj.return_b())
elif sys.argv[1] == "3":
	obj = Calculator(4,2)
	mul.mul(obj.return_a(),obj.return_b())
elif sys.argv[1] == "4":
	obj = Calculator(10,2)
	div.div(obj.return_a(),obj.return_b())

