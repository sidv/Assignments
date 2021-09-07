import tkinter as tk
from emp import Employee

employee=[]
win =tk.Tk() #for window 
win.title("Employee Data")
win.geometry("600x400")	

lframe=tk.Frame(win)
lframe.grid(row=0,column=0)

rframe=tk.Frame(win)
rframe.grid(row=0,column=1)

tempid=tk.IntVar(lframe)
tname=tk.StringVar(lframe)
tage=tk.IntVar(lframe)
tgender=tk.StringVar(lframe)
tsalary=tk.IntVar(lframe)
tplace=tk.StringVar(lframe)
tdate=tk.StringVar(lframe)
tpcompany=tk.StringVar(lframe)
msgfield=tk.StringVar(lframe)

def store_data():
	employee.append(Employee(tempid,tname.get(),tage.get(),tgender.get(),tsalary.get(),tplace.get(),tdate.get(),tpcompany.get()))
	emp_id.delete(0,'end')
	e_name.delete(0,'end')
	e_age.delete(0,'end')
	e_gender.delete(0,'end')
	e_salary.delete(0,'end')
	e_place.delete(0,'end')
	e_join.delete(0,'end')
	e_pcompany.delete(0,'end')
	msgfield.set("Employee Added")

def display():
	for i in employee:
		lst.insert(tk.END,i.emp_name)

tk.Label(lframe,text="Employee id").grid(row=0,column=0)
emp_id = tk.Entry(lframe,textvariable=tempid)
emp_id.grid(row=0,column=1)

tk.Label(lframe,text="Employee Name").grid(row=1,column=0)
e_name = tk.Entry(lframe,textvariable=tname)
e_name.grid(row=1,column=1)

tk.Label(lframe,text="Employee Age ").grid(row=2,column=0)
e_age = tk.Entry(lframe,textvariable=tage)
e_age.grid(row=2,column=1)

tk.Label(lframe,text="Gender").grid(row=3,column=0)
e_gender = tk.Entry(lframe,textvariable=tgender)
e_gender.grid(row=3,column=1)

tk.Label(lframe,text="Salary").grid(row=4,column=0)
e_salary = tk.Entry(lframe,textvariable=tsalary)
e_salary.grid(row=4,column=1)

tk.Label(lframe,text="place").grid(row=5,column=0)
e_place = tk.Entry(lframe,textvariable=tplace)
e_place.grid(row=5,column=1)

tk.Label(lframe,text="Join Date").grid(row=6,column=0)
e_join = tk.Entry(lframe,textvariable=tdate)
e_join.grid(row=6,column=1)


tk.Label(lframe,text="Previous Company").grid(row=7,column=0)
e_pcompany = tk.Entry(lframe,textvariable=tpcompany)
e_pcompany.grid(row=7,column=1)


tk.Button(lframe,text="SUBMIT",command = store_data).grid(row=10,column=1)
tk.Button(lframe,text="DISPLAY",command = display ).grid(row=12,column=1)

msgbox= tk.Label(lframe,textvariable=msgfield)
msgbox.grid(row=22,column=1)

lst=tk.Listbox(rframe)
lst.grid(row=0,column=2)


#date
#pcompany
win.mainloop()
