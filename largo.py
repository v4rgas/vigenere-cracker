from vigenere import encode, decode
from string import ascii_uppercase


def binomio_finder(text: str) -> dict:
    diccionario_binomio = {}
    for index in range(0, len(texto_codificado) - 1):
        binomio = texto_codificado[index:index + 2]
        lista_llaves = list(diccionario_binomio.keys())
        if binomio in lista_llaves:
            diccionario_binomio[binomio] += 1
        else:
            diccionario_binomio[binomio] = 1

    lista_aux = []
    for key in diccionario_binomio.keys():
        lista_aux.append((key, diccionario_binomio[key]))

    lista_aux = sorted(lista_aux, key=lambda x: x[1], reverse=True)

    return lista_aux, diccionario_binomio


def trinomio_finder(text: str) -> dict:
    diccionario_trinomio = {}
    for index in range(0, len(texto_codificado) - 2):
        trinomio = texto_codificado[index:index + 3]
        lista_llaves = list(diccionario_trinomio.keys())
        if trinomio in lista_llaves:
            diccionario_trinomio[trinomio] += 1
        else:
            diccionario_trinomio[trinomio] = 1

    lista_aux = []
    for key in diccionario_trinomio.keys():
        lista_aux.append((key, diccionario_trinomio[key]))

    lista_aux = sorted(lista_aux, key=lambda x: x[1], reverse=True)

    return lista_aux, diccionario_trinomio


with open('text.csv', 'r') as text:
    texto = text.read()
    texto = texto.upper()
    texto = str([letra for letra in texto if letra in ascii_uppercase])
    # print(texto)

clave = 'ABCEFGHIJ'
clave = clave.upper()

texto_codificado = encode(mensaje=texto, clave=clave)
texto_decodificado = decode(mensaje=texto_codificado, clave=clave)

lista_ordenada_trinomio, diccionario_tri = trinomio_finder(texto_codificado)
lista_ordenada_binomio, diccioanrio_bi = binomio_finder(texto_codificado)

# print(lista_ordenada_trinomio)

lista_ordenada_trinomio = lista_ordenada_trinomio[0:5]
lista_ordenada_binomio = lista_ordenada_binomio[0:5]

lista_ordenada = lista_ordenada_binomio + lista_ordenada_trinomio

diccionario_nomios = {}
for tupla in lista_ordenada:
    nomio = tupla[0]
    largo = len(nomio)

    lista_distancias = []
    aux = 1
    for index in range(len(texto_codificado)):
        seccion_texto = texto_codificado[index:index + largo]
        if seccion_texto == nomio:
            lista_distancias.append(aux)
            aux = 1
        else:
            aux += 1

    diccionario_nomios[nomio] = lista_distancias


print(diccionario_nomios)
