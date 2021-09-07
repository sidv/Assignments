import json
import requests
import pandas as pd
#import matplotlib.pyplot as plt

df_lst = []
url = "https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"

res = requests.request("GET",url)
data = res.json()
data_rec = data['records']
df_lst.append(pd.DataFrame(data_rec))
df = pd.concat(df_lst)
print(df[['clustername','clusterno','centroid']].to_string())


