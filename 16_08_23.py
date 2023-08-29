#listas o arreglos
import os
os.system ('cls')

'''
varlist = ['Duvan', True, 5.5, 9]

print(varlist[0])
print(varlist[1])
print(varlist[2])
print(varlist[3])


#del varlist[2] #elimina elementos dentro de la lista


varlist.insert(1, "donde?")
varlist.append('usco')
#varlist.append(input('Inserte ciudad: '))


for z in varlist:
    print(z)
    
print('----------------------------------------------------------')
print('----------------------------------------------------------')

q = 0
while q < len(varlist):
    print(varlist[q])
    q += 1
   
print('----------------------------------------------------------')
print('----------------------------------------------------------')
'''
'''
eliminar = ('Digite el calor a eliminar: ')
contador = 0
for z in varlist:
    if eliminar == z:
        del varlist[contador]
    else:
        contador += 1
        
print(varlist)

print('----------------------------------------------------------')
print('----------------------------------------------------------')

'''




datos = [[['hector', 'duvan'], ['doz', 'aaaaaa']],[['he1ctor', 'du1van'], ['do1z', 'aaa1aaa']]]

print(datos[1][1][1])

print('----------------------------------------------------------')
print('----------------------------------------------------------')

for i in datos:
    for u in i:
        for x in u:
            print(x)
        print('---------')
        
duplas
