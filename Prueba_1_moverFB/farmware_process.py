import os
from API import API
from CeleryPy import log
from CeleryPy import move_absolute
from CeleryPy import send_message
from plant_detection.Image import Image
from plant_detection.Parameters import Parameters
from plant_detection.DB import DB
from plant_detection import ENV
from plant_detection import GUI
import CeleryPy
import time
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from plant_detection.PlantDetection import PlantDetection
from time import gmtime, strftime, time
import json
import requests
import numpy as np
import cv2
import csv

farmware_name = 'pruebas herramientas_CS'
weeder=(20,553,-402) 
CeleryPy.move_absolute(weeder,(0,0,0),150)
CeleryPy.move_absolute(weeder,(100,0,0),150)
CeleryPy.move_absolute(weeder,(100,0,100),150)
CeleryPy.move_absolute(weeder,(100,0,200),150)

CeleryPy.move_absolute((400,400,-200),(0,0,0),150)
CeleryPy.write_pin(number=4, value=1, mode=0)
CeleryPy.wait(100)
CeleryPy.write_pin(number=4, value=0, mode=0)
CeleryPy.wait(200)
CeleryPy.write_pin(number=4, value=1, mode=0)

CeleryPy.move_absolute(weeder,(120,0,200),150)
CeleryPy.move_absolute(weeder,(120,0,0),150)
CeleryPy.move_absolute(weeder,(0,0,0),150)
CeleryPy.move_absolute(weeder,(0,0,200),150)
send_message(message='PerFect', message_type='success', channel='toast')
CeleryPy.move_absolute((0,0,0),(0,0,0),250)

