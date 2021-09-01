#program to plot graph on "Location.Country"(x axis) and total of "Data.Cases" and "Data.Deaths"(y axis) from covid csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
df = pd.read_csv("covid.csv")
country_location = df.loc[:,["Location.Country"]]
data_case = pd.DataFrame(df.loc[:,["Data.Cases"]])
data_death = pd.DataFrame(df.loc[:,["Data.Deaths"]])
data_case_arr = data_case.to_numpy()
data_death_arr = data_death.to_numpy()
total_death = np.add(data_case_arr,data_death_arr)
total_df = pd.DataFrame(total_death , columns = ["Total"])
new_df = pd.concat([country_location,total_df],axis=1)
new_df.plot(kind="scatter", x = "Location.Country", y = "Total" , xlabel="Country", ylabel="Total Deaths")
pl.show()
