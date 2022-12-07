print("Los estudiantes pagan mensualidades acorde a su carrera y reciben descuetos segun su promedio de notas")
Carrera=input("Ingrese la carrera del estudiante (Ingeniería de Sistemas[S], Industrial[I] o de Transportes [T]):")
Promedio=input("Ingrese promedio de notas del estudiante:")
Promedio=float(Promedio)

if (Carrera=="S"):
   Mensualidad=1500
elif (Carrera=="I"):
   Mensualidad=1800
elif (Carrera=="T"):
   Mensualidad=1200

if (Promedio<11):
   Descuento=0*Mensualidad
elif (Promedio>=11 and Promedio<=14):
   Descuento=0.05*Mensualidad
elif (Promedio>=15 and Promedio<=18):
   Descuento=0.20*Mensualidad
elif (Promedio>18):
   Descuento=0.50*Mensualidad

Pagototal=Mensualidad-Descuento

print("La mensualidad es:",Mensualidad)
print("El descuento es:",Descuento)
print("El pago total es:",Pagototal)