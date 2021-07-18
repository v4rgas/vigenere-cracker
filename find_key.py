from string import ascii_uppercase
from vigenere import encode, decode, get_key

LARGO_CLAVE  = 4
LETRAS_COMUNES = 'SRNDLC'
FRECUENT_LETTERS ='ETAIONSH' 

KEYS = 5

#Devuelve una lista con tuplas, (CARACTER, FRECUENCIA) ordenadas de mayor frecuencia a menor
def sort_by_frecuency(alist):
    lista_frecuencia = [(char, alist.count(char)) for char in set(alist)]
    lista_frecuencia.sort(key=lambda char: char[1], reverse=True)
    return lista_frecuencia 


def find_key(texto, largo_clave, frecuent_letters):
    # se para el texto en chuncks de tamaño largo_clave
    chuncks = [[letra for index, letra in enumerate(texto) if (index)%(largo_clave) == numero] for numero in range(5)]  

    # limpio chuncks vacios
    chuncks = [chunck for chunck in chuncks if chunck]

    # busco frecuencia
    possible_key = ''
    for chunck in chuncks:
        sorted_chunck = sort_by_frecuency(chunck)
        most_frec_letter, _  = sorted_chunck[0]
        possible_key_letter = get_key(most_frec_letter, frecuent_letters[0])
        
        possible_key+=possible_key_letter

    return possible_key

if __name__ == '__main__':
    # with open()
    pass
