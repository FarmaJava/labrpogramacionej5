import os
import random
os.system("cls")

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("He pensado un número entre 1 y 100. ¡Adivina cuál es!")

while not adivinado:
    adivinanza = int(input("Ingresa tu adivinanza: "))
    intentos += 1
    
    if adivinanza < 1 or adivinanza > 100:
        print("Por favor, ingresa un número entre 1 y 100.")
        continue
    
    if adivinanza < numero_secreto:
        print("El número es MÁS ALTO.")
    elif adivinanza > numero_secreto:
        print("El número es MÁS BAJO.")
    else:
        adivinado = True
        print(f"¡Correcto! ¡Adivinaste el número {numero_secreto}!")
        print(f"Intentos: {intentos}")