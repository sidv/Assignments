class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Areasqr = Square(5)
print(Areasqr.area())     

print(Square().area()) 
	def __init__(self,length=0):
		print(length)
		self.length = length
	def area(self):
		return(super().area(self.length))

num = int(input("Enter the side length : "))
if num == 0 or num == "":
	s = Square()
	print("Sqaure : ",s.area())
else:
	s = Square(num)
	print("Sqaure : ",s.area())
print(dir(math))
