import cv2  
import numpy as np
import matplotlib.pyplot as plt
from .base_manager import BaseManager

class UIManager(BaseManager):
    ui_elements = list()

    def add(self, element):
        self.ui_elements.append(element)
    
    def callbacks(self, event, x, y, flags, param):
        for ui_element in self.ui_elements:
            ui_element.track(event, x, y, flags, param)

    def draw(self):
        for x in self.ui_elements:
            x.draw(self.app.canvas.ui)
