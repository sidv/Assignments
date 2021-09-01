import tkinter as tk
from employee import Employee

employee = []

#window Creation
win = tk.Tk()
win.title("ERP Project")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=1)

#creating variables
t_empid = tk.IntVar(left_fr)
t_name = tk.StringVar(left_fr)
t_age = tk.IntVar(left_fr)
t_gender = tk.StringVar(left_fr)
t_sal = tk.StringVar(left_fr)
t_place = tk.StringVar(left_fr)
t_date = tk.StringVar(left_fr)
t_company = tk.StringVar(left_fr)
msgfield = tk.StringVar(left_fr)
def store_data():
	employee.append(Employee(t_empid,t_name.get(),t_age.get(),t_gender.get(),t_sal.get(),t_place.get(),t_date.get(),t_company.get()))
	emp_id.delete(0,'end')
	emp_name.delete(0,'end')
	emp_age.delete(0,'end')
	emp_gender.delete(0,'end')
	emp_sal.delete(0,'end')
	emp_place.delete(0,'end')
	emp_date.delete(0,'end')
	emp_comp.delete(0,'end')
	#msgfield.delete(0,'end')
	msgfield.set("Data Added Successfully!!")


def display():
	for i in employee:
		lst.insert(tk.END,i.emp_name)

tk.Label(left_fr,text = "Employee ID").grid(row=0,column=0)
emp_id = tk.Entry(left_fr,textvariable=t_empid)
emp_id.grid(row=0,column=1)

tk.Label(left_fr,text = "Name").grid(row=1,column=0)
emp_name = tk.Entry(left_fr,textvariable=t_name)
emp_name.grid(row=1,column=1)

tk.Label(left_fr,text = "Age").grid(row=2,column=0)
emp_age = tk.Entry(left_fr,textvariable=t_age)
emp_age.grid(row=2,column=1)

tk.Label(left_fr,text ="Gender").grid(row=3,column=0)
emp_gender = tk.Entry(left_fr,textvariable=t_gender)
emp_gender.grid(row=3,column=1)

tk.Label(left_fr,text = "Salary").grid(row=4,column=0)
emp_sal = tk.Entry(left_fr,textvariable=t_sal)
emp_sal.grid(row=4,column=1)

tk.Label(left_fr,text = "Place").grid(row=5,column=0)
emp_place = tk.Entry(left_fr,textvariable=t_place)
emp_place.grid(row=5,column=1)

tk.Label(left_fr,text = "Joining Date").grid(row=6,column=0)
emp_date = tk.Entry(left_fr,textvariable=t_date)
emp_date.grid(row=6,column=1)

tk.Label(left_fr,text = "Previous Company").grid(row=7,column=0)
emp_comp = tk.Entry(left_fr,textvariable=t_company)
emp_comp.grid(row=7,column=1)

tk.Button(left_fr,text="Submit",command = store_data).grid(row=11,column=0)
tk.Button(left_fr,text="Display",command = display).grid(row=11,column=1)

msg_box = tk.Label(left_fr,textvariable=msgfield)
msg_box.grid(row=20,column=1)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

win.mainloop()

