import os
os.system("cls")

n = int(input("¿Cuántos números de Fibonacci deseas generar? "))

if n <= 0:
    print("Error: Ingresa un número positivo.")
else:
    fibonacci = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    
    print(f"Primeros {n} números:")
    print(fibonacci)