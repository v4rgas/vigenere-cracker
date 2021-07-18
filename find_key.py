from string import ascii_uppercase
from vigenere import encode, decode, get_key

LARGO_CLAVE = 4
LETRAS_COMUNES = 'SRNDLC'
FRECUENT_LETTERS = 'ETAIONSH'

KEYS = 5

# Devuelve una lista con tuplas, (CARACTER, FRECUENCIA) ordenadas de mayor frecuencia a menor


def sort_by_frecuency(alist):
    lista_frecuencia = [(char, alist.count(char)) for char in set(alist)]
    lista_frecuencia.sort(key=lambda char: char[1], reverse=True)
    return lista_frecuencia


with open('example_text.txt') as file:
    TEXTO = file.read()

# TEXTO = 'ABABABABAB'

chuncks = [[letra for index, letra in enumerate(TEXTO) if (
    index) % (LARGO_CLAVE) == numero] for numero in range(LARGO_CLAVE)]

# LIMPIO CHUNCKS VACIOS
chuncks = [chunck for chunck in chuncks if chunck]

# BUSCO FRECUENCIA
possible_key = ''
for chunck in chuncks:
    sorted_chunck = sort_by_frecuency(chunck)
    most_frec_letter, most_frec = sorted_chunck[0]
    possible_key_letter = get_key(most_frec_letter, FRECUENT_LETTERS[0])

    possible_key += possible_key_letter

print(possible_key)

with open('de.txt', 'w') as file:
    file.write(decode(TEXTO, possible_key))
