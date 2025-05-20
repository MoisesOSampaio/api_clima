import requests
from dotenv import load_dotenv
import os
class Request:

    @staticmethod
    def getWeather(location:str):
        load_dotenv()
        key = os.getenv("KEY")
        payload = {
            "access_key": key,
            "query": location
        }
        result = requests.get(f'https://api.weatherstack.com/current', params=payload)

        return result.json()
