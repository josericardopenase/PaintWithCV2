from ..core import UI

class Group(UI):
    items = []
     
    def add(self, ui):
        self.items.append(ui)

    def draw(self, frame):
        for x in self.items:
            x.draw(frame)