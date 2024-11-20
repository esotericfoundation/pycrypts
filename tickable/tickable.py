class Tickable:

    tickables: list["Tickable"] = []

    def __init__(self):
        self.load()

    def tick(self):
        pass

    def load(self):
        Tickable.tickables.append(self)

    def unload(self):
        if self in Tickable.tickables:
            Tickable.tickables.remove(self)
