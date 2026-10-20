
from array import array as arr

#imprecion de una tabla 
def print_table(table):
    #Imprimiendo
    for row in table:
        for column in row:
            print(column, end=",")
        print("\b ")

table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9]),
]

print_table(table)

# Insercion 
row = 1
column = 2
value = 99

# Insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

#Imprime mensaje
print("---DESPUES DA LA INSERCION---")
print_table(table) #DRY

# Insertando una fila completa 
new_row = arr('i', [100, 200, 300])
pos = 1
table.insert(pos, new_row)

#Imprime mensaje
print("---DESPUES DE LA INSERCION DE LA FILA---")
print_table(table) #DRY

#Eliminacion de un elemento
del table[2]

#Imprime mensaje
print("---DESPUES DE LA ELIMINACION DE LA FILA 2---")
print_table(table) #DRY
