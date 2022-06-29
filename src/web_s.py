import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

f = requests.get("https://www.nike.com/fr/w/hommes-chaussures-nik1zy7ok")
soup = BeautifulSoup(f.text, 'html.parser')

models = []
descriptions = []
prices = []

for div_model in soup.findAll("div", {"class": "product-card__title"}):
    models.append(div_model.text)

for div_description in soup.findAll("div", {"class": "product-card__subtitle"}):
    descriptions.append(div_description.text)

for div_price in soup.findAll("div", {"class": "product-price css-11s12ax is--current-price"}):
    prices.append(div_price.text)

finaldf = pd.DataFrame(
    {'Models': models,
     'Descriptions': descriptions,
     'Prices': prices
     })

print(tabulate(finaldf, headers='keys', tablefmt='psql'))
