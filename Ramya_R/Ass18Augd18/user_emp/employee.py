from user import User


class Employee(User):
    def __init__(self):
        self.empid = ""
        self.name = ""
        self.age = 0
        self.gender = ""

    def insert(self):
        print("Enter Student Details:")
        self.empid = input("\tEmployee id  :")
        self.name = input("\tName: ")
        self.age = input("\tAge: ")
        self.gender = input("\tGender: ")
        self.set_username(input("\tUsername: "))
        self.set_password(input("\tPassword: "))
        self._role = input("Role: ")

    def display(self):
        print("Details:")
        print(f"{self.empid}| {self.name} | {self.age} | {self.gender} | {self.get_username()} | {self._role}")

    def xyz(self):
        super().display()
