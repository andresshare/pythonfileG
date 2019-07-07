import  random

IMAGENES_AHORCADO = [''' 

+----+
|    |
O    |
     |
     |
     |
====== ''','''
+----+
|    |
O    |
|    |
     |
     |
====== ''','''
                     
 +----+
 |    |
 O    |
/|    |
      |
      |
====== ''','''

 +----+
 |    |
 O    |
/|\   |
      |
      |
====== ''','''

+----+
 |    |
 O    |
/|\   |
/     |
      |
====== ''','''

+----+
 |    |
 O    |
/|\   |
/ \   |
      |
====== ''']

palabras = 'hormiga babuino tejon murcielago oso castor camello ' \
           'gato almeja cobra pantera coyote cuervo ciervo perro ' \
           'burro pato aguila huron zorro rana cabra ganso halcon ' \
           'leon lagarto llama topo mono alce raton mula salamandra ' \
           'nutria buho panda loro paloma piton conejo carnero ' \
           'rata cuervo rinoceronte salmon foca tiburon oveja ' \
           'mofeta perezoso serpiente araña cigüeña cisne tigre ' \
           'sapo trucha pavo tortuga comadreja ballena ' \
           'lobo wombat cebra'.split()


def Obtenerpalabraalazar(listadepalabras):
    indicedepalabras = random.randint(0, len(listadepalabras)-1)
    return listadepalabras[indicedepalabras]


def mostrartablero(IMAGENES_AHORCADO, letrasincorrectas, letrascorrectas, palabrasecreta):
    print(IMAGENES_AHORCADO[len(letrasincorrectas)])
    print()

    print("letras incorrectas:", end= " " )
    for letra in letrasincorrectas:
        print(letra, end = " ")
        print()
    espaciosvacios = "" * len(palabrassecreta)

    for i in range(len(palabrasecreta)):
        if palabrasecreta[i] in letrascorrectas:
            espaciosvacios = espaciosvacios[:i] + palabrasecreta[i] + espaciosvacios = espaciosvacios[i + 1:]

    for letra in espaciosvacios:
        print(letra, end="")
        print()

def obtenerIntento(letrasProbadas):
    while True:
        print("adivina una letra")
        intento = input()
        intento = intento.lower()
        if len(intento) !=1:
            print("Por favor introduce una letra")
        elif intento in letrasprobadas:
            print("ya has probado esa letra, prueba otra!! ")
        elif intento not  in "abcdefghijklmnñopqrstuvwxyz":
            print("por favor ingresa  una letra")
        else:
            return intento
    def jugardenuevo():
        print("Quieres jugar de nuevo? (si /no)")
        return input().lower().startswith('s')

    print("A H O R C A D O")
    letrasincorrectas = ""
    letrascorrectas =""
    palabrasecreta =  obtenerpalabraalazar(words)
    juegoterminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO,letrasincorrectas,letrascorrectas,palabras)
    intento = obtenerintento(letrasincorrectas + letrascorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

encontradoTodasLasLetras = True
for i in range(len(palabraSecreta)):
    if palabraSecreta[i] not in letrasCorrectas:
        encontradoTodasLasLetras = False
        break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
        else:
            letrasIncorrectas = letrasIncorrectas + intento
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) -1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' +
                  str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break


