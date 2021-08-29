#Write a program to plot graph on "Year"(x axis) and "Data.AIDS-Related #Deaths.All Ages"(y axis) from aids.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

df = pd.read_csv("aids.csv") #reading from csv file
deaths = pd.DataFrame(df.loc[:,["Year","Data.AIDS-Related Deaths.All Ages"]])
deaths.plot(kind="scatter", x = "Year", y = "Data.AIDS-Related Deaths.All Ages" , xlabel="year", ylabel="Data.AIDS-Related Deaths.All Ages")
pl.show() 


