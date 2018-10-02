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

    def label(self, p2c=None, weeder_remove=False, weeder_safe_remove=False):
        """Draw circles on image indicating detected plants."""
        def _circle(objects, color, already_pixels=False):
            bgr = {'red': (0, 0, 255),
                   'green': (0, 255, 0),
                   'blue': (255, 0, 0),
                   'cyan': (255, 255, 0),
                   'grey': (200, 200, 200)}
            if not already_pixels:
                pixel_objects = p2c.convert(objects, to_='pixels')
            else:
                pixel_objects = objects
            for obj in pixel_objects:
                cv2.circle(self.images['marked'], (int(obj[0]), int(obj[1])),
                           int(obj[2]), bgr[color], CIRCLE_LINEWIDTH)

        if p2c is None:
            detected_pixel_objects = self.plant_db.pixel_locations
            _circle(detected_pixel_objects, 'red', already_pixels=True)
        else:
            # Mark known plants
            known = [[_['x'], _['y'], _['radius']] for _
                     in self.plant_db.plants['known']]
            _circle(known, 'green')

            # Mark weeds
            remove = [[_['x'], _['y'], _['radius']] for _
                      in self.plant_db.plants['remove']]
            _circle(remove, 'red')

            # Mark weeder size for weeds
            if weeder_remove:
                weeder_size = self.plant_db.weeder_destrut_r
                remove_circle = [[_['x'], _['y'], weeder_size] for _
                                 in self.plant_db.plants['remove']]
                _circle(remove_circle, 'grey')

            # Mark saved plants
            save = [[_['x'], _['y'], _['radius']] for _
                    in self.plant_db.plants['save']]
            _circle(save, 'blue')

            # Mark safe-remove weeds
            safe_remove = [[_['x'], _['y'], _['radius']] for _
                           in self.plant_db.plants['safe_remove']]
            _circle(safe_remove, 'cyan')

            # Mark weeder size for safe-remove weeds
            if weeder_safe_remove:
                weeder_size = self.plant_db.weeder_destrut_r
                safe_remove_circle = [[_['x'], _['y'], weeder_size] for _
                                      in self.plant_db.plants['safe_remove']]
                _circle(safe_remove_circle, 'grey')

    def run(self):
        self.mov_robot_origin()
        self.mov_robot_photo()
        self.label(p2c=none,weeder_remove=False,weeder_safe_remove=False)
        sys.exit(0)
