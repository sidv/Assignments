print("Reading from file..............")
fd=open("mybio.txt","r")
data = fd.read()
print(data)
fd.close()

print("Writing to file...........")
fd = open("mybio.txt","w")
fd.write("I am performing write operation")
fd.close()

print("Appending to file..........")
fd = open("mybio.txt","a")
fd.write("I am performing append operation")
fd.close()

fd=open("data.txt","x")
fd.close()
