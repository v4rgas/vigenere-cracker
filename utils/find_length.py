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


# def find_length(texto_codificado):
#     lista_ordenada = nomio_finder(texto_codificado, 3)
#     lista_ordenada.update(nomio_finder(texto_codificado, 2))

#     distances_dict = defaultdict(int)
#     for indexes in lista_ordenada.values():
#         for index in range(len(indexes) - 1):
#             distances_dict[indexes[index + 1] - indexes[index]] += 1

#     indexes_distance = sorted([(key, value) for key, value in distances_dict.items(
#     )], key=lambda x: x[1], reverse=True)[:15]

#     divisores = []
#     lista_distancias = [tupla[0] for tupla in indexes_distance]

#     for index in range(2, len(lista_distancias)):
#         for combination in combinations(lista_distancias, index):
#             gcd_variable = reduce(gcd, combination)
#             if gcd_variable != 1:
#                 divisores.append(gcd_variable)

#     return sort_by_frecuency(divisores)

def coincidence_index(group_letters: list) -> float:
    dictionary_letters = defaultdict(str)
    for letter in group_letters:
        dictionary_letters[letter] += 1

    numerator = 0
    for frecuency in dictionary_letters.values():
        numerator += frecuency * (frecuency - 1)

    N = len(group_letters)

    return 26 * numerator / (N * (N - 1))


def find_length_cindex(texto_codificado):
    cantidad_grupos = len(texto_codificado)

#     lista = []
#     for cantidad_grupo in range(cantidad_grupos):
#
#         grupos = [[texto_codificado[index] for index in range(
#             cantidad_grupos) if index % cantidad_grupo == offset] for offset in range(cantidad_grupo)]
#
#         lista.append(grupos)

    grupos = [[[] for _ in range(grupo)]
              for grupo in range(cantidad_grupos)]

    for index_letra, letra in enumerate(texto_codificado):
        for grupo in range(1, cantidad_grupos):
            for index in range(grupo):
                if index_letra % grupo == index:
                    grupos[grupo][index].append(letra)

    print(grupos[6])


if __name__ == "__main__":
    find_length_cindex('ABCDEFGHIJK')
