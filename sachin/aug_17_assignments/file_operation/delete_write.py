def write_data():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"
    with open(filepath, 'w') as file :
        file.write("hii iam sachin and iam also ")


def delete_data():
    filepath = input("Enter the filename : ")
    filepath = filepath +".txt"   
    with open(filepath, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()