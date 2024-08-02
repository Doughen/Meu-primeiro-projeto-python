import requests
import pandas as pd



api_url = "https://fakestoreapi.com/users/5"
response = requests.get(api_url)
response.json()
print("esse é o print do json")
print(response.json())
data = response.json()
df = pd.DataFrame(data)
print("esse é o print do dataframe")
print(df)