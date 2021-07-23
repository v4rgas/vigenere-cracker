from collections import defaultdict
from functools import reduce
from itertools import combinations
from math import gcd

from utils.vigenere import sort_by_frecuency


def nomio_finder(texto_codificado: str, length: int):
    nomio_dict = defaultdict(list)
    for index in range(len(texto_codificado)):
        nomio_dict[texto_codificado[index: index + length]].append(index)
    return nomio_dict

# Recibe el path del texto codificado y returna una lista con la (DISTANCA, FRECUENCIA)


def gcd_method(texto_codificado):
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


def coincidence_index(group_letters: list) -> float:

    N = len(group_letters)
    if N <= 1:
        return 0

    dictionary_letters = defaultdict(int)
    for letter in group_letters:
        dictionary_letters[letter] += 1

    numerator = 0
    for frecuency in dictionary_letters.values():
        numerator += frecuency * (frecuency - 1)

    return (numerator / (N * (N - 1)))


def cindex_method(texto_codificado):
    cantidad_grupos = len(texto_codificado)+1

#     grupos = [[[] for _ in range(grupo)]
#               for grupo in range(cantidad_grupos)]
#
#     for index_letra, letra in enumerate(texto_codificado):
#         for grupo in range(cantidad_grupos):
#             for index in range(grupo):
#                 if index_letra % grupo == index:
#                     grupos[grupo][index].append(letra)

    indices_coincidencia = {}
    for grupo in range(1, cantidad_grupos):
        indices_coincidencia[grupo] = sum(
            coincidence_index(texto_codificado[index::grupo]) for index in range(grupo))/grupo

    print(indices_coincidencia)
    # grupos = grupos[1:]

    # indices_coincidencia = {}
    # for grupo in grupos:
    # indices_coincidencia[len(grupo)] = sum(
    #     coincidence_index(subgrupo) for subgrupo in grupo)/len(grupo)

    for key in indices_coincidencia.keys():
        if indices_coincidencia[key + 1] / indices_coincidencia[key] > 1.45:
            return key + 1


def find_length(texto_codificado, method='cindex'):
    if method == 'cindex':
        return cindex_method(texto_codificado)
    elif method == 'gcd':
        return gcd_method(texto_codificado)
