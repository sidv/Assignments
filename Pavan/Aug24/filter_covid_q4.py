import pandas as pd
import matplotlib.pyplot as pl

covid_df = pd.read_csv("covid.csv")
new_df = covid_df.loc[:, ["Location.Country", "Data.Cases", "Data.Deaths"]]
new_df["Total cases & deaths"] = new_df["Data.Cases"] + new_df["Data.Deaths"]
new_df = new_df.loc[:, ["Location.Country", "Total cases & deaths"]]

new_df.plot(kind = "scatter", x = "Location.Country", y = "Total cases & deaths", xlabel = "Location.Country", ylabel = "Total cases & deaths")
pl.show()
#print(new_df)
