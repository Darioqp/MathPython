#-------Hallar ternas Pitagóricas------------

from math import sqrt

c=int(input("Ingrese el maximo valor para la hipotenusa: "))

cuadrados_perfectos=[]
ternas = []

for i in range(c-1):
    
    hipotenusa=(i+2)**2
    
    cuadrados_perfectos.append(hipotenusa)

for i in cuadrados_perfectos:

    for j in cuadrados_perfectos:
        
        if j>i and i+j in cuadrados_perfectos:
            
            ternas.append((int(sqrt(i)),int(sqrt(j)),int(sqrt(i+j))))
            
for elemento in ternas:

    print(elemento)


