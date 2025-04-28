import sys

from pycrypts.game import PyCrypts # Absolute import required for PyInstaller executable

pycrypt = PyCrypts(sys.argv)
pycrypt.init()

while pycrypt.tick():
    pass

pycrypt.quit()
