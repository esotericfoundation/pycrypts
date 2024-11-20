class Tickable:

    tickables: list["Tickable"] = []

    def __init__(self):
        Tickable.tickables.append(self)

    def tick(self):
        pass

    def unload(self):
        Tickable.tickables.remove(self)
