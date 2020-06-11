import os
empleados ={100:"Ruiz",200:"Gomez",300:"Salas"}
vbuscar = 0
encontrado="0"
nombre =""
resp =""

while resp!="N":
    vbuscar = int(raw_input("ingrese empleado a localizar"))
    for i in empleados:
        if i == vbuscar:
            encontrado="1"
            nombre = empleados[i]
            break
        else:
           encontrado="0"
    if encontrado == "1":
         print ("El empleado es:"+nombre)
    else:
         print("No se encontro el empleado")
    resp = raw_input("Desea continuar <s/n>:").upper()
    os.system('cls')
print("thanks you")