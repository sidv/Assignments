

def crt_file():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"
    with open(filepath, 'x') as file :
        print("\tfile created")

def read_file():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"
    with open(filepath, 'r') as file :
        filedata = file.read()
        print(filedata)
        