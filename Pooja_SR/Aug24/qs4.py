# 4 Write a program to plot graph on "Location.Country"(x axis) and total of "Data.Cases" and "Data.Deaths"(y axis) from covid csv

import pandas as pd #Importing pandas
import numpy as np #Importing numpy
import matplotlib.pyplot as pl #Importing matplolib to draw graph


df=pd.read_csv("covid.csv") #Reading csv file. Pass the path to csv file

case_df = pd.DataFrame(df.loc[:,["Data.Cases"]])
death_df = pd.DataFrame(df.loc[:,["Data.Deaths"]])

case_arr = case_df.to_numpy()   #Convert to numpy array
death_arr = death_df.to_numpy() #Conevrt to numpy array

total_arr = np.add(case_arr ,death_arr) #Adding two numpy array

total_df = pd.DataFrame(total_arr, columns = ["Total_case&deaths"])

country_df = df.loc[:,["Location.Country"]]

new_df = pd.concat( [country_df , total_df] ,axis=1) 

new_df.plot(kind="scatter", x = "Location.Country", y = "Total_case&deaths" , xlabel="Location.Country", ylabel="Total_case&Deaths")

pl.show() 
