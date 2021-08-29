#4.Write a program to plot graph on "Location.Country"(x axis) and total of "Data.Cases" and "Data.Deaths"(y axis) from covid csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

df = pd.read_csv("covid.csv")
plt.xticks(total_states, df['Location.Countary'],rotation=90)  
plt.ylim(1,max(df['Cases'])+10) 
plt.ylabel('Data.Cases')  
plt.title('Total_Cases')  
plt.show()

figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.bar(total_states,df['Data.cases'], align='center', alpha=0.5,  
                 color=("blue"),  
                 edgecolor=(0.5,0.4,0.8)  )
    
plt.xticks(total_states, df['Location.Countary'],rotation=90)  
plt.ylim(1,max(df['Deaths'])+10) 
plt.ylabel('Data.Deaths')  
plt.title('Total_death_Cases')  
plt.show()

df.plot.barh(stacked=True,figsize=(10,10))
df1=df.iloc[:,1:3]
df1.plot.barh(color={"Data.Cases": "red", "Data.Death": "green"},figsize=(10,10))
