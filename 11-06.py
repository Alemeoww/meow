# # uso y ejemplos de listas
# # que es una lista? 
# # es una coleccion de datos

# #     -6 -5 -4 -3 -2 -1
# numeros=[4, 3, 8,9,66,41]
# #      0  1  2 3  4 5

# # print(numeros.insert(3,1000))
# # print(numeros)
# # numeros.remove(66)
# # print(numeros)
# # numeros.sort()
# # print(numeros)

# # print(numeros)41

# # numeros.append(20)
# # print(numeros)


# # for numero in numeros:
# #     print("numero" ,numero*2)

# # frutas=["Manzana", "Frambueza", "Durazno"]

# # for fruta in frutas:
# #     print(fruta)

# # Shigeuru, Hideki, Hideo

# # Miyamoto, Anno, Kojima

# # Shigeru Miyamoto
# # Hideki Anno
# # Hideo Kojima





# # nombres=["Adolf"]
# # apellidos=["Musolini"]
# # while True:
# #     print('''
# #         1.- Insertar nombre y apellido
# #         2.- Buscar Nombre
# #         3.- Mostar Nombres y apellidos
# #         2.- Salir
# #           ''')
# #     op=int(input("Seleccione una opcion: "))
# #     match op:
# #         case 1:
# #             nom=input("Ingrese un nombre")
# #             nombres.append(nom)
# #             ape=input("Ingrese un nombre")
# #             apellidos.append(ape)
# #             print(apellidos)
# #         case 2:
# #             buscar=input("Ingrese el nombre a buscar")
# #             if buscar in nombres:
# #                 print(f"El nombre {buscar} se encuentra en la lista")
# #             else:
# #                 print(f"El nombre {buscar} NO se encuentra en la lista")
# #         case 3:
# #             cont=0
# #             for i in nombres:
# #                 print(cont+1, ".-", nombres[cont], apellidos[cont])
# #                 cont+=1
# #         case 4:
# #             print("Saliendo...")
# #             break
# #         case _:
# #             print("Opcion invalida")


# productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
# precios=[70000, 30000, 15000]
# carrito=[]

# while True:
#     print('''
#         1.- Ingresar productos a la tienda
#         2.- Comprar
#         3.- Crear Boleta
#         4.- Salir
#           ''')
#     op=int(input("Ingese una opcion: "))
#     match op:
#         case 1:
#             nom=input("Ingrese un Producto: ")
#             productos.append(nom)
#             ape=int(input("Ingrese un Precio: "))
#             precios.append(ape)
#         case 2:
#                 for i in range(3):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")
#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")
    

# '''
# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir
# '''
notas=[]
while True:
    print('''
        1.- Ingresar nota
        2.- Borrar nota
        3.- Mostrar notas
        4.- Sacar promedio, nota mayor y nota menor
        5.- Limpiar todas las notas
        6.- Salir
    ''')
    op = int(input("Seleccione una opción: "))
    
    match op:
        case 1:
            nota = float(input("Ingrese una nota(0.0 a 7.0): "))
            notas.append(nota)
            print(f"Nota {nota} agregada.")
        case 2:
            if notas:
                nota = float(input("Ingrese la nota a borrar: "))
                if nota in notas:
                    notas.remove(nota)
                    print(f"Nota {nota} borrada.")
                else:
                    print(f"La nota {nota} no se encuentra en la lista.")
            else:
                print("No hay notas para borrar.")
        case 3:
            if notas:
                print("Notas ingresadas:")
                for i, nota in enumerate(notas, start=1):
                    print(f"{i}. {nota}")
            else:
                print("No hay notas para mostrar.")
        case 4:
            if notas:
                promedio = sum(notas) / len(notas)
                nota_mayor = max(notas)
                nota_menor = min(notas)
                print(f"Promedio: {promedio:.2f}")
                print(f"Nota mayor: {nota_mayor}")
                print(f"Nota menor: {nota_menor}")
            else:
                print("No hay notas para calcular.")
        case 5:
            notas.clear()
            print("Todas las notas han sido limpiadas.")
        case 6:
            print("Saliendo del programa.")
            break
        case _:
            print("Opción inválida, intente de nuevo.")