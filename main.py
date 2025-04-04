from flask import Flask, render_template, redirect
import pandas as pd
import matplotlib.pyplot as plt

# Buscar en ThingSpeak estaciones meteorológicas:
# https://thingspeak.mathworks.com/channels/public
# Ejemplos:
# https://thingspeak.mathworks.com/channels/870845
# https://thingspeak.mathworks.com/channels/1293177
# https://thingspeak.mathworks.com/channels/12397

URLs = [
    'https://api.thingspeak.com/channels/159150/feeds.csv?results=8000',
    'https://api.thingspeak.com/channels/196384/feeds.csv?results=8000',
    'https://api.thingspeak.com/channels/178343/feeds.csv?results=8000',
]


app = Flask(__name__)
def descargar(url):
  # descarga el CSV en un dataframe, desde el URL
  df = pd.read_csv(url)
  # Convertir la cadena en una fecha real
  df['created_at'] = pd.to_datetime(df['created_at'])
  # Borrar columnas innecesarias
  if 'field6' in df.columns:
    df.drop(['entry_id', 'field5', 'field6'], axis=1, inplace=True)
  else:
    df.drop(['entry_id', 'field5', 'field6'], axis=1, inplace=True)

  # Renombrar columnas
  df.columns = ['fecha', 'temp_exterior', 'temp_interior', 'presion_atm', 'humedad']
  return df

def graficar(df):
  # Crear la figura
  fig = plt.figure(figsize=(8, 5))
  plt.plot(df['fecha'], df['temp_exterior'], label='Temperatura Exterior')
  plt.plot(df['fecha'], df['temp_interior'], label='Temperatura Interior')

@app.route('/')
def index():
  return render_template('index.html')

# Programa Principal
if __name__ == '__main__':   


  app.run(host='0.0.0.0', debug=True)
