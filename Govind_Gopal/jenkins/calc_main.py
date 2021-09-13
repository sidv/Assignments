import calc 
import sys
#while True:
#calc.calc_menu()
ch = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])
if ch == "1":
	calc.add(a,b)
elif ch == "2":
	calc.sub(a,b)
elif ch == "3":
	calc.mul(a,b)
elif ch == "4":
	calc.div(a,b)
#elif ch == "5":
#	break
else:
	print("Invalid input")
