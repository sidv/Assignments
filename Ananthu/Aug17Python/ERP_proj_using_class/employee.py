

class Emp:
    def __init__(self, emp_id=0, name="", age=0, gender="", place="", salary=0, previous_company="", joining_date=""):
        self._emp_id = emp_id
        self._name = name
        self._age = age
        self._gender = gender
        self._place = place
        self._salary = salary
        self._previous_company = previous_company
        self._joining_date = joining_date

    def set_name(self, name):
        self._name = name
        return "Name modified successfully"

    def set_age(self, age):
        self._age = age
        return "age modified successfully"

    def set_gender(self, gender):
        self._gender = gender
        return "gender modified successfully"

    def set_name(self, salary):
        self._salary = salary
        return "salary modified successfully"
