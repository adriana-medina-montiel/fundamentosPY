import random

int_rand = random.randint(0,2)

if int_rand==0:
    choice_maq ="piedra"
elif int_rand==1:
    choice_maq="papel"

else:
    choice_maq="tijera"    
 

#elige usuario
choice_txt ='''
escribe una opcion:
piedra
papel
tijera
'''
choice_user = input(choice_txt)

print("maquina->",choice_maq)
print("usuario->",choice_user)

if choice_maq == choice_user:
    print("es un empate")
else: 
    if choice_maq == "piedra" and choice_user == "papel":
        print("gana usuario!")
    elif choice_maq == "piedra" and choice_user == "tijera":
        print("gana maquina") 

    elif choice_maq == "papel" and choice_user == "piedra":
        print("pierde maquina ")

    elif choice_maq == "papel" and choice_user == "tijera":
        print("gana usuario") 

    elif choice_maq == "tijera" and choice_user == "papel":
        print("gana maquina") 
    else:
        print("gana usuario")
    



