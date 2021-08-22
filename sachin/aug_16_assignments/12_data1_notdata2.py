#12.Write the code to find all the words in data1.txt but not in data2.txt


with open('data1.txt', 'r') as file :
  filedata1 = file.read()


with open('data2.txt', 'r') as file :
  filedata2 = file.read()

lstfile1 = filedata1.split(" ")
lstfile2 = filedata2.split(" ")
set1 = set(lstfile1)


set2 = set(lstfile2)

print(set1.difference(set2))