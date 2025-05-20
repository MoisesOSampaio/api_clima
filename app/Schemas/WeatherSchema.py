from pydantic import BaseModel
from datetime import time
class WeatherSchema(BaseModel):
    nome: str
    pais : str
    regiao : str
    hora : time
    temperatura: float 
