import os
os.system('cls')

'''
def nombres():
    return {'Maria': 'sanchez', 'juan': 'silva'}

for i in nombres():
    print(f'nombre: {i} apellido:', nombres()[i])  

'''

def suma(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print('la sumatoria es: ', suma(10, 20, 30))