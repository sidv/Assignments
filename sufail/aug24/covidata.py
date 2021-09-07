import pandas as pd
import matplotlib.pyplot as pl
import numpy as np

df = pd.read_csv("covid.csv")
case = pd.DataFrame(df.loc[:,["Data.Cases"]])
death = pd.DataFrame(df.loc[:,["Data.Deaths"]])
country=df.loc[:,["Location.Country"]]
case_arr = case.to_numpy()
death_arr = death.to_numpy()
total_death = np.add(case_arr,death_arr)
total_df = pd.DataFrame(total_death , columns = ["Total"])
new_df = pd.concat([country,total_df],axis=1)
new_df.plot(kind="scatter", x = "Location.Country", y = "Total" , xlabel="Country", ylabel="Total Deaths")
pl.show()
