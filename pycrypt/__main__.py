import pygame

from pycrypt.game import PyCrypt

pycrypt = PyCrypt(pygame)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
