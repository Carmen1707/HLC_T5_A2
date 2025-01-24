n1 = int(input("Introduce el primer numero:"))
n2 = int(input("Introduce el segundo numero:"))
n3 = int(input("Introduce el tercer numero:"))

#Parte de los numeros introducidos 

print ("Los numeros son " ,n1 ,n2 , n3)

#Parte de mayor 
if n1 > n2 and n1 > n3: #ver si el 1 es mayor que el 2 y 3 si pues si imprime en pantalla 
    print("El mayor es el primer número:")
elif n2 > n1 and n2 > n3: #ver si el 2 es mayor que el 1 y 3 
    print("El mayor es el segundo número:")
elif n3 > n1 and n3 > n2:
    print("El mayor es el tercer número:")
#Parte de los iguales
    if n1 == n2 and n1 == n3:
        print("Los tres números son iguales")