#3.Print a dataframe which contain "clustername","clusterno", and "centroid"
import json
import requests
import pandas as pd
dflst = []
url = "https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
res = requests.request("GET",url)
data = res.json()
data_records = data['records']
dflst.append(pd.DataFrame(data['records']))
df = pd.concat(dflst)
print(df[['clustername','clusterno','centroid']].to_string())

