#Iram Jimenez NC = 0079
print("====================")
print("1. Función simple sin parámetros")
print("====================")

def saludo():
    print("¡Hola! Te damos la bienvenida a Python")

saludo()

print("====================")
print("2. Función con parámetros")
print("====================")

def bienvenido(nombre):
    print("Hola", nombre, "¡mucho gusto!")

bienvenido("Sofia")

print("====================")
print("3. Función con valor por defecto")
print("====================")

def mi_funcion(nombre, apellido="Desconocido"):
    print("Nombre:", nombre, "| Apellido:", apellido)

mi_funcion("Valeria")
mi_funcion("Mateo", "Gómez")

print("====================")
print("4. Función que devuelve un valor (return)")
print("====================")

def multiplicar(a, b):
    return a * b

resultado = multiplicar(8, 9)
print("El resultado de la multiplicación es:", resultado)

print("====================")
print("5. Retornar múltiples valores")
print("====================")

def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(15, 6)
print("Suma:", s)
print("Resta:", r)
print("Iram Jimenez NC = 0079")