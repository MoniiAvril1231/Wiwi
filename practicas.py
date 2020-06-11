contador = 0
while contador <= 10:
    print(contador)
    contador += 2 


cont_ext = 0
cont_int = 0

while cont_ext < 3:
    while cont_int < 60:
        print(cont_ext, cont_int)
        cont_int += 1

    cont_ext += 1
    cont_int = 0