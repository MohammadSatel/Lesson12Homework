import requests
from bs4 import BeautifulSoup
import os
import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('weather_scraping.log')
file_handler.setLevel(logging.DEBUG)  
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def clean_screen():
    os.system('cls')
      
def scrape_weather_description(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        description_element = soup.find('p', {'data-testid': 'wxPhrase', 'class': 'DailyContent--narrative--3Ti6_'})
        
        if description_element:
            description = description_element.text.strip()
            logger.info("Weather description scraped. %s")
            return f"Weather Description: {description}"
        else:
            logger.warning("Weather description not found on the page. %s")
            return "Weather description not found on the page."
    else:
        logger.error("Failed to fetch data. %s")
        return "Failed to fetch data."

if __name__ == "__main__":
    clean_screen()
    weather_url = "https://weather.com/weather/tenday/l/96f2f84af9a5f5d452eb0574d4e4d8a840c71b05e22264ebdc0056433a642c84"
    description_data = scrape_weather_description(weather_url)
    print(description_data)
