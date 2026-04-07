import os
os.system("cls")

contraseña = input("Crea una contraseña: ")

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = any(c.isupper() for c in contraseña)
tiene_minuscula = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
tiene_especial = any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for c in contraseña)

print(f"Longitud (≥8): {'✓' if tiene_longitud else '✗'}")
print(f"Mayúscula: {'✓' if tiene_mayuscula else '✗'}")
print(f"Minúscula: {'✓' if tiene_minuscula else '✗'}")
print(f"Número: {'✓' if tiene_numero else '✗'}")
print(f"Carácter especial: {'✓' if tiene_especial else '✗'}")

if all([tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial]):
    print("\n✓ Contraseña válida")
else:
    print("\n✗ Contraseña no válida")