from collections import defaultdict
from functools import reduce
from itertools import combinations
from math import gcd

# from utils.vigenere import sort_by_frecuency


def nomio_finder(texto_codificado: str, length: int):
    nomio_dict = defaultdict(list)
    for index in range(len(texto_codificado)):
        nomio_dict[texto_codificado[index: index + length]].append(index)
    return nomio_dict

# Recibe el path del texto codificado y returna una lista con la (DISTANCA, FRECUENCIA)


def find_length(texto_codificado):
    lista_ordenada = nomio_finder(texto_codificado, 3)
    lista_ordenada.update(nomio_finder(texto_codificado, 2))

    distances_dict = defaultdict(int)
    for indexes in lista_ordenada.values():
        for index in range(len(indexes) - 1):
            distances_dict[indexes[index + 1] - indexes[index]] += 1

    indexes_distance = sorted([(key, value) for key, value in distances_dict.items(
    )], key=lambda x: x[1], reverse=True)[:15]

    divisores = []
    lista_distancias = [tupla[0] for tupla in indexes_distance]

    for index in range(2, len(lista_distancias)):
        for combination in combinations(lista_distancias, index):
            gcd_variable = reduce(gcd, combination)
            if gcd_variable != 1:
                divisores.append(gcd_variable)

    return sort_by_frecuency(divisores)


def coincidence_index(list):
    pass


def find_length_cindex(texto_codificado):

    largo_codificado = len(texto_codificado)

    lista = []
    for cantidad_grupo in range(largo_codificado):
        grupos = [[texto_codificado[index] for index in range(
            largo_codificado) if index % cantidad_grupo == offset] for offset in range(cantidad_grupo)]

        lista.append(grupos)


if __name__ == "__main__":
    find_length_cindex('ABCDEFGHIJK')
