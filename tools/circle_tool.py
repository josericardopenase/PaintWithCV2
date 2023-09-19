from .base_tool import BaseTool
import numpy as np
import cv2

class CircleTool(BaseTool):
    def draw(self, ix, iy, x, y):
        center = (ix, iy)  # (x, y) coordinates of the center
        color = (0, 0, 255)  # Red in this case
        thickness = 2
        #cv2.circle(self.canvas, center, radius, color, thickness)