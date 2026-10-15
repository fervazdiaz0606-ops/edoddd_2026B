#xd
#
#
#
from array import array as arr

from s01t0102_1d import print_array

my_array = arr('i',[5,10,15,20])

print("---- Antes de la insercion ----")
print_array(my_array)

#
my_array.insert(1, 90) 
print("---- Despues de la insercion ----") 
print_array(my_array)

print("---- Despues de un append ----")
my_array.append(1000)
print_array(my_array)

print ("---- Simular un append con insert ----")
my_array.insert(len(my_array), 90000)
print_array(my_array)