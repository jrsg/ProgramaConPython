numero1 = int(input("Escribe un número entero"))
numero2 = int(input("Escribe otro número entero"))

if numero1 > numero2:
    print("El número mayor es", numero1)
elif numero2 > numero1:  # otra versión: numero1 < numero2
    print("El número mayor es", numero2)
else:
    print("Son iguales")

