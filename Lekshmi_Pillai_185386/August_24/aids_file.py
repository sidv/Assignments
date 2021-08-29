import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pl

df=pd.read_csv("aids.csv") #Reading csv file. Pass the path to csv file

death_df = pd.DataFrame(df.loc[:,["Year","Data.AIDS-Related Deaths.All Ages"]])

death_df.plot(kind="scatter", x = "Year", y = "Data.AIDS-Related Deaths.All Ages" , xlabel="Year", ylabel="Death_Rate")

pl.show() #Show the graph
