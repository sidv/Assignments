import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
totalnoofapplication_loop = []
districtname_loop = []
#data.gov.in
url = "https://api.data.gov.in/resource/d76a86b1-6a2a-4ab3-9201-cb9f6bc61fa4?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=10&limit=10"
res = requests.request("GET",url)
data = res.json()
totalnoofapplication = data['records']
for i in data['records']:
	totalnoofapplication_loop.append(i["totalnoofapplication"])
	districtname_loop.append(i["districtname"])
#district_name = data['districtname'] #Fetching records key from response
print(totalnoofapplication_loop)
#create dataframe from json
df_total = pd.DataFrame(totalnoofapplication_loop,columns = ["Total_Application"])
df_district = pd.DataFrame(districtname_loop,columns = ["District_Name"])
new_df = pd.concat( [df_district , df_total] ,axis=1)
print(df_total.info()) #printing columns and other info
#Graph
new_df.plot(kind = "scatter", x = "Total_Application", y = "District_Name" , xlabel="total_no_of_application", ylabel="District Name")
plt.show()

