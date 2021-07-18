from string import ascii_uppercase
from math import ceil

def encode(mensaje, clave):
    alfabeto = ascii_uppercase
    final = ''

    clave = clave*ceil(len(mensaje)/len(clave))

    for clv, msg in zip(clave, mensaje):
        index_clv = alfabeto.find(clv)
        index_msg = alfabeto.find(msg)
        
        final += alfabeto[(index_clv+index_msg)%len(alfabeto)]

    return final


def decode(mensaje, clave):
    alfabeto = ascii_uppercase
    final = ''

    clave = clave*ceil(len(mensaje)/len(clave))

    for clv, msg in zip(clave, mensaje):
        index_clv = alfabeto.find(clv)
        index_msg = alfabeto.find(msg)
        
        final += alfabeto[(index_msg-index_clv)%len(alfabeto)]

    return final

def get_key(encr_letter, deencr_letter):
    alfabeto = ascii_uppercase

    diff = alfabeto.find(encr_letter)-alfabeto.find(deencr_letter) 
    diff = (diff+len(alfabeto))%len(alfabeto)

    return alfabeto[diff]
    

if __name__ == '__main__':
    print(ascii_uppercase)
    en_txt = encode('HOLA', 'AEXO')
    txt = decode(en_txt, 'AEXO')

    print(get_key(en_txt[0], txt[0]))


#A -> B

