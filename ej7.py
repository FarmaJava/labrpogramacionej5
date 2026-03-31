import os
os.system("cls")

precio_original = float(input("Ingresa el precio original ($): "))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (%): "))

if precio_original <= 0 or porcentaje_descuento < 0:
    print("Error: Los valores deben ser positivos.")
else:
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    
    print(f"\nPrecio original: ${precio_original:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Precio final: ${precio_final:.2f}")