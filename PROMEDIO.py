n=input("Ingrese la cantidad de datos:")
n=int(n)
acum=0
for i in range(n):
    dato=input("Ingrese el dato:")
    dato=int(dato)
    acum=acum+dato
prom=acum/n
print("El promedio es: ",prom)