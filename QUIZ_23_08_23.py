import os
os.system('cls')

print('EJERCICIO 1')
print('------------------------------')

mate = []
noot = []
num = int(input('Cuantas materias quiere adicionar?: '))
x = 0
while x < num:
    materia, nota = (input('Ingrese materia: '),float(input('Ingrese nota: ')))
    mate.append(materia)
    noot.append(nota)
    x += 1
    
os.system('cls')

for materia, nota in zip(mate,noot):
    print(materia, nota)

os.system('pause')
os.system('cls')


print('------------------------------')
print('EJERCICIO 2')
print('------------------------------')



personas = {}
vec = int(input('Cuantas personas desea agregar?: '))
x = 0
y = 1
while x < vec:
    personas[y]=(input('Ingrese el nombre: '))
    y += 1
    x += 1


for valor in personas.values():
    print('su nombre es:',valor)
    

os.system('pause')  
os.system('cls')

print('------------------------------')
print('EJERCICIO 3')
print('------------------------------')

moneda = {'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

cam = int(input('Ingrese la cantidad de dinero en pesos colombianos: '))
pe = int(input('A que divisa quiere realizar la conversión? (0 para euro, 1 para dolar, 2 para yen): '))
if pe == 0:
    total = 2*cam
    print('Su cambio es: ',total, moneda.get('Euro'))
elif pe == 1:
    total = 3*cam
    print('Su cambio es: ',total, moneda.get('Dollar'))
elif pe == 2:
    total = 4*cam
    print('Su cambio es: ',total, moneda.get('Yen'))
else:
    print('Divisa o entrada inexistente')

os.system('pause')
os.system('cls')

print('------------------------------')
print('EJERCICIO 4')
print('------------------------------')

n = 0
variables = (4, 3.2, 'hola', 10, ('hola', 32), [3, 'cosas'])
for n, tipo in enumerate(variables):
    print(f"Elemento en la posición {n} es de tipo {type(tipo)}")


os.system('pause')    
os.system('cls')