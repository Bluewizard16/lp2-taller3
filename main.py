from flask import Flask, render_template, redirect

# Buscar en ThingSpeak estaciones meteorológicas:
# https://thingspeak.mathworks.com/channels/public
# Ejemplos:
# https://thingspeak.mathworks.com/channels/870845
# https://thingspeak.mathworks.com/channels/1293177
# https://thingspeak.mathworks.com/channels/12397

URLs = [
]

app = Flask(__name__)

# Programa Principal
if __name__ == '__main__':   
  # Ejecuta la app
  app.run(host='0.0.0.0', debug=True)
