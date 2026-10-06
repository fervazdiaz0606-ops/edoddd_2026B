'''
NOTAS 
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero 
deestudiantes.
2. Es ver cuanto crece el numero de 
operaciones en mi algoritmo conforme
creece el tamaño de la entrada 
Agrego las bigO identificadas 
Teniendo en cuenta la Cota superior asintotica
O(n) + O(4) = O(n+4) = 0(n)
'''

#creando un lista de estudiantes 
student_list_01 = ['Pau mi amor','Bot alex', 'fernanda', 'Diana']
student_list_02 = ['Poncho','Bot aza', 'fer good ', 'yerik']

def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student:
            print("👌Estudiante encontrado: ")
            return student
        #si no se encuentra el estudiante
    print("👻 Estudiante no encontrado")
    return None
#probando algoritmo
check_student('Pau mi amor', student_list_02) #
