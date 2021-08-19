fdr = open("mybio.txt","r")
fda = open("mybio.txt","a")
#fdr = open("mybio.txt","rb")
"""
data = fdr.read() # Reading whole file content at a time
print(data)

data = fdr.read() #No output beacause cursor is moved to end  of file
print(data)

data= fdr.read(10) #Read 10 characters #No output because cursor is moved to  last location
print(data)
"""

data = fdr.read(20) # 20 chars
print(data)

print(fdr.readline()) # Read till new line char

for i in fdr: #
	print(i)

fda.write("****This is appended data*******")

fdr.close()
fda.close()

#open first file in read mode
#open second file in write mode
#read from first file assign it to variable
#Pass the variable to write function if another file
#Close both files




