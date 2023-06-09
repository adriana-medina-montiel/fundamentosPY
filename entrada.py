#fintion  imput retorna string
name= input("como te llamas?\n")
age= int(input('cuantos años tienes?\n'))
future= int(input('cuantos años mas?\n'))

print("hola" + name)
print("En\n" + str(future) + "años tendras\n" + str(age+future))



text_complete="hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print((f"hola{name}, en{future} años tendras{ age + future} años"))