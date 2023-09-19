from ..core import UI, Reactive, Style
import cv2  

class Button(UI, Reactive):
    def __init__(self, img, position = (), style = Style()):
        self._default_color = style.color
        self.img = img
        self.position = position
        self.style = style
        self.is_active = False

    def set_active(self, value):
        self.is_active = value
    
    def _draw_overlay(self, frame, img, length):
        x, y, h, w = length
        if self.is_active:
            self._default_color = self.style.active_color
        else:
            if(self.is_hover): 
                self._default_color = self.style.hover_color
            else:
                self._default_color = self.style.color
        cv2.rectangle(frame, (x, y), (h, w), self._default_color, -1)  # Borde negro
    
    def draw(self, frame):
        self._draw_overlay(frame, self.img, self.position)

class Toggle(UI, Reactive):
    pass