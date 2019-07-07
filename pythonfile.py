import random
intentos_realizados = 0
print("Como te llamas?")
miNombre = input()

numero = random.randint(1, 20)
print('OK, '  + miNombre +  " estoy pensando en un numero entre 1 y 20 ")

while intentos_realizados < 6:
    print("intenta Adivinar")
    estimacion = input()
    estimacion = int(estimacion)

    intentos_realizados = intentos_realizados + 1

    if estimacion < numero:
         print("Tu estimacion es muy baja")

    if estimacion > numero:
        print("Tu estimacion es muy alta")

    if  estimacion == numero:
        break
if estimacion == numero:
    intentos_realizados = str(intentos_realizados)
    print("ok" + miNombre +" Adivinaste en " + intentos_realizados + "intentos")

if estimacion != numero:
    numero = str(numero)
    print("Error, No era el numero que pensaba " +  numero)


