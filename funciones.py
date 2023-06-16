#funciones 
#def name_function(params);
#   code
#sin parametros y sin retorno
def saluda():
    print("hola a todos")

saluda()

#con parametros, sin retorno
def duplica(num):
    print(num *2)

duplica(5)

def suma (num1, num2):
    print(f"la suma de los numeros es:{num1+num2}")

suma(23,45)
#parametros opcionales
def get_lista(al_1 ="jose", al_2 ="darlen"):
    return[al_1, al_2]

my_list = get_lista()
print(my_list)
my_list = get_lista("peter")
print(my_list)
my_list = get_lista("peter parker, tony strark")
print(my_list)
my_list = get_lista(al_1="peter parker", al_2="tony strark")
print(my_list)
