from .base_manager import BaseManager
import numpy as np


class CanvasManager(BaseManager):
    def __init__(self, app):
        self.width = app.width
        self.height = app.height
        self.ui = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.draw = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.temp = np.zeros((self.width, self.height, 3), dtype=np.uint8)

    def save(self):
        self.draw += self.temp

    def clear(self):
        self.draw[:, :] = (0, 0, 0)

    def clear_temp(self):
        self.temp[:, :] = (0, 0, 0)

    def get_canvas(self):
        return (self.ui + self.draw + self.temp)
