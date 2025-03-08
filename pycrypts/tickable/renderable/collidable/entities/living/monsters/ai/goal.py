class Goal:
    def __init__(self, owner, priority, game):
        self.owner = owner
        self.priority = priority
        self.game = game

    def start(self):
        pass

    def tick(self):
        pass

    def end(self):
        pass

    def can_use(self) -> bool:
        return self.owner.is_alive()
