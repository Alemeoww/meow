#num=int(input("ingresa un numero: "))


#for i in range(1,11):
    #print(num, "x" , i, "=", i*num)

cantA=int(input("ingresa numero de alumnos"))

for j in range(cantA):
    cantN=int(input("ingrese el numero de notas del alumno", j+1))
    suma=0
    for i in range(cantN):
        print("ingrese nota ", i+1) "del alumno ", j+1, ("use valores decimales")
        nota=float(input())
        suma+=nota
        #suma=suma+nota
    prom=suma/cantN
    print("el promedio es ", prom)
    if prom>=4:
        print("usted aprobó")
    else:
        print("usted reprobó")