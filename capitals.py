from fastapi import FastAPI
from pydantic import BaseModel
import requests, random

app= FastAPI()

country_capitals= {}

class Country(BaseModel):
    name:str

@app.get('/randomcountry')
def get_country():
    results = requests.get("https://countriesnow.space/api/v0.1/countries/capital").json()
    result_list = results["data"]
    countries_list = [i['name'] for i in result_list]
    capitals_list= [i['capital'] for i in result_list]
    random_country= random.choice(countries_list)
    c=[each for each in result_list if each['name'] == random_country][0]
    print(result_list)
    return random_country

@app.post('/country')
def main(country: Country):

    return f"hello {country.name}"


