#4.Create a GUI app using tkinter and show the data "year_" and "actual_rainfall_in_south_west_monsoon_in_mm_" https://tn.data.gov.in/node/6885468/api

import tkinter as tk
import json
import requests
import pandas as pd

#Got url from data.gov.in
url = "https://api.data.gov.in/resource/6fa7d29e-127a-429b-bc2d-78aa5809a078?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
#Requesting the server using GET type
lst = []
res = requests.request("GET",url)
data = res.json()
lst.append(pd.DataFrame(data['records']))
df = pd.concat(lst)
win = tk.Tk()
win.title("Rainfall details")
txt=tk.Listbox(win,height=60,width=100)
txt.grid(column=0,row=1)
txt.insert(tk.END,"YEAR    |  Rainfall")
for index, row in df.iterrows():
    txt.insert(tk.END,f"{row['year_']} | {row['actual_rainfall_in_south_west_monsoon_in_mm_']}")
win.mainloop()
