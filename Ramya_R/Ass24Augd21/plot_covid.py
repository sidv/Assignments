import pandas as pd #Importing pandas
import numpy as np #Importing numpy
import matplotlib.pyplot as pl #Importing matplolib to draw graph

df=pd.read_csv("covid.csv") #Reading csv file. Pass the path to csv file

cases_df = pd.DataFrame(df.loc[:,["Data.Cases"]])
deaths_df = pd.DataFrame(df.loc[:,["Data.Deaths"]])

cases_arr = cases_df.to_numpy()   #Convert to numpy array
deaths_arr = deaths_df.to_numpy() #Conevrt to numpy array

total_arr = np.add(cases_arr ,deaths_arr) #Adding two numpy array

total_df = pd.DataFrame(total_arr, columns = ["Total_deaths"])
#print(total_arr)
#print(total_df)
country_df = df.loc[:,["Location.Country"]]

new_df = pd.concat( [country_df , total_df] ,axis=1) #Concat two dataframes Pass all dataframes as elements of list in correct order

new_df.plot(kind="scatter", x = "Location.Country", y = "Total_deaths" , xlabel="Location.Country", ylabel="Total Deaths")

pl.show() #Show the graph

