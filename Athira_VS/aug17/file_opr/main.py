from file_operations import *

while True: 
    print("__________MENU__________")
    print("1. Create file")
    print("2. Write data to file(Any data)")
    print("3. Delete data from file")
    print("4. Read data from file")
    print("5. Copy content of one file to another")
    print("6. Find certain string inside a file")
    print("7. Print unique content of 2 files")
    print("8. Exit")

    ch = input("Enter your choice: ")

    if ch and ch != '8':
        file = input("Enter file name: ")

    if ch == '1':
        # Create file
        fd = create_file(file)
        if fd:
            print(f"Created file {file}")
    
    elif ch == '2':
        # Write data to file(Any data)
        write_to_file(file)
        
    elif ch == '3':
        # Delete data from file
        delete_data(file)
        
    elif ch == '4':
        # Read data from file
        read_data(file)

    elif ch == '5':
        # Copy content of one file to another
        file2 = input("Enter 2nd file name: ")
        copy_file(file, file2)

    elif ch == '6':
        # Find certain string inside a file
        data = input("Enter string to be searched: ")
        search_string(file, data)

    elif ch == '7':
        # Print unique content of 2 files
        file2 = input("Enter 2nd file name: ")
        unique_content(file, file2)

    elif ch == '8':
        # Exit
        break
    else:
        print("Invalid Entry!!!")





