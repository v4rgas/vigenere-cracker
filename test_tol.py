from time import time
from random import choice
from utils.find_key import find_key
from utils.find_length import find_length
from utils.vigenere import encode, most_probable_length
from main import letras_iguales
from csv import writer
from functools import lru_cache
from string import ascii_uppercase

def read_text():
    with open('stats/moby.txt') as f:
        text = f.read()
        text = text.split()
    return text


@lru_cache(maxsize=None)
def func():
    texto = read_text()
    with open('stats_tol.csv', 'w', newline='') as f:
        fwriter = writer(f)
        fwriter.writerow(('largo de la clave', 'cantidad de palabras',
                         'tolerancia'))
        for key_length in range(5, 300, 5):
            for cant_palabra in range(50000, 100000, 5000):
                # lenght_correcto = False

                chunk_text = ''.join(texto[:cant_palabra])
                clave = ''.join(choice(ascii_uppercase)
                                for _ in range(key_length))
                _, all_caps_text = encode(chunk_text, clave)
                
                # tol = 0.0
                # while not lenght_correcto:
                #     tol += 1
                    # largo = most_probable_length(find_length(all_caps_text), tolerancia=tol)
                #     lenght_correcto = (largo == key_length)

                possibles_lenghts = find_length(all_caps_text)
                
                for index in range(1, len(possibles_lenghts)):
                    num, frec = possibles_lenghts[index - 1]
                    _, frec2 = possibles_lenghts[index]
                    
                    if num == key_length:
                        tolerancia = frec2 / frec
                        print(tolerancia)
                        fwriter.writerow(
                            (key_length, cant_palabra, tolerancia))


func()
