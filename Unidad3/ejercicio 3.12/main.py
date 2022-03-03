numero = int(input("Escribe un número entero o escribe -1 para detener"))
mayor = -99999

while numero != -1:  # Mientras sea True
    if numero > mayor:
        mayor = numero

    numero = int(input("Escribe otro número o -1 para detener"))

print("El número mayor fue", mayor)
