import tkinter as tk
import pandas as pd
import requests as r

def req_data():
    url = "https://api.data.gov.in/resource/6fa7d29e-127a-429b-bc2d-78aa5809a078?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&"
    offset = 0
    data = []
    while(offset < 10):
        result = r.get(url+f"offset={offset}")
        data.append(pd.DataFrame(result.json()['records']))
        offset += 1

    df = pd.concat(data)
    return df

def gui():
    win = tk.Tk()
    win.title("Rainfall Data")
    lst=tk.Listbox(win,height=50,width=40)
    lst.grid(column=0,row=1)
    
    def display():
        df = req_data()
        lst.insert(tk.END,"year                     Rainfall in mm")
        for index, row in df.iterrows():
            lst.insert(tk.END,f"{row['year_']:30} {row['actual_rainfall_in_south_west_monsoon_in_mm_']}")
    
    tk.Button(win,text="Display",command = display).grid(row=2,column=0)
    
    win.mainloop()

gui()