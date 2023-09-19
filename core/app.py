import cv2  
import numpy as np
import matplotlib.pyplot as plt
from .managers.ui_manager import UIManager
from .managers.tool_manager import ToolManager
from .managers.canvas_manager import CanvasManager


class App:
    window = 'Drawing'

    def __init__(self, width, height):
        self.canvas = CanvasManager(width, height)
        self.ui = UIManager()
        self.tools = ToolManager(self)
    
    def callbacks(self, *args):
        self.ui.callbacks(*args)
        self.tools.callbacks(*args)
    
    def run(self):
        cv2.namedWindow('Drawing', cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty('Drawing', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while True:
            self.ui.draw(self.canvas.ui)
            cv2.setMouseCallback(self.window, self.callbacks)
            cv2.imshow(self.window, self.canvas.get_canvas())
            if cv2.waitKey(20) == 27:
                break
        