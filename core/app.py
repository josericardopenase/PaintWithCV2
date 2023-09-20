import cv2  
import numpy as np
import matplotlib.pyplot as plt
from .managers.ui_manager import UIManager
from .managers.tool_manager import ToolManager
from .managers.canvas_manager import CanvasManager


class App:

    def __init__(self, width, height, window='Drawing', bg=(245,245,245)):
        self.width = width
        self.height = height
        self.window = window
        self.bg=bg

        self.canvas = CanvasManager(self)
        self.ui = UIManager(self)
        self.tools = ToolManager(self)
    
    def callbacks(self, *args):
        self.ui.callbacks(*args)
        self.tools.callbacks(*args)
        self.canvas.callbacks(*args)
    
    def run(self):
        cv2.namedWindow(self.window, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty(self.window, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback(self.window, self.callbacks)

        while True:
            self.ui.draw()
            cv2.imshow(self.window, self.canvas.get_canvas())
            if cv2.waitKey(20) == 27:
                break
        