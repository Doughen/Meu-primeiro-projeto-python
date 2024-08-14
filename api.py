#importando as bibliotecas

import requests
import pandas as pd

#criando uma função de usuários

def api_usuarios(api_url):


    
    response = requests.get(api_url)
    response.json()
    print("esse é o print do json")
    print(response.json())
    data = response.json()
    df = pd.DataFrame(data)
    print("esse é o print do dataframe")
    print(df)

#chamando a função da api

api_usuarios("https://fakestoreapi.com/users/5")
api_usuarios("https://jsonplaceholder.typicode.com/users/1")