
from .base_tool import BaseTool
import cv2

class LineTool(BaseTool):
    def draw(self, ix, iy, x, y):
        # Define the color of the line in BGR format (blue, green, red)
        color = (255, 255, 255)  # Red in this case
        # Define the thickness of the line
        thickness = 2
        # Draw the line on the image
        cv2.line(self.canvas, (ix, iy), (x, y), color, thickness)