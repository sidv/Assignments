import json
import pandas as pd
import requests

URL = 'https://data.gov.in/resources/district-wise-total-msme-registered-service-enterprises-till-last-date/api'

res = requests.request("GET", URL)

data = res.json()

print(data)
