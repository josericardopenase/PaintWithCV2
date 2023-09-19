from dataclasses import dataclass
import cv2  

class Reactive:
    is_pressed = False
    is_toggled = False
    is_hover = False
    bd_callback = None
    bu_callback = None

    def subscribe():
        pass

    def onButtonDown(self, function):
        self.bd_callback = function
    
    def onButtonUp(self, function):
        self.bu_callback = function
    
    def is_hovered(self, x, y):
        return x >= self.position[0] and x <= self.position[2] and y >= self.position[1] and y <= self.position[3]

    def track(self, event, x, y, flags, param):
        self.is_hover = self.is_hovered(x, y) 
        if event == cv2.EVENT_LBUTTONDOWN and self.is_hovered(x, y):  # Verifica si el clic está dentro del cuadro 'line'
            if self.bd_callback : self.bd_callback()
        if event == cv2.EVENT_LBUTTONUP and self.is_hovered(x, y):  # Verifica si el clic está dentro del cuadro 'line'
            if self.bu_callback : self.bu_callback()

class UI:
    def draw(self):
        pass

@dataclass
class Style: 
    color : tuple = (255, 255, 255)
    hover_color : tuple = (0, 0, 0)
    active_color : tuple = (255, 255, 255)
    text : str = ""
