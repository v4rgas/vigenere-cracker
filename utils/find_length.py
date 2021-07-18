from utils.vigenere import sort_by_frecuency
from collections import defaultdict
from itertools import combinations
from math import gcd
from functools import reduce

def nomio_finder(texto_codificado: str, length: int):
    nomio_dict = defaultdict(list)
    for index in range(len(texto_codificado)):
        nomio_dict[texto_codificado[index: index + length]].append(index)
    return nomio_dict

# Recibe el path del texto codificado y returna una lista con la (DISTANCA, FRECUENCIA)
def find_lenght(texto_codificado):
    lista_ordenada = nomio_finder(texto_codificado, 3)
    lista_ordenada.update(nomio_finder(texto_codificado, 2))

    indexes_distance = []
    for indexes in lista_ordenada.values():
        indexes_distance.extend([indexes[index + 1] - indexes[index]
                                for index in range(len(indexes) - 1)])

    indexes_distance = sort_by_frecuency(indexes_distance)[:15]
    divisores = []

    lista_distancias = [tupla[0] for tupla in indexes_distance]

    for index in range(2, len(lista_distancias)):
        for combination in combinations(lista_distancias, index):
            divisores.append(reduce(gcd, combination))
    
    return sort_by_frecuency(divisores)
    