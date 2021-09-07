# 2.Draw the graph for "totalnoofapplication" and "districtname" from this data link.
#https://data.gov.in/resources/district-wise-total-msme-registered-service-enterprises-till-last-date/api

import pandas as pd
import json
import requests as req
import matplotlib.pyplot as pl



#Got url from data.gov.in
url = "https://api.data.gov.in/resource/d76a86b1-6a2a-4ab3-9201-cb9f6bc61fa4?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
#Requesting the server using GET type
res = req.request("GET",url)
data = res.json()
data_records = data['records'] #Fetching records key from response

#creating dataframe from json
df = pd.DataFrame(data_records)

#plot the graph
df.plot(kind = "scatter", x = "totalnoofapplication", y = "districtname" , xlabel="totalnoofapplication", ylabel="districtname")
pl.show()
