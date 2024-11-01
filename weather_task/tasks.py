from celery import shared_task
from datetime import datetime

import requests
import os
import json


@shared_task
def weather():
    city_list = ['London']
    api_id = "a5cce6e7742008216acb1fb336f95323"

    data_list = []
    for city in city_list:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + str(city) + "&appid=" + str(api_id), headers={"Content-Type": "json"})

        if not os.path.exists(os.getcwd() + '/storeddata'):
            directory_name = "storeddata"
            os.mkdir(directory_name)

        now_time = datetime.now()

        file_name = f"storeddata/{city}_{now_time}.json"
        with open(file_name, "w") as outfile:
            json.dump(r.text, outfile)

        data_list.append({str(file_name): r.text})

    print('working ====================================== ', data_list)

#shell_command
# from weather_task.tasks import weather
# r = weather()