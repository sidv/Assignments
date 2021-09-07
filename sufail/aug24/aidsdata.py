import pandas as pd
import matplotlib.pyplot as p1

df=pd.read_csv("aids.csv")
ndf=pd.DataFrame(df.loc[:,["Year","Data.AIDS-Related Deaths.All Ages"]])
ndf.plot(kind="scatter",x="Year",y="Data.AIDS-Related Deaths.All Ages" ,xlabel="YEAR" ,ylabel="Death Rate")
p1.show()
