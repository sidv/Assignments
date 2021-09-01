#4.Create a GUI app using tkinter and show the data "year_" and "actual_rainfall_in_south_west_monsoon_in_mm_"
#https://tn.data.gov.in/node/6885468/api
import tkinter as tk
import pandas as pd
import requests 
url = "https://api.data.gov.in/resource/6fa7d29e-127a-429b-bc2d-78aa5809a078?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&"
dflst = []
res = requests.request("GET",url)
data = res.json()
dflst.append(pd.DataFrame(data['records']))
df = pd.concat(dflst)
win = tk.Tk()
win.title("Rainfall details")
lst_box=tk.Listbox(win,height=50,width=40)
lst_box.grid(column=0,row=1)
lst_box.insert(tk.END,"YEAR|Rainfall in Southwest monsoon in mm")
for index, row in df.iterrows():
    lst_box.insert(tk.END,f"{row['year_']:30} | {row['actual_rainfall_in_south_west_monsoon_in_mm_']}")
win.mainloop()
