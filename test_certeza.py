from utils.find_key import find_key
from utils.find_length import find_length
from utils.vigenere import decode, encode, most_probable_length


def letras_iguales(palabra_1, palabra_2):
    cantidad_iguales = sum(
        letra_1 == letra_2 for letra_1, letra_2 in zip(palabra_1, palabra_2)
    )

    return cantidad_iguales/len(palabra_1)


if __name__ == '__main__':
    

    with open('original_text.txt', 'r') as text:
        texto = text.read()

    texto_codificado, all_caps_text = encode(mensaje=texto, clave=CLAVE)

    with open('encoded_text.txt', 'w') as f:
        f.write(texto_codificado)

    largos_posibles = find_length(all_caps_text)
    print(largos_posibles)

    largo = most_probable_length(largos_posibles)
    print(f'Grado de verdad del largo que se dedujo: {largo == len(CLAVE)}')
