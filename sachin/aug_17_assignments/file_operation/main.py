""""2.Write a menu driven code for file operations(Use modules,Take filename from users)
-Create file
-Write data to file
-Delete data from file
-Read data from file
-Copy content of one file to another
-Find certain string inside a file
-Compare two files content and print unique content of both file"""

import crt_read as cr
import delete_write as dw
import cpy_find_compare as cfc




def file_operations():
    print("\t1 . Create file")
    print("\t2 . Write data to file")
    print("\t3 . Delete data from file")
    print("\t4 . Read data from file")
    print("\t5 . Copy content of one file to another")
    print("\t6 . Find certain string inside a file")
    print("\t7 . Compare two files content and print unique content of both file")
    print("\t8 . Exit")


while True:
    file_operations()
    ch = int(input("Enter the choice : "))

    if ch == 1:
        cr.crt_file()
    elif ch == 2:
        dw.write_data()
    elif ch == 3:
        dw.delete_data()

    elif ch == 4:
        cr.read_file()
    elif ch == 5:
        cfc.cpy_data_to_another_file()
    elif ch == 6:
        cfc.str_search_file()
    elif ch == 7:
        cfc.compare_two_files()    

    elif ch == 8:
        break;
    else:
        print("invalid choice")        



