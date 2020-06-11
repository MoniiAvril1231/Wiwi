import os
user_1 = ''
age_1 = 0
user_2 = ''
age_2 = 0

user_1 = input('Nombre del primer usuario: ')
age_1 = int(input('Indica tu edad: '))

while age_1 < 0:
    print('Incorrecto. Inténtelo nuevamente!')
    age_1 = int(input('Indica tu edad: '))

user_2 = input('Nombre del segundo usuario: ')
age_2 = int(input('Indica tu edad: '))

while age_2 < 0:
    print('Incorrecto. Inténtelo nuevamente!')
    age_2 = int(input('Indica tu edad: '))

if age_1 > age_2:
    print(f'{user_1} es mayor que {user_2}')
elif age_1 < age_2:
    print(f'{user_1} es menor que {user_2}')
else:
    print(f'{user_1} tienen la misma edad {user_2}')
    resp = input("Desea continuar <s/n>:").upper()
os.system('cls')
print("thanks you")