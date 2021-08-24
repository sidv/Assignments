from menu_driven_file import *


def menu_file ():
    print("\t1.create file")
    print("\t2.write data into file")
    print("\t3.delete date ")
    print("\t4.read file")
    print("\t5.copy content file")
    print("\t6.find string")
    print("\t7.copy content file")
    print("\t8.exit")


while True:
	menu_file()
	ch = int(input("\tEnter your choice"))
	file_name=input('enter file name:')
	if ch == 1:
		f1.create_file(file_name)
	elif ch == 2:
		data=input('enter the data')
		f1.write_data(file)
	elif ch ==3 :
	
		f1.delete_data(file_name)
	elif ch == 4:
		f1.read_file(file_name)
	elif ch ==5:
		file2=input('name of the file')
		f1.copy_content(file_name,file2)
	elif ch == 6:
		string=input('enter the string:')
		f1.find_string(file_name,string)
	elif ch == 7:
		file2 =input('enter the seconf file:')
		f1.unique(file_name,file2)
	elif ch ==8:
		print('exit')
		break
	else:
		print("Invalid choice")
