import os
import random
os.system("cls")

longitud = int(input("Longitud de la contraseña: "))

if longitud < 4:
    print("Error: Mínimo 4 caracteres.")
else:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    contraseña = ""
    
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    
    print(f"Contraseña: {contraseña}")