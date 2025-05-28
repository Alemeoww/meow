usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None
correo= None

def usuarios_registrados():
    return any ([usuario1, usuario2, usuario3])

while True:
        men_principal=int(input("""
        1.- Iniciar Sesión
        2.- Registrar usuario
        3.- Salir
        Ingrese una opción: """))
        match men_principal:
            case 1:
                while True:
                    if not usuarios_registrados():
                        print("No hay usuarios registrados, registre uno antes de iniciar.")
                        break
                    op_sub=int(input("""
        1.- Realizar llamadas
        2.- Enviar correo electronico
        3.- Cerrar sesión
        Ingrese una opción: """))
                    if op_sub == 1:
                        while True:
                            num=input("Ingrese un numero a llamar")
                            if len(num) != 9:
                                print("El número debe tener 9 digitos")
                                continue
                            valido = True
                            for caracter in num:
                                if caracter not in "0123456789":
                                    valido = False
                                    break
                            if not valido:
                                print("Solo pueden ser digitos")
                                continue
                            if num[0] != "9":
                                print("el numero debe comenzar con 9")
                                continue
                            print("numero valido, llamando...")
                            break
                    elif op_sub == 2:
                        while True:
                            correo=input("ingrese un correo")
                            if "@" not in correo:
                                print("correo invalido, debe contener '@'")
                                continue
                            mensaje=input("escriba un mensaje: ")
                            print("enviando mensaje...")
                            print("mensaje enviado con exito")
                            break
                    elif op_sub == 3:
                        break
                    else:
                        print("opción invalida")
            case 2:
                nuevo_usuario = input("ingrese su usuario: ")
                nueva_contra = input("ingrese su contraseña: ")
                
                if usuario1 is None:
                    usuario1 = nuevo_usuario
                    contrasena1 = nueva_contra
                elif usuario2 is None:
                    usuario2 = nuevo_usuario
                    contrasena1 = nueva_contra
                elif usuario3 is None:
                    usuario3 = nuevo_usuario
                    contrasena3 = nueva_contra
                else: 
                    print("Limite de usuarios alcanzados")
                print("Usuario registrado con exito")
            case 3:
                print("Saliendo")
                break
            case _:
                print("Opción invalida, ingrese nuevamente")