#num=int(input("ingresa un numero: "))


#for i in range(1,11):
    #print(num, "x" , i, "=", i*num)

#cantA=int(input("ingresa numero de alumnos"))

#for j in range(cantA):
#    cantN=int(input("ingrese el numero de notas del alumno", j+1))
#    suma=0
#    for i in range(cantN):
#        print("ingrese nota ", i+1) "del alumno ", j+1, ("use valores decimales")
#        nota=float(input())
#        suma+=nota
#        #suma=suma+nota
#   prom=suma/cantN
#   print("el promedio es ", prom)
#   if prom>=4:
#       print("usted aprobó")
#   else:
#       print("usted reprobó")

#num=int(input("ingrese un numero "))

#if num % 2==0:
#    print("el numero",num," es par")
#else:
#    print("el numero",num," es impar")

#designe 2 votantes. Pida la cantidad de votantes
#pida el vodo a cada votante y muestre los resultados
#verifique quien ganó. Considera un empate


#La florida 20%, la pintana 30%, puente alto 25%, San Joaquin 15%
#Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
#preguntar al usuario en que comuna vivve
#preguntar al usuario con cuantas personas vive
#el arancel actual es de 200.000 por semestre
#Basados en las respuestas del usuario y en
#la informacion dada, calcular su descuento

descuento_comun={
    "la florida":0.20,
    "la pintana":0.30,
    "puente alto":0.25,
    "san joaquin":0.15
}
comuna = input("¿En qué comuna vive? ").strip().lower()

personas=int(input("con cuantas personas vive?"))

arancel=200000

desc1=descuento_comun.get(comuna, 0)

if personas==1:
    desc2=0.02
elif 2<=personas<=4:
    desc2=0.03
else:
    desc2=0.04

descuento_total=desc1+desc2
descuento_final=arancel*descuento_total
total_pagar=arancel-descuento_final

print("descuento total aplicado:", descuento_total*100,"%")
print("monto a pagar:$", total_pagar)