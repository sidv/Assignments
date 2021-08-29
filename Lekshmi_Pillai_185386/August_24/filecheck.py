import pandas as pd
import numpy as np 
import matplotlib.pyplot as pl

df=pd.read_csv("covid.csv") #Reading csv file. Pass the path to csv file

datacase_df = pd.DataFrame(df.loc[:,["Data.Cases"]])
death_df = pd.DataFrame(df.loc[:,["Data.Deaths"]])

datacase_arr = datacase_df.to_numpy()
death_arr = death_df.to_numpy() 

total_arr = np.add(datacase_arr ,death_arr) #Adding two numpy array

total_df = pd.DataFrame(total_arr, columns = ["Total_deaths"])

country_df = df.loc[:,["Location.Country"]]

new_df = pd.concat( [country_df , total_df] ,axis=1) #Concat two dataframes Pass all dataframes as elements of list in correct order

new_df.plot(kind="scatter", x = "Location.Country", y = "Total_deaths" , xlabel="Location.Country", ylabel="Total Deaths")

pl.show() #Show the graph
