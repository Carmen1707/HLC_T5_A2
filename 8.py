Base = int(input("introduzca la base del tríangulo:" ))
Altura = int(input("Introduzca la altura del tríangulo:" ))
Precio=int(input("Introduzca el precio por metro cuadrado:" ))

Area=(Base*Altura/2)
Ct = Area*Precio
print(Area,"metros cuadrados" , "Costo total=", Ct)