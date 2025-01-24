def estrellas():
    cantidad_estrellas = int(input("Ingrese la cantidad de estrellas: "))
    for i in range(1 ,cantidad_estrellas + 1):
        print("★"*i)

    return None

estrellas()
