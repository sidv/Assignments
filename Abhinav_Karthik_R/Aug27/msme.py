import pandas as pd
import requests as r
import matplotlib.pyplot as pl


url ="https://api.data.gov.in/resource/d76a86b1-6a2a-4ab3-9201-cb9f6bc61fa4?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&"
offset = 0
data = []
while(offset < 50):
    result = r.get(url+f"offset={offset}")
    data.append(pd.DataFrame(result.json()['records']))
    offset += 1

df = pd.concat(data).drop_duplicates("districtname",keep="last")
print(df)
df.plot(kind = "scatter", x = "totalnoofapplication", y = "districtname" , xlabel="Applications", ylabel="Districts")
pl.show()