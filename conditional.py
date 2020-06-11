nom = ""
sue = 0
tser = 0
bon = 0
nom = input("ingrese su nombre: ")
sue = int(input("ingrese su sueldo: "))
tser = int(input("tiempo de servicio: "))
if tser>=1 or tser<=3:
    bon = sue * 0.02
elif tser>=4 and tser<=5:
    bon = sue * 0.03
else:
    bon = sue * 0.04
print("La bonificacion de: "+ nom +" es:"+ bon)