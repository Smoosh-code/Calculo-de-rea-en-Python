# Paso 1: Solicitar al usuario el radio del círculo
import math
from re import escape


radio = float(input("Por favor, ingrese el radio del círculo: "))


# Paso 2: Vamos a calcular el área del círculo utilizando la formula: area = π * radio^2

area = math.pi * (radio**2)

# Paso3: Mostrar al usuario el área calculada.

print("El área del círculo con radio", radio, "es:", area)
