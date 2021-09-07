import pandas as pd
import matplotlib.pyplot as pl

aids_df = pd.read_csv("aids.csv")
new_df = aids_df.loc[:,["Year", "Data.AIDS-Related Deaths.All Ages"]]
#print(type(new_df))
new_df.plot(kind = "scatter", x = "Year", y = "Data.AIDS-Related Deaths.All Ages", xlabel = "Year", ylabel = "Data.AIDS-Related Deaths.All Ages")
pl.show()
