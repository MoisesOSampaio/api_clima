from app.Helpers.Request import Request
from app.Schemas.WeatherSchema import WeatherSchema
from datetime import datetime
from http import HTTPStatus
from fastapi import HTTPException
class WeatherServices:
    
    def pegarTemperaturaAtual(self,local : str):
        response = Request.getWeather(local)
        return self.__tratarDados(response)


    def __tratarDados(self,response) -> WeatherSchema:
        if "success" in response.keys():
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=response["error"]["info"])
        weatherSchema = WeatherSchema(
            nome=response["location"]["name"], 
            pais=response["location"]["country"], 
            regiao=response["location"]["region"], 
            hora=datetime.strptime(response["current"]["observation_time"],'%I:%M %p').time(), 
            temperatura=response["current"]["temperature"])
        return weatherSchema
