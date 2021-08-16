numb = "1,2,3,4,5,6,7,8,9"
print ("Sum of numbers is ")
sum=0
for i in range(0,18,2):
	a = int(numb[i:i+1])
	sum=sum + a

print (sum)
	
print ("\n Sum of even numberd is ")
sum=0
for i in range(2,18,4):
        a = int(numb[i:i+1])
        sum=sum + a

print (sum)
print ("1,2,3,4,5,6,7,8,9")
sub = input("Enter the sub string \n")
if sub == "1":
	print ("the entered sub string is '1'")
elif sub == "2":
	print ("Entered substring is '2'")
elif sub == "3":
	print ("Entered substring is '3'")
elif sub =="4":
	print ("Entered substring is '4'")
elif sub == "5":
	print ("Entered substring is '5'")
elif sub == "6":
	print ("Entered substring is '6'")
elif sub == "7":
	print ("Entered substring is '7'")
elif sub == "8":
	print ("Entered substring is '8'")
elif sub == "9":
	print ("Entered substring is '9'")
elif sub == ",":
	print ("Entered substring is ','")
else :
	print ("invalid input")
