import file_handler as fl


def menu():
    print("1.create file \t 2.write data \t 3.delete data")
    print("4.Read data \t 5.Copy file data to another \t 6.find string")
    print("7.unique from two files \t 8.Exit")

while True:
    menu()
    ch = int(input("Enter the choice "))
    file_name = input("Enter file name ")
    if(ch == 1):
        fl.create_file(file_name)
    elif(ch == 2):
        data = input("Enter the data to be written ")
        fl.write_data(file_name,data)
    elif(ch == 3):
        fl.delete_data(file_name)
    elif(ch ==4):
        fl.read_data(file_name)
    elif(ch == 5):
        file2 = input("Enter the name of destination file ")
        fl.copy_data(file_name,file2)
    elif(ch == 6):
        string = input("Enter the string ")
        fl.find_string(file_name,string)
    elif(ch == 7):
        file2 = input("Enter the second file ")
        fl.unique(file_name,file2)
    elif(ch == 8):
        break
    else:
        print("Invalid option")