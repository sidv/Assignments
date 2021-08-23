from file_opr import *


def file_menu():
    print('\t1.create file')
    print('\t2.write data o the file')
    print('\t3.delete data from the file')
    print('\t4.read data from file')
    print('\t5.copy content to one file to another file')
    print('\t6.find certain string inside a file')
    print('\t7.print unique content from both the file')
    print('\t8.exit')


while True:
    file_menu()
    ch = int(input("Enter choice : "))
    file = input("Enter file name : ")
    if ch == 1:
        # create file
        create_file(file)
    elif ch == 2:
        # write data to file
        write_data(file)
    elif ch == 3:
        delete_data(file)
    elif ch == 4:
        read_data(file)
    elif ch == 5:
        copy_content(file)
    elif ch == 6:
        find_copy_certain_str(file)
    elif ch == 7:
        unique_element(file)
    elif ch == 8:
        break
    else:
        print("Invalid option")
