from http import HTTPStatus
from fastapi import HTTPException,APIRouter
from app.Schemas.WeatherSchema import WeatherSchema
from app.Helpers.Request import Request
from app.Services.WeatherServices import WeatherServices

router = APIRouter()

class WeatherController:

    @router.get("/{local}",status_code=HTTPStatus.OK, response_model=WeatherSchema)
    def getWeather(local : str):
        print(local)

        services = WeatherServices()
        result = services.pegarTemperaturaAtual(local)
        print(result)
        return result