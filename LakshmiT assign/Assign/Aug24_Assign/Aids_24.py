
#3.Write a program to plot graph on "Year"(x axis) and "Data.AIDS-Related Deaths.All Ages"(y axis) from aids.csv

import pandas as pd 
import matplotlib.pyplot as pl
x = []
y = []
  
with open('aids.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[2])
        y.append((row[3]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Aids datas")
  
plt.xticks(rotation = 75)
plt.xlabel('Year')
plt.ylabel('Data.AIDS-Related Deaths.All Ages')
plt.title('Death_Rate', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


