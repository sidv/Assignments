emp_info = {}
sl_no = int(input("Enter employee details to dictionary:"))
e_name = input("Enter employee name")
e_age = input("Enter employee age")
e_sex = input("Enter employee gender")
e_place = input("Enter employee place")
e_sal = input("Enter employee salary")
e_comp = input("Enter employee previous company") 
temp ={
	"Ename":e_name,
        "Eage":e_age,
        "Esex":e_sex,
        "Eplace":e_place,
        "Esal":e_sal,
	"Ecomp":e_comp
	}
emp_info[sl_no] = temp
print(temp)
