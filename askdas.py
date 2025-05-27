total = 0

while True:
    print("""
    =====Menú=====
    1.- Bebidas
    2.- Postres
    3.- Almuerzos
    4.- Salir""")
    
    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            while True:
                op = int(input("""
                =====Bebidas=====
                Ingrese su opción
                1.- Coca cola $1200
                2.- Pepsi $1000
                3.- Salir
                Ingrese su opción: """))
                
                if op == 1:
                    total += 1200
                    print(f"Total acumulado: ${total}")
                elif op == 2:
                    total += 1000
                    print(f"Total acumulado: ${total}")
                elif op == 3:
                    break  # Regresa al menú principal
                else:
                    print("Opción no válida, intente de nuevo")
        
        case 2:
            while True:
                op = int(input("""
                =====Postres=====
                Ingrese su opción
                1.- Helado de fresa $500
                2.- Helado de mora $550
                3.- Salir
                Ingrese su opción: """))
                
                if op == 1:
                    total += 500
                    print(f"Total acumulado: ${total}")
                elif op == 2:
                    total += 550
                    print(f"Total acumulado: ${total}")
                elif op == 3:
                    break  # Regresa al menú principal
                else:
                    print("Opción no válida, intente de nuevo")

        case 3:
            while True:
                op = int(input("""
                =====Almuerzos=====
                Ingrese su opción
                1.- Puré con pollo $1500
                2.- Arroz con vienesa $1200
                3.- Salir
                Ingrese su opción: """))
                
                if op == 1:
                    total += 1500
                    print(f"Total acumulado: ${total}")
                elif op == 2:
                    total += 1200
                    print(f"Total acumulado: ${total}")
                elif op == 3:
                    break  # Regresa al menú principal
                else:
                    print("Opción no válida, intente de nuevo")
        
        case 4:
            print(f"Saliendo... El total es: ${total}")
            break  # Termina el programa
        case _:
            print("Opción no válida. Intente de nuevo.")
