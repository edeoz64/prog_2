import os
os.system ('cls')



edad = int(input('Digite su edad: '))
if(edad>=18):
    print('Es mayor de edad')
else:
    print('Es menor de edad')
    
#-----------------------------------------------------------
#-----------------------------------------------------------

edad = int(input('Digite su edad: '))
if edad >= 18 and edad <= 35:
    print('Adultos jóvenes')
elif edad < 18 and edad > 0:
    print('Niños')
elif edad > 35 and edad <= 60:
    print('Adultos')
elif edad > 60:
    print('Adultos mayores')
    
