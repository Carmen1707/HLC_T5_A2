def check_chars():
    word = input("Introduce la palabra:")

    for char in word:
        if "@" == char:
            print("la palabra tiene el caracter @")
        if "#" == char:
            print ("La palabra tiene el caracter #")
        if "$" == char:
            print ("La palabra tiene el caracter $")
        if "%" == char:
            print ("La palabra tiene el caracter %")
check_chars()
