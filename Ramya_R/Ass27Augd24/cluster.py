import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Got url from data.gov.in
url = "https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
#Requesting the server using GET type
res = requests.request("GET",url)
data = res.json()
data_records = data['records'] #Fetching records key from response

#creating dataframe from json
df = pd.DataFrame(data_records)
print(df)
print(df.info()) #printing columns and other info

dfl = df.loc[:, ['clusterno', 'clustername', 'centroid']]
print(dfl)

