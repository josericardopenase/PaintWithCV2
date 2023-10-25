from .base_manager import BaseManager
import cv2


class ToolManager(BaseManager):
    tool = None
    drawing = False

    def set_tool(self, tool):
        self.tool = tool(self.app.canvas.temp)

    def callbacks(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
        if event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.tool.reset()
            self.app.canvas.save()

        if self.drawing and self.tool:
            self.app.canvas.clear_temp()
            self.tool.execute(x, y)
