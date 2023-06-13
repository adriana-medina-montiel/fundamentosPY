students=[]

def show_students():
    for student in students:
        print("alumno->",student)
def add_student(student):
    students.append(student)
def remove_student(student):
    try:
        students.remove(student)
    except Exception:
        print("no existe")
    

choice_text='''
elige una opccion
1 insertar
2 mostrar
3 eliminar
4 salir
'''
while True:
    choice = int(input(choice_text))
    if choice ==1:
        student= input("ingresa estudiante")
        add_student(student)

    elif choice == 2:
        show_students()
    elif choice ==3:
        student= input("ingresa student para eliminar:")
        remove_student(student)
    elif choice==4:
        break    
    else:
        print('opcion incirrecta')        