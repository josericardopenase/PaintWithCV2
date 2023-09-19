from .core.app import App
from .ui.components import Button, Style, Toggle
from .tools.line_tool import LineTool
from .tools.rectangle_tool import RectangleTool
from .tools.circle_tool import CircleTool

app = App(800, 800)

bs = Style(color=(255, 255, 255), hover_color=(90, 50, 50), active_color=(255, 0, 0))

b1 = Button(img='imagen.jpg', position=(0, 0, 40, 40), style=bs)
b2 = Button(img='imagen.jpg', position=(40, 0, 80, 40), style=bs)
b3 = Button(img='imagen.jpg', position=(80, 0, 120, 40), style=bs)
b4 = Button(img='imagen.jpg', position=(120, 0, 160, 40), style=bs)

b1.onButtonDown(lambda : app.tools.set_tool(LineTool))
b2.onButtonDown(lambda : app.tools.set_tool(RectangleTool))
b3.onButtonDown(lambda : app.tools.set_tool(CircleTool))
b4.onButtonDown(lambda : app.canvas.clear())

app.ui.add(b1)
app.ui.add(b2)
app.ui.add(b3)
app.ui.add(b4)

app.run()