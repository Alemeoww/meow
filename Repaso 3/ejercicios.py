sw=1

while True:
    try:
        op=int(input("""
    Menú
    1.- Ver mi saldo
    2.- Retirar dinero
    3.- Salir
    Ingrese su opción: """))
        match op:
            case 1:
                while True:
                    try:
                        op=int(input(f"""
        Tiene un saldo de: $500000
        1.- Volver
        2.- Salir
        """))
                        if op == 1:
                            break
                        elif op == 2:
                            print("cierre de sesión exitoso, saliendo del sistema.")
                            exit()
                    except Exception:
                        print("Error, respuesta invalida")
            case 2:
                while True:
                    try:
                        op=int(input(f"""
        Transferencia realizada
        1.- Volver
        2.- Salir
        """))
                        if op == 1:
                            break
                        elif op == 2:
                            print("cierre de sesión exitoso, saliendo del sistema.")
                            exit()
                    except Exception:
                        print("Error, respuesta invalida")
            case 3:
                print("Cierre de sesión exitoso, adiós.")
                break
    except Exception:
        print("error, opción no valida")