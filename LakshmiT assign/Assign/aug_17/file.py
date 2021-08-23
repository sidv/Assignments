
def create_file(file_name):
    f = open(file_name,"x")

def write_data(file_name,data):
    f = open(file_name,"w")
    f.write(data)
    f.close()

def delete_data(file_name):
    f = open(file_name,"w")
    f.truncate()
    f.close()
def read_data(file_name):
    f = open(file_name, "r")
    f.read()
    f.close()
def copy_data(file1,file2):
    f1 = open(file1,"r")
    f2 = open(file2 , "a")
    f2.write(f1.read())
    f1.close()
    f2.close()
def find_string(file,string):
    f = open(file,"r")
    if string in f.read():
        print("found")
    else:
        print("not found")
    f.close()

def unique(file1,file2):
    f1 = open(file1,"r")
    f2 = open(file2,"r")
    s1 = set(f1.read().split(" "))
    s2 = set(f2.read().split(" "))
    print(s1.symmetric_difference(s2))
    f1.close()
    f2.close()
