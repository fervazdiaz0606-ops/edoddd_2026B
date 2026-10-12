#Array
#From Array import *
import array as arr

#Creacion de un arreglo 
# 1: Entero con signo 
# I: Entero sin signo
# f: numero decimal 
# d: numero decimal de doble 
# u: Caracter unicode
my_array = arr.array('i', [10, 22, 300, 400, 500, 600, 700, 800, 900, 1000]) # O(n)

# Interaccion automatica 
for num in my_array: # O(n)
    print(num) # O(1)

#Acceso individual a los elementos 
print(my_array[0]) # primer elemento 
print(my_array[1]) # segundo elemento 
print(my_array[2]) # tercer elemento 

#Tamaño del arreglo
#Length 
print(len(my_array)) # O(1)

#Interaccion por indices 
for i in range(len(my_array)): # O(n)
  if my_array[i] % 2 == 0: 
    print(f"Elemento {i}: {my_array[i]}") # O(1)