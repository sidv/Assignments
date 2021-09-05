#Create a GUI app using tkinter and show the data "year_" and "actual_rainfall_in_south_west_monsoon_in_mm_"
#https://smartcities.data.gov.in/resources/surat-covid-19-cluster-containment-zone-details/api

import tkinter as tk  
import pandas as pd
import requests

df_list = []
win = tk.Tk()
win.title("Rainfall Data")


url = "https://api.data.gov.in/resource/6fa7d29e-127a-429b-bc2d-78aa5809a078?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
get_req = requests.request("GET",url)
data = get_req.json()
data_records = data['records']
df_list.append(pd.DataFrame(data_records))
df = pd.concat(df_list)
lst = tk.Listbox(win,height=50,width=40)
lst.grid(column=0,row=1)
lst.insert(tk.END,"YEAR | Rainfall in Southwest monsoon in mm")
for index, row in df.iterrows():
    
    lst.insert(tk.END,f"{row['year_']:30} | {row['actual_rainfall_in_south_west_monsoon_in_mm_']}")
win.mainloop()

