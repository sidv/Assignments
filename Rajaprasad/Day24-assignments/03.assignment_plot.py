import pandas as pd
import matplotlib.pyplot as plt
import requests

URL = 'https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10'

res = requests.request('GET', URL)
data = res.json()
data_record = data['records']

df = pd.DataFrame(data_record)
# print(df.info())
df = df.loc[:, ['clusterno', 'clustername', 'centroid']]
print(df)
