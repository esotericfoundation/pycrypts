class Tickable:

    tickables: list["Tickable"] = []

    def __init__(self):
        self.load()

    def tick(self):
        pass

    def load(self):
        Tickable.tickables.append(self)

    def unload(self):
        print(f"Unloading tickable {self}")
        if self in Tickable.tickables:
            print(f"Successfully unloaded tickable {self}")
            Tickable.tickables.remove(self)
        else:
            print(f"Failed to unload tickable {self}")
