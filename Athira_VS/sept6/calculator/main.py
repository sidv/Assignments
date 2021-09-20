import sys
from calc import Calc

print("Command: Perform multiplication, 10*20")
print("Command Format: python3 main.py 3 10 20")

#while True:
print("______MENU______")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulo Division")
print("7. Exit")

ch = sys.argv[1]

if ch and ch != '7':
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    c = Calc(a, b)



if ch == '1':
    print(f"{a} + {b} = {c.add()}")
elif ch == '2':
    print(f"{a} - {b} = {c.subtract()}")
elif ch == '3':
    print(f"{a} * {b} = {c.multiply()}")
elif ch == '4':
    print(f"{a} / {b} = {c.divide()}")
elif ch == '5':
    print(f"{a} // {b} = {c.floor_divide()}")
elif ch == '6':
    print(f"{a} % {b} = {c.modulo_divide()}")
#elif ch == '7':
    #break
else:
    print("Invalid Entry!!!")
