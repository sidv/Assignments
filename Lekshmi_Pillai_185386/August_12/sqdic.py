#4.Write a code to create a dictonary from given number range
#-If the input is 4 then the keys in dictionary are 1,2,3,4
#-And value is square of the key
#{1:1, 2:4, 3:9 ,4:16, 5:25}


num = int(input("Enter the range"))
dictsquare = {}
for i in range(0,num) : 
	dictsquare[i+1] = (i+1)*(i+1)

print("_____Dictionary Square_____")
print(dictsquare)
