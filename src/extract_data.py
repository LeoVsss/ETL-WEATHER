import requests
import json
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
from dotenv import load_dotenv
import os

input_path = 'config/.env'
env_path = Path(input_path)

load_dotenv(env_path)

api_key = os.getenv('API_KEY')
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={api_key}'

def extract_weather_data(url:str) -> list:

  response = requests.get(url)
  data = response.json()

  if response.status_code != 200:
      logging.error("Erro de requisição")
      return []

  if not data:
      logging.warning("Lista vazia")
      return []  

  if response.status_code == 200:
      logging.warning("Carregado com sucesso")
      return []

  output_path = 'data/weather_data.json'
  output_dir = Path(output_path).parent
  output_dir.mkdir(parents=True, exist_ok=True)

  with open(output_path, 'w') as f:
      json.dump(data, f,indent=4)

  return data  

extract_weather_data(url)