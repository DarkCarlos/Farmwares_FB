import os
from API import API
from CeleryPy import log
from CeleryPy import move_absolute
from plant_detection.Image import Image
from plant_detection.Parameters import Parameters
from plant_detection.DB import DB
from plant_detection import ENV
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
        self.x_photo_pos = 400
        self.y_photo_pos = 235
        self.z_photo_pos = 0

        """"self.api = API(self)
        self.points = []"""
    def mov_robot_origin(self):
        log('Execute move: ', message_type='debug', title=str(self.farmwarename))
        move_absolute(
            location=[0, 0, 0],
            offset=[0, 0, 0],
            speed=800)
    def mov_robot_photo(self):
        log('Execute move: ', message_type='debug', title=str(self.farmwarename))
        move_absolute(
            location=[self.x_photo_pos, self.y_photo_pos, self.z_photo_pos],
            offset=[0, 0, 0],
            speed=800)

    def run(self):
        self.mov_robot_origin()
        self.mov_robot_photo()
        sys.exit(0)
