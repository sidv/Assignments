#Create a GUI interface for the ERP project(take input from user and #show Name in list)

import tkinter as tk
from employee_class import Employee

employees = []
def store_data():
	employees.append(Employee(len(employees),name.get(),gender.get(),place.get(),salary.get(),prv_company.get(),joining_date.get()))
	
def display():
	for i in employees:
		lst.insert(tk.END,i.name)
win = tk.Tk()
win.title("Employee app")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=1)

name = tk.StringVar(left_fr) # creating object
gender = tk.StringVar(left_fr)
place = tk.StringVar(left_fr)
salary = tk.IntVar(left_fr)
prv_company = tk.StringVar(left_fr)
joining_date = tk.IntVar(left_fr)

tk.Label(left_fr, text = "Name").grid(row=0,column=0) #creating label
name_entry = tk.Entry(left_fr,textvariable=name)
name_entry.grid(row=0,column=1) #creating textbox

tk.Label(left_fr, text = "Gender").grid(row=1,column=0)
gender_entry = tk.Entry(left_fr,textvariable=gender)
gender_entry.grid(row=1,column=1)

tk.Label(left_fr, text = "Place").grid(row=2,column=0)
place_entry= tk.Entry(left_fr,textvariable=place)
place_entry.grid(row=2,column=1)

tk.Label(left_fr, text = "Salary").grid(row=3,column=0)
salary_entry = tk.Entry(left_fr,textvariable=salary)
salary_entry.grid(row=3,column=1)

tk.Label(left_fr, text = "Previous Company").grid(row=4,column=0)
prv_com=tk.Entry(left_fr,textvariable=prv_company)
prv_com.grid(row=4,column=1)

tk.Label(left_fr, text = "Joining Date").grid(row=5,column=0)
join_date = tk.Entry(left_fr,textvariable=joining_date)
join_date.grid(row=5,column=1)

tk.Button(left_fr,text="Submit",command = store_data).grid(row=6,column=0) #creating submit button
tk.Button(left_fr,text="Display",command = display).grid(row=6,column=1) #creating display button
lst = tk.Listbox(right_fr) #creating listbox on right side
lst.grid(row=0,column=1)


win.mainloop()
