import pygame

def tick_all_entities():
    for entity in Entity.entities:
        entity.tick()
    pass

class Entity:

    entities = []

    def __init__(self, screen, position, character, size):
        self.screen = screen

        self.position = position

        image = pygame.image.load("./assets/entities/" + character + ".png").convert_alpha()
        self.image = pygame.transform.scale(image, (size, size))

        self.size = size

        Entity.entities.append(self)

    def render(self):
        self.screen.blit(self.image, self.position)

    def tick(self):
        self.move()
        self.render()

    def move(self):
        pass

    def move_without_collision(self, distance_travelled):
        if distance_travelled.magnitude_squared() != 0:
            distance_travelled = distance_travelled.normalize() * 0.15

            self.position += distance_travelled

            for entity in Entity.entities:
                if entity == self:
                    continue

                if self.is_colliding(entity):
                    self.position -= distance_travelled
                    break

    def is_inside_hitbox(self, location):
        return self.position.distance_to(location) < (self.size / 2)

    def is_colliding(self, entity):
        return self.position.distance_to(entity.position) < (self.size / 2 + entity.size / 2)

    def remove(self):
        if self in Entity.entities:
            Entity.entities.remove(self)
