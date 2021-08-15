#3.Write a code to search substring in above string using while loop.(Take substring from user) 

var="Click Open link on the dialog shown by your browser"

sub_str=input("enter your substring ;")

while sub_str in var:
    print("found")
    break
else:
    print("Not found!")
    

