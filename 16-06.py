# def suma():
#     n1=int(input("introduce un numero: "))
#     n2=int(input("introduce otro numero: "))
#     print(n1+n2)

# def resta():
#     n1=int(input("introduce un numero: "))
#     n2=int(input("introduce otro numero: "))
#     print(n1-n2)

#suma()

# num1=int(input("ingrese un numero: "))
# num2=int(input("ingrese otro numero: "))
# resta(num1, num2)

# def suma(n1, n2):
#     print(n1 + n2)
# def resta(n1, n2):
#     print(n1 - n2)
# def multiplicacion(n1, n2):
#     print(n1 * n2)
# def division(n1, n2):
#     print(n1 / n2)

# n1=int(input("ingrese un numero: "))
# n2=int(input("ingrese otro numero: "))
# suma(n1, n2)
# resta(n1, n2)
# multiplicacion(n1, n2)
# division(n1, n2)

# def suma_print():
#     n1 = int(input("introduce un numero: "))
#     n2 = int(input("introduce otro numero: "))
#     print(n1 + n2)

# def suma_return():
#     n1 = int(input("introduce un numero: "))
#     n2 = int(input("introduce otro numero: "))
#     return n1 + n2

# suma_print()
# veri=suma_return()
# print(veri)

# def promedio(x, y, z):
#     return (x + y + z) / 3
# if promedio (40, 70, 20) >=40:
#     print("Aprobado")
# else:
#     print("Reprobado")

#crear un programa para calcular un descuento
#pedir al usuario el precio y el descuento a aplicar
#mostrar los resultados

# def calcular_descuento(precio,descuento):
#     descuento_calculado=precio*(descuento / 100)
#     precio_final=precio-descuento_calculado
#     return precio_final
# precio=float(input("Ingrese el precio del producto: "))
# descuento =float(input("Ingrese el porcentaje de descuento: "))
# precio_final =calcular_descuento(precio,descuento)
# print("El precio final después de aplicar el descuento es:",precio_final)

# productos=["zapato"]
# precio=[20000]

list_prod=[
    {"nombre":"zapato", "precio":20000},
    {"nombre":"pelota", "precio":24000}
]

# print(list_prod)

# list_prod.insert(0, {"nombre":"camisa", "precio":14000})

# print(list_prod)

while True:
    print('''
    1. Agregar producto
    2. Mostrar productos
    3. Actializar producto
    4. Salir
    ''')
    op = input("Seleccione una opción: ")
    match op:
        case 1:
            nom=input("Ingrese el nombre del producto: ")
            pre=int(input("Ingrese el precio del producto: "))
            list_prod.insert(0, {"nombre":nom, "precio":pre})
        case 2:
            for p in list_prod:
                print(p)
        case 3:
            for i in range(len(list_prod)):
                print(i+1, ".-", list_prod[i])
            opc= int(input("Seleccione el producto a actualizar: "))
            print(list_prod[opc-1])
            nn=input("seleccione el producto a actualizar: ")
            np=int(input("Ingrese el nuevo precio: "))
            list_prod[opc-1]
        case 4:
            break
        case _:
            print("Opción no válida")