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

#descuento_comun={
    #"la florida":0.20,
  #  "la pintana":0.30,
   # "puente alto":0.25,
 #   "san joaquin":0.15
#}
#comuna = input("¿En qué comuna vive? ").strip().lower()

#personas=int(input("con cuantas personas vive?"))

#arancel=200000

#desc1=descuento_comun.get(comuna, 0)

#if personas==1:
#    desc2=0.02
#elif 2<=personas<=4:
 #   desc2=0.03
#else:
 #   desc2=0.04

#descuento_total=desc1+desc2
#descuento_final=arancel*descuento_total
#total_pagar=arancel-descuento_final

#print("descuento total aplicado:", descuento_total*100,"%")
#print("monto a pagar:$", total_pagar)

#calcular el puntaje de credito
#debe de calcular que tanto credito tiene una persona
#en cierta entidad financiera, debera considerar
#cantidad de ingresos, nivel educacional y nacionalidad
#cantidad de ingresos
#500.000 a 1.000.000 : 300.000
#1.000.000 a 1.500.000: 650.000
#1.500.001 o mas : 1.000.000
#nivel educacional
#basico : x1, medio: 1.3, superior: 1.5
#nacionalidad
#chilena : +300.000, extranjero: +0

#pedir dia y mes de nacimiento y mostrar el signo zodiacal

#def calcular_credito(ingresos, educacion, nacionalidad):
    #if 500000 <= ingresos <= 1000000:
     #   puntaje_ingresos = 300000
    #elif 1000000 < ingresos <= 1500000:
     #   puntaje_ingresos = 650000
    #elif ingresos > 1500000:
     #   puntaje_ingresos = 1000000
    #else:
     #   puntaje_ingresos = 0

    #if educacion == 'basico':
    #    multiplicador = 1
    #elif educacion == 'medio':
    #    multiplicador = 1.3
    #elif educacion == 'superior':
    #    multiplicador = 1.5
    #else:
    #    multiplicador = 0

    #if nacionalidad == 'chilena':
     #   puntaje_nacionalidad = 300000
    #else:
   #     puntaje_nacionalidad = 0

  #  puntaje_total = (puntaje_ingresos * multiplicador) + puntaje_nacionalidad
 #   return puntaje_total


#ingresos = int(input("Ingrese sus ingresos: "))
#educacion = input("Ingrese su nivel educacional (basico, medio, superior): ").lower()
#nacionalidad = input("Ingrese su nacionalidad (chilena o extranjero): ").lower()

#puntaje = calcular_credito(ingresos, educacion, nacionalidad)
#print("Su puntaje de crédito es:", puntaje)



#crear un programa que pida la cantidad de ramos
#luego pide el promedio por cada materia
#basados en su promedio final, aplicar puntaje
#de beneficios
#4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0 : 800
# agregar puntaje segun carrera
# tecnico : +60, ingenieria: +40, diplomado: +20

