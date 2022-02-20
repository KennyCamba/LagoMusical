from tda.linked_list import LinkedList

rana = ['brr', 'birip', 'brrah', 'croac']
libelula = ['fiu', 'plop', 'pep']
grillo = ['cric-cric', 'trri-trri', 'bri-bri']

cancion1 = LinkedList()
cancion1.add(rana[0])
cancion1.add(libelula[0])
cancion1.add(grillo[0])
cancion1.add(rana[2])

cancion2 = LinkedList()
cancion2.add(libelula[2])
cancion2.add(rana[1])
cancion2.add(grillo[1])
cancion2.add(rana[3])

cancion3 = LinkedList()
cancion3.add(grillo[2])
cancion3.add(libelula[1])
cancion3.add(grillo[0])
cancion3.add(rana[2])

canciones = [cancion1, cancion2, cancion3]


def reproducir(sonido):
    for cancion in canciones:
        if cancion.contains(sonido):
            salida = []
            while cancion.next(sonido) != None:
                sonido = cancion.next(sonido)
                salida.append(sonido)
            return salida 
    return None