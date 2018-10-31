import os
from API import API
from CeleryPy import log
from CeleryPy import move_absolute
from plant_detection.Image import Image
from plant_detection.Parameters import Parameters
from plant_detection.DB import DB
from plant_detection import ENV
from plant_detection import GUI
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from plant_detection.PlantDetection import PlantDetection
from time import gmtime, strftime, time
import json
import requests
import numpy as np
import cv2
import csv

class MyFarmware():
    def __init__(self, farmwarename):
        self.farmwarename = farmwarename
        self.x_photo_pos = 570
        self.y_photo_pos = 350
        self.z_photo_pos = 0
        self.image = None
        self.plant_db = DB()
        self.params = Parameters()
        self.plant_detection = None
        self.dir = os.path.dirname(os.path.realpath(__file__)) + os.sep

        """"self.api = API(self)
        self.points = []"""
    def mov_robot_origin(self):
        log('Execute move: ', message_type='debug', title=str(self.farmwarename))
        move_absolute(
            location=[0, 0, 0],
            offset=[0, 0, 0],
            speed=800)

    def mov_right(self):
        log('Execute move: ', message_type='debug', title=str(self.farmwarename))
        move_absolute(
            location=[300, 400, 0],
            offset=[0, 0, 0],
            speed=800)

    def mov_robot_photo(self):
        log('Execute move: ', message_type='debug', title=str(self.farmwarename))
        move_absolute(
            location=[self.x_photo_pos, self.y_photo_pos, self.z_photo_pos],
            offset=[0, 0, 0],
            speed=800)
    def take_photo(self):
        self.image = Image(self.params, self.plant_db)
        self.image.capture()
        self.image.save('Seedling_photo_' + strftime("%Y-%m-%d_%H:%M:%S", gmtime()))

    def process_photo(self):
        self.plant_detection = PlantDetection(coordinates=True, app=True)
        self.plant_detection.detect_plants()

    def mostrar_foto(self):
        self.run()

    def run(self):
        self.mov_robot_origin()
        self.mov_robot_photo()
        self.take_photo()
        self.mostrar_foto()
        sys.exit(0)
