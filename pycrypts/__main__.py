import pygame

from pycrypts.game import PyCrypts

pycrypt = PyCrypts(pygame)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
