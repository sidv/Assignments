fdr = open("mybio.txt","r")
#fda = open("mybio.txt","a")

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

print("___________")
data = fdr.read()
print(data)

fdr.close()
#fda.close()
