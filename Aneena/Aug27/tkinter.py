import json
import requests
import pandas as pd
clustername_loop = []
clusterno_loop = []
centroid_loop = []
#url in data.gov.in
url = "https://api.data.gov.in/resource/ee35f072-4d80-4b41-8c17-fd74414907be?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=10"
#GET -request to server
res = requests.request("GET",url)
data = res.json()
for i in data['records']:
        clustername_loop.append(i["clustername"])
        clusterno_loop.append(i["clusterno"])
        centroid_loop.append(i["centroid"])
#create dataframe from json
df_clustername = pd.DataFrame(clustername_loop,columns = ["clustername"])
df_clusterno = pd.DataFrame(clusterno_loop,columns = ["clusterno"])
df_centroid = pd.DataFrame(centroid_loop,columns = ["centroid"])
new_df = pd.concat( [df_clustername , df_clusterno , df_centroid],axis = 1)
print(new_df)


