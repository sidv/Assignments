import tkinter as tk
from emp_tkinter_class import Employee

employees = []

win = tk.Tk() #Creating window
win.title("Employee app") #Setting up the title
win.geometry("800x800")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=1)

#Creating Object
name = tk.StringVar(left_fr)
age = tk.IntVar(left_fr)
gender = tk.StringVar(left_fr)
place = tk.StringVar(left_fr)
salary = tk.StringVar(left_fr)
prev_company = tk.StringVar(left_fr)
join_date = tk.StringVar(left_fr)
msg = tk.StringVar(left_fr)
#Create function
def store_data():
	employees.append(Employee(len(employees),name.get(),age.get(),gender.get(),place.get(),salary.get(),prev_company.get(),join_date.get()))
	name_entry.delete(0,'end')
	age_entry.delete(0,'end')
	gender.delete(0,'end')
	place_entry.delete(0,'end')
	salary_entry.delete(0,'end')
	prev_company_entry.delete(0,'end')
	join_date_entry.delete(0,'end')
	msg.set("Data Stored")
def display():
	for i in employees:
		lst.insert(tk.END,i.name)
tk.Label(left_fr, text="Name" ).grid(row=0, column=0)
name_entry = tk.Entry(left_fr,textvariable=name)
name_entry.grid(row=0,column=1)

tk.Label(left_fr, text="Age" ).grid(row=1, column=0)
age_entry = tk.Entry(left_fr,textvariable=age)
age_entry.grid(row=1,column=1)

#tk.Label(left_fr, text="Gender" ).grid(row=2, column=0)
#gender_entry = tk.Entry(left_fr,textvariable=gender)
#gender_entry.grid(row=2,column=1)

tk.Radiobutton(left_fr,text="Male",variable=gender,value="male").grid(row=2,column=0)
tk.Radiobutton(left_fr,text="Female",variable=gender,value="female").grid(row=2,column=1)


tk.Label(left_fr, text="Place" ).grid(row=3, column=0)
place_entry = tk.Entry(left_fr,textvariable=place)
place_entry.grid(row=3,column=1)

tk.Label(left_fr, text="Salary" ).grid(row=4, column=0)
salary_entry = tk.Entry(left_fr,textvariable=salary)
salary_entry.grid(row=4,column=1)

tk.Label(left_fr, text="prev_company" ).grid(row=5, column=0)
prev_company_entry = tk.Entry(left_fr,textvariable=prev_company)
prev_company_entry.grid(row=5,column=1)

tk.Label(left_fr, text="join_date" ).grid(row=6, column=0)
join_date_entry = tk.Entry(left_fr,textvariable=join_date)
join_date_entry.grid(row=6,column=1)


tk.Button(left_fr,text="Submit",command = store_data).grid(row=8,column=0)
tk.Button(left_fr,text="Display",command = display).grid(row=8,column=1)

#msg_box = tk.Text(left_fr,height=1,width=15)
#msg_box.grid(row=10,column=0)
msg_box = tk.Label(left_fr,textvariable=msg)
msg_box.grid(row=10,column=0)

lst=tk.Listbox(right_fr)
lst.grid(row=0,column=1)

win.mainloop()
