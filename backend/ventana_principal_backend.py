from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal

from utils.find_key import find_key
from utils.find_length import find_length
from utils.vigenere import decode

class VentanaPrincipalBackend(QObject):
    senal_add_to_table = pyqtSignal(list)
    senal_pop_up = pyqtSignal(str)
    senal_set_text = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.texto_codificado = ''
        self.clave_encontrada = ''
        self.largos_posibles = []

    def set_file(self, path):
        self.senal_add_to_table.emit([(0,0) for _ in range(4)])
        self.senal_set_text.emit('')
        self.texto_codificado = ''
        self.clave_encontrada = ''
        self.largos_posibles = []

        with open(path) as file:
            self.texto_codificado = file.read()

    def start_find_length(self):
        thread = Thread(target=self.find_length)
        thread.start()

    def find_length(self):
        if self.texto_codificado:
           self.largos_posibles = find_length(self.texto_codificado)
           self.senal_add_to_table.emit(self.largos_posibles)

        else:
            self.senal_pop_up.emit('Se requiere un un texto para decodificar')

    def start_find_key(self,largo):
        thread = Thread(target=self.find_key, args=(largo,))
        thread.start()

    def find_key(self, largo):
        if self.texto_codificado and largo<0:
            self.clave_encontrada = find_key(self.texto_codificado, largo_clave=largo, lang='ENG')
            self.senal_set_text.emit(self.clave_encontrada)
        
        if not self.texto_codificado:
            self.senal_pop_up.emit('Se requiere un un texto para decodificar')

        if largo<1:
            self.senal_pop_up.emit('Necesitas introducir o generar una clave')
        

    def decodificar(self):
        if self.clave_encontrada:
            texto_decodificado = decode(self.texto_codificado, self.clave_encontrada)
            with open('decoded_text.txt', 'w') as f:
                f.write(texto_decodificado)
        else:
            self.senal_pop_up.emit('Debes completar pasos previos')
            
    
        
