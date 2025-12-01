def insercion(lista):
 
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

print("ORDENAR PRECIOS DE PRODUCTOS")
cantidad = int(input("¿Cuántos precios vas a ingresar? "))

precios = []

for i in range(cantidad):
    precio = float(input(f"Precio {i+1}: $"))
    precios.append(precio)

print("\nPrecios originales:")
print(precios)
ordenados = insercion(precios)

print("\nPrecios ordenados de menor a mayor:")
print(ordenados)

print("\nPrecio más barato:", ordenados[0])
print("Precio más caro:", ordenados[-1])
promedio = sum(ordenados) / len(ordenados)
print("Promedio de precios:", round(promedio, 2))
