from tkinter import *
from employee import Emp

emp = []
root = Tk()
root.geometry("700x500")
root.title("Enterprise resource planning system ")


def store_data():
    # print(gender.get())
    emp.append(Emp(emp_id.get(), fname.get(), lname.get(), age.get(
    ), gender.get(), salary.get(), pre_comp.get(), join_date.get()))

    msg.set("Data stored successfully")


def display():
    for i in emp:
        lst.insert(END, i.fname, i.lname)


lframe = Frame(root)
lframe.place(x=10, y=100)
rframe = Frame(root)
rframe.place(x=400, y=100)

# creating objects
emp_id = StringVar(lframe)
fname = StringVar(lframe)
lname = StringVar(lframe)
age = IntVar(lframe)
gender = StringVar(lframe)
salary = StringVar(lframe)
pre_comp = StringVar(lframe)
join_date = StringVar(lframe)
msg = StringVar(lframe)

Label(root, text="welcome to ERP system ",
      font='consolas 14 bold', padx=20, pady=20).grid(row=0, column=1)

Label(lframe, text='employee id : ').grid(row=1, column=0)
Entry(lframe, textvariable=emp_id).grid(row=1, column=1)

Label(lframe, text='First name : ').grid(row=2, column=0)
Entry(lframe, textvariable=fname).grid(row=2, column=1)

Label(lframe, text='last name : ').grid(row=3, column=0)
Entry(lframe, textvariable=lname).grid(row=3, column=1)

Label(lframe, text='Age : ').grid(row=4, column=0)
Entry(lframe, textvariable=age).grid(row=4, column=1)

Label(lframe, text='Gender : ').grid(row=5, column=0)
# Entry(lframe, textvariable=gender).grid(row=5, column=1)

Radiobutton(lframe, text="Male", variable=gender,
            value="male").grid(row=5, column=1)
Radiobutton(lframe, text="Female", variable=gender,
            value="female").grid(row=5, column=2)
Radiobutton(lframe, text="other", variable=gender,
            value="other").grid(row=5, column=3)


Label(lframe, text='salary : ').grid(row=6, column=0)
Entry(lframe, textvariable=salary).grid(row=6, column=1)

Label(lframe, text='Previous company : ').grid(row=7, column=0)
Entry(lframe, textvariable=pre_comp).grid(row=7, column=1)

Label(lframe, text='joining date : ').grid(row=8, column=0)
Entry(lframe, textvariable=join_date).grid(row=8, column=1)

Button(lframe, text='Submit', command=store_data).grid(row=9, column=0)
Button(lframe, text='Display', command=display).grid(row=9, column=1)

lst = Listbox(rframe, bg='grey', fg='white')
lst.grid(row=1, column=3)

msg_box = Label(lframe, textvariable=msg)
msg_box.grid(row=10, column=0)


root.mainloop()
