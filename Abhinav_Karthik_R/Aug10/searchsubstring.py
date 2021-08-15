var = "Click Open link on the dialog shown by your browser"

sub = input("Enter a substring")

ls = len(sub)
lv = len(var)
i = 0
x = 0
while(i < lv):
	if (var[i:ls+i] == sub):
		x = 1
	i=i+1

if(x == 1):
	print("substring found")
else:
	print("not a substring")



