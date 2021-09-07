#2.Draw the graph for "totalnoofapplication" and "districtname" from this data link.
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "https://api.data.gov.in/resource/d76a86b1-6a2a-4ab3-9201-cb9f6bc61fa4?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"


res = requests.request("GET",url)
data = res.json()
data_records = data['records']
df = pd.DataFrame(data_records)
df.plot(kind = "scatter", x = "totalnoofapplication", y = "districtname" , xlabel="totalnoofapplication", ylabel="districtname")
plt.show()



