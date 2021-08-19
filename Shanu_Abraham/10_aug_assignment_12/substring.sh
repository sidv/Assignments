# search substring in above string using while loop

var="Click Open link on the dialog shown by your browser"

sub_str=input("enter your substring ;")

while sub_str in var:
    print("found")
    break
else:
    print("Not found!")
