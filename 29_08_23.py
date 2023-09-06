#camelCase -> sumaDosNumeros
#pascalCae -> Funciones
import os
os.system('cls')
def suma():
    a = 20
    w = 30
    print('suma',a + w)
    
suma()

def resta():
    e = 30
    t = 15
    return (e - t)

print('Resta es:',resta())
incremento = resta() + 20
print('El resultado es: ',incremento)

def alumnos():
    return ['juan', 'maria', 'jose']

print(alumnos()[1])

for val in alumnos():
    print('Nombre:',val)