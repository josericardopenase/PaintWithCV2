class BaseTool:
    def __init__(self, canvas):
        self.initial_point = None
        self.canvas = canvas

    def reset(self):
        self.initial_point = None

    def execute(self, x, y):
        if not self.initial_point:
            self.initial_point = (x, y)
        self.draw(self.initial_point[0], self.initial_point[1], x, y)

    def draw(self, ix, iy, x, y):
        pass
