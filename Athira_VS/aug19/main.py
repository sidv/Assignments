import circle as cir
import rectangle as rt
import subclass_square as sq

print("***********Square*************")
a = sq.Square(int(input("Enter the length of the square: ")))
print(f"Area of square is : {a.area()}")
s = sq.Shape()
print(f"Area of shape is : {s.area()}")




print("***********Rectangle*************")
a = rt.Rectangle(input("Enter length of rectangle a: "), input("Enter breadth of rectangle a: "))
b = rt.Rectangle(input("Enter length of rectangle b: "), input("Enter breadth of rectangle b:"))

print(f"Area of rectangle a: {a.area()}")
print(f"Area of rectangle b: {b.area()}")
print("a.__doc__()")
print(a.__doc__())
print("\nstr(a)")
print(str(a))

print(f"a>b : {a > b}")

#print("Printing a+b")
print(f"a + b = {a+b}")

print("***********Circle*************")

a = cir.Circle(input("Enter radius of circle a: "))
b = cir.Circle(input("Enter radius of circle b: "))

print(f"Area of circle a: {a.area()}")
print(f"Area of circle b: {b.area()}")
print("a.__doc__()")
print(a.__doc__())
print("\nstr(a)")
print(str(a))

#print("Printing a+b")
print(f"a + b = {a+b}")


