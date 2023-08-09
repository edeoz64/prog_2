import os 
os.system('cls')

print('Bienvenido a esta calculadora, según la operación que desee realizar ponga un símbolo, + para suma, - para resta, x para multiplicación y por último / para división')

op = input('Digite el simbolo de la operación que quiera realizar: ')
n1 = int(input('Digite el primer número: '))
n2 = int(input('Digite el segundo número: '))
suma = n1 + n2
rest = n1 - n2
mult = n1*n2
div = n1/n2
res = n1 % n2


if op == '+':
    print('El resultado de su suma es:', suma)
elif op == '-':
    print ('El resultado de su resta es:', rest)
elif op == 'x':
    print('El resultado de su multiplicación es:', mult)
elif op == '/' and n2 == 0:
    print('No es posible dividir entre 0') 
elif op == '/':
    print('El resultado de su división es:', div)