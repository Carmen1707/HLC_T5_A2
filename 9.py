import random

numero = random.randint(1, 50)

for _ in range(5):
    intento = int(input("Adivine el valor (Del 1 al 50): "))
    if intento == numero:
        print("¡Adivinaste!")

    elif intento < numero :
        print("El número es mayor.")
    
    elif intento > numero :
        print("El número es menor.")

    else:
        print("Intenta de nuevo.")