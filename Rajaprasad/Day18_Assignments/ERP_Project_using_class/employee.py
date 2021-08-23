

class Emp:
    def __init__(self, emp_id=0, name="", age=0, gender="", place="", salary=0, previous_company="", joining_date=""):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.gender = gender
        self.place = place
        self.salary = salary
        self.previous_company = previous_company
        self.joining_date = joining_date

    def set_name(self, name):
        self.name = name
        return "Name modified successfully"

    def set_age(self, age):
        self.age = age
        return "age modified successfully"

    def set_gender(self, gender):
        self.gender = gender
        return "gender modified successfully"

    def set_salary(self, salary):
        self.salary = salary
        return "salary modified successfully"

    def display(self):
        print(
            f'{self.name} |{self.age} | {self.gender}|{self.place} |{self.salary} | {self.previous_company} | {self.joining_date} ')
