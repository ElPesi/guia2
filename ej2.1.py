c = 0 

while True:  
    n = int(input("Ingresa un número entero positivo (o negativo para salir): "))  

    if n < 0:  
        break

    c += n  

print(f"La suma total es: {c}")
