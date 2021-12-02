import requests
import json

def calculateDegreeds(temp):
    KelvinTemp = float(temp);
    CelsiusTemp = KelvinTemp - 273.15;
    CelsiusString = str(CelsiusTemp);
    return CelsiusString;

openWeatherKey = ""
openwwatherApi = "https://api.openweathermap.org/data/2.5/weather?"

print("Este programa consulta la api de openwather.org")

print("Ingrese la ciydad a consultar: ")
ciudad = input()
uri = openwwatherApi + "q=" + ciudad + "&appid=" + openWeatherKey;
data = requests.get(uri)
result = json.loads(data.text)
feelLikes = calculateDegreeds(result["main"]["feels_like"])
temp = calculateDegreeds(result["main"]["temp"])
    
print("La temperatura en " + ciudad + "es de "+ temp +" y la sensacion termica es de " + feelLikes)