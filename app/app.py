#!/usr/bin/env python3
import serial
import time


def sendMessage(message):
    ser.write((message+"\n").encode('utf-8'))


if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbmodem143301', 9600, timeout=1)
    ser.flush()
    time.sleep(2)  # Leave time for the Arduino to initialize
    sendMessage("128")
