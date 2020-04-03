#!/usr/bin/env python3
import serial
import requests
import time

ser = serial.Serial('/dev/tty.usbmodem143301', 9600, timeout=1)
ser.flush()
time.sleep(2)  # Leave time for the Arduino to initialize


def sendMessage(message):
    ser.write((message+"\n").encode('utf-8'))


def fetchAvailableEBikes():
    data = requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=turbigo&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&refine.name=Turbigo+-+R%C3%A9aumur')
    return data.json()['records'][0]["fields"]["ebike"]


if __name__ == '__main__':
    while True:
        try:
            availableEBikes = fetchAvailableEBikes()
            sendMessage(str(availableEBikes))
        except:
            pass
        time.sleep(30)
