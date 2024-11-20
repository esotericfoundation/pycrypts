import pygame

from game import Game

game = Game()
game.init()

while game.tick():
    pass

pygame.quit()
