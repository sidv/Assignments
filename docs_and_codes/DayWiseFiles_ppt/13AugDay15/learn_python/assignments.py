def process_data():
	return 10,20,34,45


x,y,z,a = process_data()
print(x)
print(y)
print(z)
print(a)
print("________________________________________________")

def process_data1():
	return [2,3,4,5]

lst = process_data1()
x,y,z,a = process_data1()
print(x)
print(y)
print(z)
print(a)

print("_______________________________________________________")

def process_data2(lst):
	return "|".join(lst)

x = ["sid","10","30","40"] 
ret=process_data2(x)
print(ret)


print("______________________________________________")
a = b = c = 10
print(a)
print(b)
print(c)
x, y = (130,120)
print(x)
print(y)
lst =[40,50,80]
x,y,z = lst
print(x)
print(y)
print(z)

data =  {"sid","pavan","gopi","Siddhant","Ramya","Bhargav"}
print(data)
x,y,z,a,b,c = data
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
