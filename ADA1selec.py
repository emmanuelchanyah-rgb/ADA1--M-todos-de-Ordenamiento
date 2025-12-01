def seleccion(lista):
    n = len(lista)

    for i in range(n):
        indice_menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return lista

print("ORDENAR EDADES DE PERSONAS")
cantidad = int(input("¿Cuántas edades vas a ingresar?"))

edades = []

for i in range(cantidad):
    edad = int(input(f"Edad {i+1}: "))
    edades.append(edad)

print("\nEdades originales:")
print(edades)

ordenadas = seleccion(edades)

print("\nEdades ordenadas:")
print(ordenadas)

print("\nClasificación:")
for edad in ordenadas:
    if edad < 18:
        print(edad, " Menor de edad")
    elif edad < 30:
        print(edad, " mayor de edad")
    elif edad < 60:
        print(edad, " Adulto")
    else:
        print(edad, " Adulto mayor")
