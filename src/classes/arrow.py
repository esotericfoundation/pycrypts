from src.classes.entity import Entity

class Arrow(Entity):

    def __init__(self, screen, position):
        super().__init__(screen, position, "arrow", 64)
