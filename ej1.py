import os
os.system("cls")

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en cm: "))
    
if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser positivos.")
else:
    imc = peso / ((altura / 100) ** 2)
    # Categorización por talla
if imc < 18.5:
    categoria = "Talla XS (Bajo peso)"
elif 18.5 <= imc < 25:
    categoria = "Talla S (Peso normal)"
elif 25 <= imc < 30:
    categoria = "Talla M (Sobrepeso)"
elif 30 <= imc < 35:
    categoria = "Talla L (Obesidad I)"
else:
    categoria = "Talla XL (Obesidad II)"
    
print(f"Tu IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")
