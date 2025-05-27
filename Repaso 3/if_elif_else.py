
#(con while)

while True:
    try:
        num=int(input("ingrese un número: "))
        if num > 0:
            print("Es positivo")
        elif num == 0:
            print("Es cero")
        else:
            print("Es negativo")
    except Exception:
        print("Ingrese un número válido")
