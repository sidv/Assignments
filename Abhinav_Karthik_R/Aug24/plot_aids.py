import pandas as pd 
import matplotlib.pyplot as pl

df=pd.read_csv("aids.csv")
death = pd.DataFrame(df.loc[:,["Year","Data.AIDS-Related Deaths.All Ages"]])
death.plot(kind="scatter", x = "Year", y = "Data.AIDS-Related Deaths.All Ages" , xlabel="Year", ylabel="Death_Rate")

pl.show()