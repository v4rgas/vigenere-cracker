def nomio_finder(texto_codificado: str, length: int) -> dict:
    diccionario = {}
    for index in range(0, len(texto_codificado) - (length - 1)):
        trinomio = texto_codificado[index:index + length]
        lista_llaves = list(diccionario.keys())
        if trinomio in lista_llaves:
            diccionario[trinomio] += 1
        else:
            diccionario[trinomio] = 1

    lista_aux = []
    for key in diccionario.keys():
        lista_aux.append((key, diccionario[key]))

    lista_aux = sorted(lista_aux, key=lambda x: x[1], reverse=True)

    return lista_aux, diccionario


#Recibe el path del texto codificado y returna una lista con la (DISTANCA, FRECUENCIA)
def find_lenght(texto_codificado):
    lista_ordenada_trinomio, diccionario_tri = nomio_finder(texto_codificado, 3)
    lista_ordenada_binomio, diccioanrio_bi = nomio_finder(texto_codificado, 2)

    lista_ordenada_trinomio = lista_ordenada_trinomio[0:4]
    lista_ordenada_binomio = lista_ordenada_binomio[0:4]

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

        diccionario_distancias = {}

        for key in diccionario_nomios:
            for distancia in diccionario_nomios[key]:
                if distancia in diccionario_distancias.keys():
                    diccionario_distancias[distancia] += 1
                else:
                    diccionario_distancias[distancia] = 1
        
        lista_ordenada = [item for item in diccionario_distancias.items()]
        return sorted(lista_ordenada, key=lambda x: x[1], reverse=True)
