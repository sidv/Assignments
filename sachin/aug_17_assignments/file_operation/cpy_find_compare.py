def cpy_data_to_another_file():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"

    with open(filepath, 'r') as file :
        filedata = file.read()
    with open('new.txt', 'w') as file :
        file.write(filedata)   

def str_search_file():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"
    string = input("enter the string :")
    with open(filepath, 'r') as file :
        filedata = file.read()
        lst = list(filedata.split(" "))
        for i in lst:
            if i == string:
                print("found the substring")


def compare_two_files():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"
    with open(filepath, 'r') as file :
        filedata1 = file.read()
    with open('new.txt', 'r') as file :
        filedata2 = file.read()
    lst1 =filedata1.split(" ")
    lst2 =filedata2.split(" ")

    set1 = set(lst1)
    set2 = set(lst2)

    print(set1.difference(set2))
    


 
