#4.Create a GUI app using tkinter and show the data "year_" and "actual_rainfall_in_south_west_monsoon_in_mm_" https://tn.data.gov.in/node/6885468/api


import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Got url from data.gov.in
url = "https://api.data.gov.in/resource/6fa7d29e-127a-429b-bc2d-78aa5809a078?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
#Requesting the server using GET type
res = requests.request("GET",url)
data = res.json()
data_records = data['records'] #Fetching records key from response

#creating dataframe from json
df = pd.DataFrame(data_records)
print(df)
print(df.info()) #printing columns and other info

#plot the graph
df.plot(kind = "scatter", x = "year_", y = "actual_rainfall_in_south_west_monsoon_in_mm_" , xlabel="year_", ylabel="actual_rainfall_in_south_west_monsoon_in_mm_")
plt.show()

