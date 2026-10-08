import time

#crear la veriable para el problema 
n = 100
the_sum = 0

# toma el tiempo 1
timestamp_01 = time.time()
#iniciando la suma 
while(n > 0):
    the_sum = the_sum + n
    n = n - 1

# toma el tiempo 2
timestamp_02 = time.time()

# imprimimos la solucion 
print(f"La suma es: {the_sum}")

# calculamos el tiempo 
elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)
print(f"Tiempo de ejecución: {elapsed_time} µs")
