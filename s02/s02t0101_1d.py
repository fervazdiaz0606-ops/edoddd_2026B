# Importando el modulo arrays
from array import array as arr

#Creando un arreglo 
array_01 = arr('i', [3, 8, 5, 1, 6]) # O(n)

#Interando automatticamente 
for data in array_01: # O(n)
    print(data,end='') # O(1)
print() # O(1)