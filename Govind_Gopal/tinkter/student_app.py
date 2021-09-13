from std_cl import Students
import tkinter as tk

win = tk.Tk()
win.title("Students App")
win.geometry("600x400")
leftfr = tk.Frame(win)
leftfr.grid(row = 0,column = 0)

name = tk.StringVar(leftfr)
age = tk.IntVar(leftfr)
st_class = tk.StringVar(leftfr)

def get_data():
	print (name.get())
	print (age.get())
	print (st_class.get())

rightfr = tk.Frame(win)
rightfr.grid(row = 0, column = 1)

tk.Label(leftfr,text="Name").grid(row = 0, column = 0)
tk.Entry(leftfr,textvariable = name).grid(row = 0, column = 1)

tk.Label(leftfr,text = "Age").grid(row = 1, column = 0)
tk.Entry(leftfr,textvariable = age).grid(row = 1, column = 1)

tk.Label(leftfr,text = "Class").grid(row=2,column = 0)
tk.Entry(leftfr,textvariable = st_class).grid(row = 2,column = 1)

tk.Button(leftfr,text = "Submit",command = get_data).grid(row = 3, column = 0)


win.mainloop()
