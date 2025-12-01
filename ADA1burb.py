def burbuja(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j].lower() > lista[j + 1].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print("ORDENAR NOMBRES DE ESTUDIANTES")
cantidad = int(input("¿Cuántos nombres vas a ingresar? "))
nombres = []

for i in range(cantidad):
    nombre = input(f"Nombre {i+1}: ")
    nombres.append(nombre)
print("\nLista original:")
print(nombres)
ordenada = burbuja(nombres)
print("\nLista ordenada alfabéticamente:")
print(ordenada)
