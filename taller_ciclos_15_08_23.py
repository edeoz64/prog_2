# Punto número 1
import os
os.system ('cls')

con = 'main'
inn = input('Digite la contraseña: ')

if con == inn:
    print('Contraseña correcta ')
else:
    print('Contraseña incorrecta')
    
print('----------------------------------------------------------------')

# Punto número 2


x = int(input('Digite el primer número: '))
y = int(input('Digite el segundo número: '))
if y == 0:
    print('Error, digite nuevamente el número: ')
    yy = int(input('Digite el segundo número: '))
    print(x/yy)
else:
    print(x/y)


print('----------------------------------------------------------------')

# Punto número 3

n = int(input('Escriba un número: '))
if n % 2 == 0:
    print('Es par')
else:
    print('Es impar')
    
print('----------------------------------------------------------------')

# Punto número 4

vec = [4, 5, 20, 18, 2]
for a in vec:
    print(a)
    if a < 19:
        print('Menor de edad')
    else:
        print('Bienvenido')
        
    