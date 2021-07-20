from string import ascii_uppercase
from functools import lru_cache
from csv import writer
from main import letras_iguales
from utils.vigenere import encode, most_probable_length
from utils.find_length import find_length
from utils.find_key import find_key
from random import choice
from time import time


def read_text():
    with open('recursos/moby.txt') as f:
        text = f.read()
        text = text.split()
    return text


texto = read_text()


@lru_cache(maxsize=None)
def func():
    with open('stats5.csv', 'w', newline='') as f:
        fwriter = writer(f)
        fwriter.writerow(('largo de la clave', 'cantidad de palabras',
                         'semejanza entre claves', 'tiempo transcurrido'))
        for key_length in range(5, 250, 5):
            for cant_palabra in range(100, 20000, 100):

                start_time = time()

                chunk_text = ''.join(texto[:cant_palabra])
                clave = ''.join(choice(ascii_uppercase)
                                for _ in range(key_length))
                _, all_caps_text = encode(chunk_text, clave)
                largo = most_probable_length(find_length(all_caps_text))
                clave_teorica = find_key(
                    all_caps_text, largo_clave=largo, lang='ENG')
                semejanza_claves = letras_iguales(clave, clave_teorica)
                finish_time = time()-start_time
                fwriter.writerow(
                    (key_length, cant_palabra, semejanza_claves, finish_time))


func()
