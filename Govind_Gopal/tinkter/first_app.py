import tkinter

#def get_name(content):
#	print(content.widget.get())

win = tkinter.Tk() #creating window
win.title("First app") #creating window title


tkname = tkinter.StringVar(win) #creating variable, a string inside win
tkage = tkinter.IntVar(win) #similarly two int variables 
tksal = tkinter.IntVar(win)
tktxt = tkinter.StringVar(win)

def get_data(): #to print to terminal
	print (tkname.get())
	print (tkage.get())
	print (tksal.get())
	txt.insert(tkinter.END,tkname.get()) #inserting values of the variables and inserting the m in the txt variable to be ptinted on scren
	txt.insert(tkinter.END,tkage.get())
	txt.insert(tkinter.END,tksal.get())

tkinter.Label(win, text = "Name :").grid(row = 0, column =0)
tkinter.Entry(win, textvariable=tkname).grid(row = 0,column = 1)


tkinter.Label(win, text = "Age :").grid(row = 1, column =0)
tkinter.Entry(win,textvariable=tkage).grid(row = 1,column = 1)

tkinter.Label(win, text = "Salary :").grid(row = 2, column =0)
tkinter.Entry(win,textvariable=tksal).grid(row = 2,column = 1)

txt = tkinter.Text(win,width = 40, height = 10)
txt.grid(row = 4, column = 1)

tkinter.Button(win,text="Submit",command = get_data).grid(row = 3,column = 1)

win.mainloop() #running window
