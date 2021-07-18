from string import ascii_uppercase

from utils.find_key import find_key
from utils.find_length import find_lenght
from utils.vigenere import decode, encode

if __name__ == '__main__':
    CLAVE = 'ABCDEFGHIJKMNLOPQRSTUVWXYZ'
    print(len(CLAVE))

    with open('original_text.txt', 'r') as text:
        texto = text.read().upper()
        texto = ''.join([letra for letra in texto if letra in ascii_uppercase])

    texto_codificado = encode(mensaje=texto, clave=CLAVE)
    with open('encoded_text.txt', 'w') as f:
        f.write(texto_codificado)

    largos_posibles = find_lenght(texto_codificado)
    print(largos_posibles)
    largo = largos_posibles[0][0]
    clave = find_key(texto_codificado,largo_clave=len(CLAVE),lang='ENG')
    print(clave)
    
    texto_decodificado_teoria = decode(mensaje=texto_codificado, clave=clave)
    with open('decoded_text.txt', 'w') as f:
        f.write(texto_decodificado_teoria)


    
    
