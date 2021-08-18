#write a code to create a dictonary from a given number range ,if the input is 4 then the keys in dictionary are 1,2,34
#and value is square of the key{1:1.2:4,3:9,4:16,5:25}
num=int(input("Enter your range"))
number={}
for i in range(1,num+1):
	number[i]=i**2
print(number)
