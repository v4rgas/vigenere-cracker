from string import ascii_uppercase

from utils.find_key import find_key
from utils.find_length import find_lenght
from utils.vigenere import encode

if __name__ == '__main__':
    CLAVE = 'ABCD'

    with open('original_text.txt', 'r') as text:
        texto = text.read().upper()
        texto = ''.join([letra for letra in texto if letra in ascii_uppercase])

    texto_codificado = encode(mensaje=texto, clave=CLAVE)
    with open('encoded_text.txt', 'w') as f:
        f.write(texto_codificado)

    print(find_lenght(texto_codificado))
    print(find_key(texto_codificado,largo_clave=4,lang='ENG' ))
    


    
    
