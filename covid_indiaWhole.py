import requests     #pip3/pip install requests
import json 
from plyer import notification  #pip3/pip install plyer 

def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10,
    )

r = requests.get('https://api.covid19india.org/data.json')
data_json = r.json()

confirmed_str = json.dumps(data_json['statewise'][0]['confirmed'])
active_str = json.dumps(data_json['statewise'][0]['active'])
cured_recovered = json.dumps(data_json['statewise'][0]['recovered'])
deaths = json.dumps(data_json['statewise'][0]['deaths'])

notify_title = "Covid-19 Status"
notify_text = f"Confirmed : {confirmed_str}\nActive Cases : {active_str}\nCured/Discharged : {cured_recovered}\nDeaths : {deaths}"

notify_me(notify_title, notify_text)
