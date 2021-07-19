from threading import Thread
from os import path

from PyQt5.QtCore import QObject, pyqtSignal

from utils.find_key import find_key
from utils.find_length import find_length
from utils.vigenere import decode, most_probable_length


class VentanaPrincipalBackend(QObject):
    senal_add_to_table = pyqtSignal(list)
    senal_pop_up = pyqtSignal(str)
    senal_set_text = pyqtSignal(str)
    senal_set_recomended = pyqtSignal(str)

    senal_boton_archivo = pyqtSignal(bool)
    senal_boton_encuentra_largo = pyqtSignal(bool)
    senal_boton_encuentra_key = pyqtSignal(bool)
    senal_boton_decodificar = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.texto_codificado = ''
        self.clave_encontrada = ''
        self.largos_posibles = []
        self.file_path = ''
        self.lang = 'ENG'

    def change_lang(self, lang):
        self.lang = lang
        print(lang)

    def set_file(self, path):
        self.senal_boton_decodificar.emit(False)

        self.senal_add_to_table.emit([(0, 0) for _ in range(4)])
        self.senal_set_text.emit('')
        self.texto_codificado = ''
        self.clave_encontrada = ''
        self.largos_posibles = []
        self.file_path = ''

        with open(path) as file:
            self.file_path = path
            self.texto_codificado = file.read()
            self.texto_codificado = ''.join(
                [letter.upper() for letter in self.texto_codificado if letter.isalpha()])

        self.senal_boton_decodificar.emit(True)

    def start_find_length(self):
        thread = Thread(target=self.find_length)
        thread.start()

    def find_length(self):
        self.senal_boton_encuentra_largo.emit(False)

        if self.texto_codificado:
            self.largos_posibles = find_length(self.texto_codificado)
            self.senal_add_to_table.emit(self.largos_posibles)

            self.senal_set_recomended.emit(self.most_probable_length())

        else:
            self.senal_pop_up.emit('Se requiere un un texto para decodificar')

        self.senal_boton_encuentra_largo.emit(True)

    def start_find_key(self, largo):
        thread = Thread(target=self.find_key, args=(largo,))
        thread.start()

    def find_key(self, largo):
        self.senal_boton_encuentra_key.emit(False)

        if self.texto_codificado and largo > 0:
            self.clave_encontrada = find_key(
                self.texto_codificado, largo_clave=largo, lang=self.lang)
            self.senal_set_text.emit(self.clave_encontrada)
        else:
            if not self.texto_codificado:
                self.senal_pop_up.emit(
                    'Se requiere un un texto para decodificar')

            if largo < 1:
                self.senal_pop_up.emit(
                    'Necesitas introducir o generar una clave')
                self.senal_set_text.emit('')

        self.senal_boton_encuentra_key.emit(True)

    def decodificar(self):
        self.senal_boton_decodificar.emit(False)

        if self.clave_encontrada and path.exists(self.file_path):
            with open(self.file_path) as f:
                texto = f.read()

            texto_decodificado, _ = decode(
                texto, self.clave_encontrada)
            with open('decoded_text.txt', 'w') as f:
                f.write(texto_decodificado)
        else:
            if not path.exists(self.file_path):
                self.senal_pop_up.emit('ARCHIVO DEJO DE EXISTIR')
            else:
                self.senal_pop_up.emit('Debes completar pasos previos')
        self.senal_boton_decodificar.emit(True)

    def most_probable_length(self):
        return str(most_probable_length(self.largos_posibles))
