print("File operations")


print("1 for create a file")
print("2 write data to file")
print("3 delete from file")
print("8 exit")


choice=int(input())

if choice == 1:
	n=input("enter name of file")
	fd=open(n, "x")
	fd.close()
