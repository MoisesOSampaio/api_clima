from fastapi import FastAPI
from app.Helpers.Request import Request
from app.Controller.WeatherController import router
app = FastAPI()


app.include_router(router)