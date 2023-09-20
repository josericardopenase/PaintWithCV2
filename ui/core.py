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
        position = self.get_position()
        return x >= position[0] and x <= position[2] and y >= position[1] and y <= position[3]

    def track(self, event, x, y, flags, param):
        self.is_hover = self.is_hovered(x, y) 
        if event == cv2.EVENT_LBUTTONDOWN and self.is_hovered(x, y):  # Verifica si el clic está dentro del cuadro 'line'
            if self.bd_callback : self.bd_callback()
        if event == cv2.EVENT_LBUTTONUP and self.is_hovered(x, y):  # Verifica si el clic está dentro del cuadro 'line'
            if self.bu_callback : self.bu_callback()

class UI:
    def get_position(self):
        return (self.position[0], self.position[1], self.position[0] + self.style.width, self.position[1] + self.style.height)

    def draw(self):
        pass


@dataclass
class Style: 
    color : tuple = (255, 255, 255)
    hover_color : tuple = (0, 0, 0)
    active_color : tuple = (255, 255, 255)
    text : str = ""
    width: int = 0
    height : int = 0
    paddingLeft: int = 0
    paddingRight: int = 0
    paddingTop: int = 0
    paddingBottom: int = 0
    marginLeft: int = 0
    marginTop: int = 0
    marginRight: int = 0
    marginBottom: int = 0
    text_color: tuple = (255, 255, 255)
    flex_dir : str = 'col'
    flex_gap : str = 0
    outer_gap : str = 0
    border_radius : int = 0
