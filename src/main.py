from song_maker import reproducir

sonido = input('Ingrese un sonido: ')

cancion = reproducir(sonido)

if __name__ == "__main__":
    if cancion != None:
        print("\n".join(cancion))
    else:
        print('Sonido no reconocido')