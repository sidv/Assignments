class User:

    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_role(self,role):
        self.__role =role

    def get_role(self):
        return self.__role

class Employee(User):

    def __init__(self):
        self.empid = ""
        self.name = ""
        self.age =  ""
        self.gender = ""

    def insert(self):
        self.emp_id = input("\tEmployee id  :")
        self.name = input("\tName: ")
        self.age = input("\tAge: ")
        self.gender = input("\tGender: ")
        self.set_username(input("\tUsername: "))
        self.set_password(input("\tPassword: "))
        self.role = input("\tRole: ")

    def display(self):
        print(f"{self.empid}| {self.name} | {self.age} | {self.gender}  | {self.role}")

    
