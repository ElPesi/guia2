nombres = []  

while True:
    nombre = input("Ingresa un nombre (o 'fin' para terminar): ")

    if nombre.lower() == "fin": 
        break

    nombres.append(nombre) 


contador = sum(1 for nombre in nombres if nombre[0].lower() in ['a', 'e'])

print("Lista de nombres ordenada:")
for nombre in nombres:
    print(nombre)

print(f"Cantidad de nombres que comienzan con 'A' o 'E': {contador}")

buscar = input("Ingresa un nombre para buscar en la lista: ")

if buscar in nombres:
    print(f"{buscar} está en la lista.")
else:
    print(f"{buscar} no está en la lista.")
