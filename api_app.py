from enum import Enum
import os
import logging
import requests

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('api_app.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

class Actions(Enum):
    CRYPTO = 1
    CURRENCY = 2
    SPORTS = 3
    WEATHER = 4
    EXIT = 0
    
def menu():
    clean_screen()
    while True:
        for action in Actions:
            print(f'{action.value}:{action.name}')
        user_selection=Actions( int( input("\nSelect API to pull and print: ")))
        if user_selection == Actions.CRYPTO:  print_crypto()
        if user_selection == Actions.CURRENCY:  print_currency()
        if user_selection == Actions.SPORTS:  print_sports()
        if user_selection == Actions.WEATHER:  print_weather()
        if user_selection == Actions.EXIT:  break
    
def print_crypto():
    clean_screen()
    url = "https://coingecko.p.rapidapi.com/simple/price"
    querystring = {"ids":"<REQUIRED>","vs_currencies":"<REQUIRED>"}
    headers = {
        "X-RapidAPI-Key": "a59a079a82mshec781feed8400cep18583bjsn39483d1cd690",
        "X-RapidAPI-Host": "coingecko.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    logger.info("Pulling crypto API %s")

def print_currency():
    clean_screen()
    url = "https://currency-exchange.p.rapidapi.com/listquotes"
    headers = {
        "X-RapidAPI-Key": "a59a079a82mshec781feed8400cep18583bjsn39483d1cd690",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    print(response.json())
    logger.info("Pulling currency API %s")

def print_sports():
    clean_screen()
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
    querystring = {"page":"1"}
    headers = {
        "X-RapidAPI-Key": "a59a079a82mshec781feed8400cep18583bjsn39483d1cd690",
        "X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    logger.info("Pulling sports API %s")

def print_weather(): 
    clean_screen()
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q":"53.1,-0.13"}
    headers = {
        "X-RapidAPI-Key": "a59a079a82mshec781feed8400cep18583bjsn39483d1cd690",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
    logger.info("Pulling weather API %s")

def clean_screen():
    os.system('cls')
    
if __name__ == "__main__":
    menu()
    logger.info("App used %s")

    
