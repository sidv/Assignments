import pandas as pd
import numpy as np
import matplotlib.pyplot as pl


df = pd.read_csv("covid.csv")
datacase = pd.DataFrame(df.loc[:, ["Data.Cases"]])
death = pd.DataFrame(df.loc[:, ["Data.Deaths"]])
total_arr = np.add(datacase.to_numpy(), death.to_numpy())
total = pd.DataFrame(total_arr, columns=["Total_deaths"])
cntry = df.loc[:, ["Location.Country"]]
data = pd.concat([cntry, total], axis=1)
data.plot(kind="scatter", x="Location.Country", y="Total_deaths",
            xlabel="Location.Country", ylabel="Total Deaths")

pl.show()
