fd_1 = open("mybio.txt","r")

fd_2 = open("mydata.txt","w")
"""
data = fd_1.read()
fd_2.write(data)
"""
"""
1.firstline
2.secondline
"""

count = 1
for i in fd_1:
	fd_2.write(f"{count}.{i}")
	count+=1

"""
i=fd_1.read(1)
while i != '' :
	i = fd_1.read(1)
	print(i)
"""
"""
data=fd_1.read()
fd_2.write(data)
"""
fd_1.close()
fd_2.close()
