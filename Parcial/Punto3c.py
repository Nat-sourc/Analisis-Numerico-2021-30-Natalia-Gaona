import numpy as np

#Realizado por: Natalia Gaona Salamanca

gx= lambda x: x**3-2*x-5

a=-5
b=1
tolerancia=1e-5
iteramax=15
i=1 #procedimiento
b=gx(a)
tramo=abs(b-a)
while not(tramo<=tolerancia or i>=iteramax):
    a=b
    b=gx(a)
    tramo = abs(b - a)
    i=i+1
respuesta=b
#validar convergencia
if(i>=iteramax):
        respuesta=np.nan#no fue un numero aceptable
print(respuesta)
print(i)
print(tramo)