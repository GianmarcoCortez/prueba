import random

A=[]
for i in range(0,10,1):
    elemento =random.randint(1,100)
    A.append(elemento)
print("Los elementos del arreglo son:")
print(A)
print("")

print("En orden inverso:")
for i in reversed(A):
    print(i, end=" ")

