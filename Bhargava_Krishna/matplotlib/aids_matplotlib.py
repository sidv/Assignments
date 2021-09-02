import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv("aids.csv")
df = pd.DataFrame(d.loc[:,["Year", "Data.AIDS-Related Deaths.All Ages"]])

print(df)

df.plot(kind = "scatter", x = "Year", y = "Data.AIDS-Related Deaths.All Ages", xlabel = "Year", ylabel = "Deaths")

plt.show()
