# Write the code to find all the words in data1.txt but not in data2.txt
fd1 = open("data1.txt","r")
fd2 = open("data2.txt","r")
file_data1 = set(fd1.read().split(" "))
file_data2 = set(fd2.read().split(" "))
diff = file_data1.difference(file_data2) #gets all words from file_data1 but not in file_data2
fd1.close()
fd2.close()
