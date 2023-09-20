from .base_tool import BaseTool
import cv2

class RectangleTool(BaseTool):
    def draw(self, ix, iy, x, y):
        color = (255, 255, 255)  # Red in this case
        thickness = 2
        cv2.rectangle(self.canvas, (ix, iy), (x, y), color, thickness)