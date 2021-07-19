from string import ascii_lowercase, ascii_uppercase

from utils.find_key import find_key
from utils.find_length import find_lenght
from utils.vigenere import decode, encode


def letras_iguales(palabra_1, palabra_2):
    cantidad_iguales = 0
    for letra_1, letra_2 in zip(palabra_1, palabra_2):
        if letra_1 == letra_2:
            cantidad_iguales += 1
    return cantidad_iguales/len(palabra_1)


if __name__ == '__main__':
    CLAVE = 'FSDAHJIKFDASDSADSADSADSADSADFASDREWXFCDGDFDGFDGFDGERDHSAJKDASHDJKASBJWKDABNSDKANSDQOWJHDNASLKJDASHNASLKDADKS'
    print(len(CLAVE))

    with open('original_text.txt', 'r') as text:
        texto = text.read()
        texto = ''.join(
            [letra for letra in texto if letra in ascii_uppercase + ascii_lowercase])
        texto = texto.upper()

    texto_codificado = encode(mensaje=texto, clave=CLAVE)
    with open('encoded_text.txt', 'w') as f:
        f.write(texto_codificado)

    largos_posibles = find_lenght(texto_codificado)
    print(largos_posibles)
    clave = find_key(texto_codificado, largo_clave=len(CLAVE), lang='ENG')
    print(clave, letras_iguales(clave, CLAVE))

    texto_decodificado_teoria = decode(mensaje=texto_codificado, clave=clave)
    with open('decoded_text.txt', 'w') as f:
        f.write(texto_decodificado_teoria)
