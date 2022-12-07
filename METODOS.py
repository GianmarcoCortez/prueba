def Saludar():
   print("Hola mundo!") 

def CalcularDoble(num):
   res=num*2
   return res 

def Triplicar(num):
   res=num*3
   return res 


print("Llamada a la funcion Saludar:")
Saludar()

x=input("Ingrese un valor numérico para x:")
x=int(x)
print("Llamada a la función CalcularDoble (pasaje por valor)")
print("El doble de ",x," es ", CalcularDoble(x))
print("El valor original de x es ",x)

print("Llamada a la función Triplicar (pasaje por referencia)")
print("El nuevo valor de x es ",Triplicar(x))

