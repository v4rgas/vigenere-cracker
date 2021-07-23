from fuzzywuzzy import fuzz

from utils.vigenere import decode, get_key, sort_by_frecuency


def find_key(texto, largo_clave, lang) -> str:

    langs = {'ESP': 'SRNDLC',
             'ENG': 'ETAIONSHRDLUCM'}

    frecuent_letters = langs[lang][:6]

    # separa el texto en chuncks de tamaño largo_clave
    chuncks = [[] for _ in range(largo_clave)]
    index = 0
    for letra in texto:
        chuncks[index].append(letra)
        index = (index+1) % largo_clave

    # limpio chuncks vacios
    chuncks = [chunck for chunck in chuncks if chunck]

    # busco frecuencia
    possible_key = ''
    for chunck in chuncks:
        # Ordeno por letras mas frecuentes
        sorted_chunck = sort_by_frecuency(chunck)[:len(frecuent_letters)]

        max_similarity = 0
        best_match = ''
        for frec_letter, _ in sorted_chunck:
            for frecuent_letter in frecuent_letters:

                # Se generan posibles distribuciones asumiendo que cada una de las letras
                # mas frecuentes en el texto corresponde a
                # cada una de las letras mas frecuentes en ingles

                possible_key_letter = get_key(frec_letter, frecuent_letter)
                letters = [letter for letter, _ in sorted_chunck]
                letters = ''.join(
                    map(lambda x: decode(x, possible_key_letter)[1], letters))

                # Luego com fuzz.ratio (distancia entre strings) medimos que tan parecidas
                # son estas distribuciones a las letras más frecuentes en ingles
                ratio = fuzz.ratio(''.join(letters), frecuent_letters)

                if ratio > max_similarity:
                    # Nos quedamos con la letra que causa la distribucion más parecida
                    max_similarity = ratio
                    best_match = possible_key_letter

        # Se hace esto por cada columna, por lo que se genera la clave más probable
        possible_key += best_match

    return possible_key
