from core.app import App
from ui.components import Button, Style, Toggle, Group
from tools.line_tool import LineTool
from tools.rectangle_tool import RectangleTool
from tools.circle_tool import CircleTool

app = App(800, 800)

bs = Style(
    color=(255, 255, 255), 
    hover_color=(90, 50, 50), 
    active_color=(255, 0, 0),
    width=50,
    height=50
)


gs = Style(
    flex_dir='col',
    flex_gap=10,
    outer_gap=20,
    width=400
)

b1 = Button(img='imagen.jpg', style=bs)
b2 = Button(img='imagen.jpg',  style=bs)
b3 = Button(img='imagen.jpg',  style=bs)
b4 = Button(img='imagen.jpg', style=bs)

button_group = Group([
    b1, 
    b2, 
    b3,
    b4
], position=(0, 0), style=gs)

b1.onButtonDown(lambda : app.tools.set_tool(LineTool))
b2.onButtonDown(lambda : app.tools.set_tool(RectangleTool))
b3.onButtonDown(lambda : app.tools.set_tool(CircleTool))
b4.onButtonDown(lambda : app.canvas.clear())

app.ui.add(button_group)

app.run()