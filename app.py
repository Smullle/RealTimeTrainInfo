from flask import Flask, current_app
from flask import render_template
import requests
import xml.etree.ElementTree as ET


app = Flask(__name__)


@app.route('/')
def index():
    r = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=ENFLD&NumMins=90&format=xml")
    root = ET.fromstring(r.text)

    trains = []

    for train in root.findall('{http://api.irishrail.ie/realtime/}objStationData'):
        trains.append(
            [
                train.find("{http://api.irishrail.ie/realtime/}Duein").text,
                train.find("{http://api.irishrail.ie/realtime/}Destination").text,
                train.find("{http://api.irishrail.ie/realtime/}Expdepart").text,
                train.find("{http://api.irishrail.ie/realtime/}Destinationtime").text,
                train.find("{http://api.irishrail.ie/realtime/}Origin").text
            ]
        )

    return render_template('index.html', trains=trains)


if __name__ == "__main__":
    app.run()