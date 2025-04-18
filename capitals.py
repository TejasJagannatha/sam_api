from fastapi import FastAPI
from pydantic import BaseModel
import requests, random

app= FastAPI()

country_capitals= {}

class Country(BaseModel):
    capital:str

@app.get('/randomcountry')
def get_country():
    global country_capitals
    results = requests.get("https://countriesnow.space/api/v0.1/countries/capital").json()
    result_list = results["data"]
    countries_list = [i['name'] for i in result_list]
    capitals_list= [i['capital'] for i in result_list]
    random_country= random.choice(countries_list)
    random_country_details=[each for each in result_list if each['name'] == random_country][0]
    country_capitals= random_country_details
    #print(country_capitals)
    return random_country

@app.post('/country')
def main(country: Country):
    #print(random_country)
    #print(country_capitals)
    country_capital= country_capitals['capital'].lower().strip()
    guessed_capital= country.capital.lower().strip()
    #print(country_capital)
    if country_capital == guessed_capital:
        return f"The Guess is correct"
    else:
        return f"The Guess is Incorrect, correct capital: {country_capital}"


