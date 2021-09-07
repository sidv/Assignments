import tkinter as tk
from emp import Employee

employee = []

win = tk.Tk()
win.title("Employee")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=1)

eid = tk.IntVar(left_fr)
name = tk.StringVar(left_fr)
age = tk.IntVar(left_fr)
gender = tk.StringVar(left_fr)
sal = tk.StringVar(left_fr)
place = tk.StringVar(left_fr)
date = tk.StringVar(left_fr)
company = tk.StringVar(left_fr)
msg = tk.StringVar(left_fr)
def store_data():
	employee.append(Employee(eid.get(),name.get(),age.get(),gender.get(),sal.get(),place.get(),date.get(),company.get()))
	eid.set(0)
	name.delete(0,'end')
	age.set(0)
	gender.delete(0,'end')
	sal.delete(0,'end')
	place.delete(0,'end')
	date.delete(0,'end')
	cmpny.delete(0,'end')
	msg.set("Employee Added")
	

def display():
	for i in employee:
		lst.insert(tk.END,i.name)

tk.Label(left_fr,text = "Employee ID").grid(row=0,column=0)
id1 = tk.Entry(left_fr,textvariable=eid)
id1.grid(row=0,column=1)

tk.Label(left_fr,text = "Name").grid(row=1,column=0)
name = tk.Entry(left_fr,textvariable=name)
name.grid(row=1,column=1)

tk.Label(left_fr,text = "Age").grid(row=2,column=0)
emp_age = tk.Entry(left_fr,textvariable=age)
emp_age.grid(row=2,column=1)

tk.Label(left_fr,text ="Gender").grid(row=3,column=0)
gender = tk.Entry(left_fr,textvariable=gender)
gender.grid(row=3,column=1)

tk.Label(left_fr,text = "Salary").grid(row=4,column=0)
sal = tk.Entry(left_fr,textvariable=sal)
sal.grid(row=4,column=1)

tk.Label(left_fr,text = "Place").grid(row=5,column=0)
place = tk.Entry(left_fr,textvariable=place)
place.grid(row=5,column=1)

tk.Label(left_fr,text = "Joining Date").grid(row=6,column=0)
date = tk.Entry(left_fr,textvariable=date)
date.grid(row=6,column=1)

tk.Label(left_fr,text = "Previous Company").grid(row=7,column=0)
cmpny = tk.Entry(left_fr,textvariable=company)
cmpny.grid(row=7,column=1)

tk.Button(left_fr,text="Submit",command = store_data).grid(row=12,column=0)
tk.Button(left_fr,text="Display",command = display).grid(row=12,column=1)

msg1 = tk.Label(right_fr,textvariable=msg)
msg1.grid(row=22,column=1)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

win.mainloop()
