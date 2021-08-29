#1.Create a GUI interface for the ERP project(take input from user and show Name in list)

import tkinter as tk
from employee_class import Employee

employee = []

win = tk.Tk() 
win.title("ERP app") 
win.geometry("600x400")


left_fr = tk.Frame(win)
left_fr.place(x=10,y=10)

right_fr = tk.Frame(win)
right_fr.place(x=300,y=100)

emply_id = tk.IntVar(left_fr)
emply_name = tk.StringVar(left_fr)
age = tk.IntVar(left_fr)
gender = tk.StringVar(left_fr)
place = tk.StringVar(left_fr)
sal = tk.IntVar(left_fr)
previous_company = tk.StringVar(left_fr)
joining_date = tk.StringVar(left_fr)
msg = tk.StringVar(left_fr)


def store_data():
    
    employee.append(Employee(len(employee),name.get(),age.get(),place_.get(),salary.get(),previous_company.get(),joining_date.get()))
    emply_id_entry.delete(0,'end')
    emply_name_entry.delete(0,'end')
    age_entry.delete(0,'end')
    place_entry.delete(0,'end') 
    sal_entry.delete(0,'end') 
    previous_company_entry.delete(0,'end') 
    joining_date_entry.delete(0,'end') 
    msg.set("employee details added sucessfully!")


def display():
    for i in employee:
        lst.insert(tk.END,i.emply_name)
tk.Label(left_fr,text = "Employee ID").grid(row=0,column=0)
emply_id = tk.Entry(left_fr,textvariable=t_empid)
emply_id.grid(row=0,column=1)

tk.Label(left_fr,text = "Name").grid(row=1,column=0)
emply_name = tk.Entry(left_fr,textvariable=t_name)
emply_name.grid(row=1,column=1)

tk.Label(left_fr,text = "Age").grid(row=2,column=0)
age = tk.Entry(left_fr,textvariable=t_age)
age.grid(row=2,column=1)

tk.Label(left_fr,text ="Gender").grid(row=3,column=0)
gender = tk.Entry(left_fr,textvariable=t_gender)
gender.grid(row=3,column=1)

tk.Label(left_fr,text = "Salary").grid(row=4,column=0)
sal = tk.Entry(left_fr,textvariable=t_sal)
sal.grid(row=4,column=1)

tk.Label(left_fr,text = "Place").grid(row=5,column=0)
place = tk.Entry(left_fr,textvariable=t_place)
place.grid(row=5,column=1)

tk.Label(left_fr,text = "Joining Date").grid(row=6,column=0)
date = tk.Entry(left_fr,textvariable=t_date)
date.grid(row=6,column=1)

tk.Label(left_fr,text = "Previous Company").grid(row=7,column=0)
comp = tk.Entry(left_fr,textvariable=t_company)
comp.grid(row=7,column=1)

tk.Button(left_fr,text="Submit",command = store_data).grid(row=11,column=0)
tk.Button(left_fr,text="Display",command = display).grid(row=11,column=1)

msg = tk.Label(left_fr,textvariable=msgfield)
msg.grid(row=20,column=1)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

win.mainloop()
