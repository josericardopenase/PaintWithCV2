class BaseManager:
    def __init__(self, app) -> None:
        self.app = app

    def callbacks(self, event, x, y, flags, param):
        pass
