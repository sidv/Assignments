fd = open("mybio.txt","rb") #open file in binary mode for seek always

fd.seek(5)
data=fd.read(20)
print(data)
print(fd.tell())
fd.seek(5,1) #Seek moves bytes by bytes
print(fd.read(3))
fd.seek(-3,1) #negative offset will take you backwards
print(fd.read(3))

line=1
for i in fd:
	if line == 10:
		print(i)
	line+=1

def get_me_line(fd,line):
	res=""
	count=1
	for i in fd:
		if count == line:
			res=i
			break
		count+=1
	return res


get_me_line(fd,13)
