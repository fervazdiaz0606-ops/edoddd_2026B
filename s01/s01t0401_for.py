#funcion que suma los primeros numeros "n" naturales
import time

#Funcion que suma los primeros numeros "n" naturales
def total_sum_of_n(n):
    total_sum = 0
    #sumando los "n"
    for number in range(1,n+1):
       total_sum = total_sum + number
    return total_sum

dataset = [] #

for reptition in range (1,11):
    timestamp_01 = time.time()
    #suma los "n" numeros
    n = reptition*500
    result = total_sum_of_n(n)
    timestamp_02 = time.time()
    elepsed_time = round((timestamp_02-timestamp_01) * 1e6,2)

    #Agregar la tripleta de los
    #datos al datset
    dataset.append( (n,elepsed_time,result) )

#impresion del tiempo de ejecucion

# Imprimir el dataset
for tup in dataset:
   print(tup)