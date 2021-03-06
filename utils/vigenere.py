from string import ascii_uppercase, ascii_lowercase
from math import ceil


def encode(mensaje, clave):
    full_text = ''
    all_caps_text = ''
    index_clv = 0
    for letter in mensaje:
        alfabeto = ascii_lowercase if letter.islower() else ascii_uppercase

        if letter in alfabeto:
            displacement = ascii_uppercase.find(clave[index_clv].upper())
            index_clv = (index_clv+1) % len(clave)

            encoded_letter = alfabeto[(
                displacement+alfabeto.find(letter)) % len(alfabeto)]

            full_text += encoded_letter
            all_caps_text += encoded_letter.upper()

        else:
            full_text += letter

    return full_text, all_caps_text


def decode(mensaje, clave):
    full_text = ''
    all_caps_text = ''
    index_clv = 0
    for letter in mensaje:
        alfabeto = ascii_lowercase if letter.islower() else ascii_uppercase

        if letter in alfabeto:
            displacement = ascii_uppercase.find(clave[index_clv].upper())
            index_clv = (index_clv+1) % len(clave)

            encoded_letter = alfabeto[(
                alfabeto.find(letter)-displacement) % len(alfabeto)]

            full_text += encoded_letter
            all_caps_text += encoded_letter.upper()

        else:
            full_text += letter

    return full_text, all_caps_text


def get_key(encr_letter, deencr_letter):
    alfabeto = ascii_uppercase
    diff = alfabeto.find(encr_letter)-alfabeto.find(deencr_letter)
    diff = (diff+len(alfabeto)) % len(alfabeto)
    return alfabeto[diff]


def most_probable_length(largos_posibles, tolerancia = 0.05):

    lista_factibles = []
    for index in range(len(largos_posibles) - 1):
        num, frec = largos_posibles[index]
        _, frec2 = largos_posibles[index+1]

        if tolerancia > frec2 / frec:
            lista_factibles.append(num)
            break
    
    if lista_factibles:
        return max(lista_factibles)

    return largos_posibles[0][0]

# def most_probable_length(largos_posibles):
#     largos_factibles = []
#     for index in range(len(largos_posibles) - 1):
#         largos_factibles.append(largos_posibles[index])
#         if largos_posibles[index][1] >= largos_posibles[index + 1][1] * 18:
#             break

#     return max(largos_factibles)[0]

# Devuelve una lista con tuplas, (CARACTER, FRECUENCIA) ordenadas de mayor frecuencia a menor


def sort_by_frecuency(alist):
    lista_frecuencia = [(char, alist.count(char)) for char in set(alist)]
    lista_frecuencia.sort(key=lambda char: char[1], reverse=True)
    return lista_frecuencia


if __name__ == '__main__':
    full, partial = encode('Hola, que tal? como va todo.', 'AEXO')
    full_decoded, partial_decoded = decode(full, 'AEXO')

    print(full, full_decoded)
    print(partial, partial_decoded)


# A -> B
