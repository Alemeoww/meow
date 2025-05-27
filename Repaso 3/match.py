
total = 0

while  True:
    opcion = int(input("""
    =====Menú=====
    1.- Bebidas
    2.- Postres
    3.- Almuerzos
    4.- Ver total
    Ingrese una opción: """))

    match opcion:
        case 1:
            while True:
                op=int(input(f"""
                    =====Bebidas=====
                    Ingrese su opción
                    1.- Coca cola $1200
                    2.- Pepsi $1000
                    3.- Salir
                    Total acumulado: ${total}
                    Ingrese su opción: """))
                if op == 1:
                    total += 1200
                elif op == 2:
                    total += 1000
                elif op == 3:
                    break
                else:
                    print("Opción no válida, intente de nuevo")
        case 2:
            while True:
                op=int(input(f"""
                    =====Postres=====
                    Ingrese su opción
                    1.- Helado de vainilla $1700
                    2.- Helado de mora $1750
                    3.- Salir
                    Total acumulado: ${total}
                    Ingrese su opción: """))
                if op == 1:
                    total += 1700
                elif op == 2:
                    total += 1750
                elif op == 3:
                    break
                else:
                    print("Opción no válida, intente de nuevo")
        case 3:
            while True:
                op=int(input(f"""
                    ====Almuerzos====
                    1.- Puré con pollo $2600
                    2.- Arroz con vienesa $2250
                    3.- Salir
                    Total acumulado: ${total}
                    Ingrese su opción: """))
                if op == 1:
                    total += 2600
                elif op == 2:
                    total += 2250
                elif op == 3:
                    break
                else:
                    print("Opción no válida, intente de nuevo")
        case 4:
            print("el total es: ", total)
            break