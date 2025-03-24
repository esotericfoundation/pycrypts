import logging
import sys

from pycrypts.game import PyCrypts

pycrypt = PyCrypts(logging, sys.argv)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
