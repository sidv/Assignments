

def create_file(file):

    with open(file, 'x') as f:
        print("File created successfully")


def write_data(file):

    with open(file, 'w') as f:
        f.write(input('Enter the contents : '))
        print("write data into the file successfully")


def delete_data(file):

    # code to delete entire data
    # but not the file, it is in

    # open file
    with open(file, "r+") as f:

        # absolute file positioning
        f.seek(0)

        # to erase all data
        f.truncate()
        print("all data erased from  the file")


def read_data(file):
    with open(file, 'r') as f:
        print(f.read())


def copy_content(file):
    with open(file, 'r') as f:
        n_file = input("Enter new file name to copy content : ")
        with open(n_file, 'w') as f2:
            f2.write(f.read())

        with open(n_file, 'r') as f3:
            print(f3.read())


def find_copy_certain_str(file):
    with open(file, 'r') as f:
        x = input("Enter string to find")
        for i in f.read().split(" "):
            if i == x:
                n_file = input("Enter new file name to copy content : ")
                with open(n_file, 'w') as f2:
                    f2.write(i)


def unique_element(file):
    with open(file, 'r') as f:
        file2 = input("enter another filename to find unique element : ")
        with open(file2, 'r') as f2:
            print(set(f.read()).symmetric_difference(set(f2.read())))
