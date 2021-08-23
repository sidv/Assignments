
st=()

i=0

b=input("Enter the all the states")

while i<24:
	if b in st:
		st.append(b)
		i=i+1
for i in st:
	print(i)
