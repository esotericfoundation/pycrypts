import pygame as game

from pycrypt.game import PyCrypt

pycrypt = PyCrypt(game)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
