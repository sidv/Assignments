##Write a program to plot graph on "Year"(x axis) and "Data.AIDS-Related Deaths.All Ages"(y axis) from aids.csv


import pandas as pd #Importing pandas
import numpy as np #Importing numpy
import matplotlib.pyplot as pl #Importing matplolib to draw graph

df=pd.read_csv("aids.csv") #Reading csv file. Pass the path to csv file
new_df = pd.DataFrame(df.loc[:,["Year","Data.AIDS-Related Deaths.All Ages"]])
new_df.plot( kind="scatter",x="Year", y="Data.AIDS-Related Deaths.All Ages" ,xlabel="Year" ,ylabel="Data.AIDS-Related Deaths.All Ages") 

pl.show()



