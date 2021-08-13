print("ERP system")
emp={}


def main_menu():
    print("1.-Add Employee \n2.-Delete Employee \n3.-Search Employee by name \n4.-Change Employee Data \n5.Display \n6.exit")

def add_employee():
    #add employee
        emp_id = 0 
        serial_no = int(input('Enter serial no : '))
        emp_id += 1
        emp[serial_no] = {
            'emp_id' : emp_id ,
            'name' : input("Enter employee name : "),
            'age' : int(input('age : ')),
            'gender': input('gender : '),
            'salary' : int(input('salary : ')),
            'previous_company' : input('enter previous company name : '),
            'joining_date' : input("Joining date : ")
        }
        print('Employee added successful')

def delete_employee():
    serial_no = int(input('Enter serial number: '))
    if serial_no not in emp.keys():
        print('please provide right serial number')
    else:
        del emp[serial_no]

def search_employee():
        name = input('Enter employee name for search : ')
        Flag = False
        for i in emp.values():
            if i['name'] == name:
                Flag = True
                print(f' { i["emp_id"] }| { i["name"]} | {i["age"]} | {i["gender"]} | {i["salary"]} | {i["previous_company"]}  | {i["joining_date"]} ')
        if Flag == False:
            print('employee not found')

def change_employee_data():
        serial_no = int(input('Enter serial number : '))
        if serial_no not in emp.keys():
            print('please provide right serial number !')
        else:
            print('modify employee data')
            print('a,A =>change employee name \nb,B => modify gender \nc,C => modify age \nd,D => modify salary ')
            choice  = input('Enter option: ')
            if choice == 'a' or choice == 'A':
                emp[serial_no]['name'] = input('Enter new name : ')
            elif choice == 'b' or choice == 'B':
                emp[serial_no]['gender'] = input('new Gender :')
            elif choice == 'c' or choice == 'C':
                emp[serial_no]['age'] = int(input('enter new age : '))
            elif choice == 'd' or choice == 'D' :
                emp[serial_no]['salary'] = int(input('enter updated salary : '))
            else:
                print('Invalid option ')

def display_data():
        print('Displaying all employees data')
        for i,v in emp.items():
            print(f' { i }| { v["name"]} | {v["age"]} | {v["gender"]} | {v["salary"]} | {v["previous_company"]}  | {v["joining_date"]} ')   

while True:
    main_menu()
    ch = int(input('Enter choice : '))

    if ch == 1 : 
        #add employee data
        add_employee()
        
    elif ch == 2:
        #delete employee
        delete_employee()
        
    elif ch == 3:
        #search employee
        search_employee()

    elif ch == 4:
        #change employee data
        change_employee_data()
    elif ch == 5:
        #display data
        display_data()
    elif ch == 6 :
        break
    else:
        print('Invalid choice')