import PyInstaller.__main__
from os import path

location = path.join('..', 'main_gui.py')


PyInstaller.__main__.run([
    location,
    '--onefile',
    '--windowed',
    '--icon=vigenere.ico'
])
