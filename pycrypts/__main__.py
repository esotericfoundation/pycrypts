import pygame
import logging

from pycrypts.game import PyCrypts

pycrypt = PyCrypts(pygame, logging)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
