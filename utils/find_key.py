from utils.vigenere import get_key, sort_by_frecuency



def find_key(texto, largo_clave, lang):

    langs = {'ESP':'SRNDLC',
             'ENG':'ETAIONSH'}

    frecuent_letters = langs[lang]

    # separa el texto en chuncks de tamaño largo_clave
    chuncks = [[letra for index, letra in enumerate(texto) if (index)%(largo_clave) == numero] for numero in range(5)]  

    # limpio chuncks vacios
    chuncks = [chunck for chunck in chuncks if chunck]

    # busco frecuencia
    possible_key = ''
    for chunck in chuncks:
        sorted_chunck = sort_by_frecuency(chunck)
        most_frec_letter, _  = sorted_chunck[0]
        possible_key_letter = get_key(most_frec_letter, frecuent_letters[0])
        
        possible_key+=possible_key_letter

    return possible_key

if __name__ == '__main__':
    # with open()
    pass
