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

name = tk.StringVar(left_fr)
age = tk.IntVar(left_fr)
gender = tk.StringVar(left_fr)
place_ = tk.StringVar(left_fr)
salary = tk.IntVar(left_fr)
previous_company = tk.StringVar(left_fr)
joining_date = tk.StringVar(left_fr)
msg = tk.StringVar(left_fr)


def store_data():
    print(gender.get())
    employee.append(Employee(len(employee),name.get(),age.get(),place_.get(),salary.get(),previous_company.get(),joining_date.get()))
    name_entry.delete(0,'end')
    age_entry.delete(0,'end')
    place_entry.delete(0,'end') 
    salary_entry.delete(0,'end') 
    previous_company_entry.delete(0,'end') 
    joining_date_entry.delete(0,'end') 
    msg.set("employee details Stored")


def display():
    for i in employee:
        lst.insert(tk.END,i.name)


tk.Label( text="Name" ).place(x=20,y=60)
name_entry = tk.Entry(textvariable=name)
name_entry.place(x=110,y=60)

tk.Label( text="age" ).place(x=20,y=90)
age_entry = tk.Entry(textvariable=age)
age_entry.place(x=110,y=90)

tk.Label( text="gender" ).place(x=20,y=120)
tk.Radiobutton(text="Male",variable=gender,value="male").place(x=110,y=120)
tk.Radiobutton(text="Female",variable=gender,value="female").place(x=170,y=120)

tk.Label( text="place" ).place(x=20,y=150)
place_entry = tk.Entry(textvariable=place_)
place_entry.place(x=110,y=150)

tk.Label( text="salary" ).place(x=20,y=180)
salary_entry = tk.Entry(textvariable=salary)
salary_entry.place(x=110,y=180)

tk.Label( text="previous company" ).place(x=20,y=210)
previous_company_entry = tk.Entry(textvariable=previous_company)
previous_company_entry.place(x=110,y=210)

tk.Label( text="joining date" ).place(x=20,y=240)
joining_date_entry = tk.Entry(textvariable=joining_date)
joining_date_entry.place(x=110,y=240)

tk.Button(text="Submit",command = store_data).place(x=50,y=265)
tk.Button(text="Display",command = display).place(x=150,y=265)


msg_box = tk.Label(textvariable=msg)
msg_box.place(x=150,y=290)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

win.mainloop()