import random
import time

def mostrarIntroduccion():
    print('Estás en una tierra llena de dragones. Frente a tí')
    print('hay dos cuevas. En una deellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()

def elegirCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print("puerta que quieres entrar?(1 o 2)")
        cueva = input()
    return cueva


def explorarcueva(cuevaElegida):
    print("Te acercas a la cueva....")
    time.sleep(2)
    print("Es oscura y espeluznante")
    time.sleep(2)
    print("Un gran dragon  aparece subitamente frente a ti! Abre su Boca")
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida ==str(cuevaAmigable):
        print("Te regala su tesoro")
    else:
        print("Te come de un solo bocado")


jugardeNuevo = 'si'
while jugardeNuevo == 'si' or jugardeNuevo == "s":
    mostrarIntroduccion()
    numerodecueva = elegirCueva()
    explorarcueva(numerodecueva)
    print("Quiere jugar de nuevo(si,no)")
    jugardeNuevo = input()


