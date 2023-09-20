
from .base_tool import BaseTool
import cv2

class EllipseTool(BaseTool):
    def draw(self, ix, iy, x, y):
        color = (255, 255, 255)
        thickness = 2
        cv2.line(self.canvas, (ix, iy), (x, y), color, thickness)