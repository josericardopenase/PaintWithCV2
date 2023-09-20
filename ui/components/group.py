from ..core import UI, Style

class Group(UI):
    items = []

    def __init__(self, items, position=(0, 0), style=Style()):
        self.items = items
        self.style = style
        self.position = (position[0] + self.style.outer_gap, position[1] + self.style.outer_gap)

    def track(self, *args):
        for x in self.items:
            x.track(*args)

    def draw(self, frame):
        prev = None
        for x in self.items:
            if prev == None:
                x.position = self.position
            else:
                if self.style.flex_dir == 'col':
                    x.position = (prev.position[0] , prev.position[1] +  prev.style.height + self.style.flex_gap)
                else:
                    x.position = (prev.position[0] + prev.style.width + self.style.flex_gap, self.position[1])

            x.draw(frame)
            prev = x