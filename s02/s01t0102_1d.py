#Importando el modulo de arrar de 
#La biblioteca array y renombranbolo como arr 
from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input:
        print(element,end=',')
    print("\b]")

my_array = arr('i',[5,10,15,20])    
print_array(my_array)

# Buscar el elemento 
number_to_search = 15
counter = 0
print(f"Se busca {number_to_search} en el arreglo")
for integer in my_array:

    if integer == number_to_search:
        print("Numwero encontrado")
        # sirve para salir del bucle for
        break
    #Icrementamos el conrador
    counter += 1
    if counter == len(my_array):
        print("Numero no encontrado") 