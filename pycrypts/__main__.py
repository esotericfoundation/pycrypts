import sys

from pycrypts.game import PyCrypts

pycrypt = PyCrypts(sys.argv)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
