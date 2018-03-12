#! /usr/bin/python
from Tkinter import *
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
root = Tk()
frame=Frame(root)
frame.pack()
degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()
label1=Label(frame,text="Temperatura:  " + str(degrees) + " C degrees")
label2=Label(frame,text="Precion:  " + str(hectopascals) + " hpa")
label3=Label(frame,text="Humedad:  " + str(humidity))

label1.pack()
label2.pack()
label3.pack()      
time.sleep(3)

root.mainloop()