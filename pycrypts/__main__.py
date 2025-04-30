import sys

from pycrypts.game import PyCrypts # Absolute import required for PyInstaller executable

pycrypts = PyCrypts(sys.argv)
pycrypts.init()

while pycrypts.tick():
    pass

pycrypts.quit()
