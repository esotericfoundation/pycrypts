import pygame
import logging
import sys

from pycrypts.game import PyCrypts

pycrypt = PyCrypts(pygame, logging, sys.argv)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
