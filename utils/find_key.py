from fuzzywuzzy import fuzz

from utils.vigenere import decode, get_key, sort_by_frecuency


def find_key(texto, largo_clave, lang):

    langs = {'ESP': 'SRNDLC',
             'ENG': 'ETAIONSHRDLUCM'}

    frecuent_letters = langs[lang][:6]

    # separa el texto en chuncks de tamaño largo_clave
    chuncks = [[letra for index, letra in enumerate(texto) if (index) % (
        largo_clave) == numero] for numero in range(largo_clave)]

    # limpio chuncks vacios
    chuncks = [chunck for chunck in chuncks if chunck]

    # busco frecuencia
    possible_key = ''
    for chunck in chuncks:
        sorted_chunck = sort_by_frecuency(chunck)[:len(frecuent_letters)]

        max_similarity = 0
        best_match = ''
        for frec_letter, _ in sorted_chunck:
            for frecuent_letter in frecuent_letters:
                possible_key_letter = get_key(frec_letter, frecuent_letter)
                letters = [letter for letter, _ in sorted_chunck]
                letters = ''.join(
                    map(lambda x: decode(x, possible_key_letter)[1], letters))
                ratio = fuzz.ratio(''.join(letters), frecuent_letters)

                if ratio > max_similarity:
                    max_similarity = ratio
                    best_match = possible_key_letter

        possible_key += best_match

    return possible_key
