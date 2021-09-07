import pandas as pd
import requests as r


url = "https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&"
offset = 0
data = []
while(offset < 50):
    result = r.get(url+f"offset={offset}")
    data.append(pd.DataFrame(result.json()['records']))
    offset += 1

df = pd.concat(data)
print(df[['clustername','clusterno','centroid']].to_string())
