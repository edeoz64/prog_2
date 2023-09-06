import os
os.system('cls')

#-----------------------------1-------------------------------

def saludo():
     x = input('Ingrese un saludo personalizado: ')
     os.system('cls')
     print(x)
saludo()
os.system('pause')
os.system('cls')

#-----------------------------2-------------------------------

def salnom():
     nom = input('Ingrese su nombre: ')
     os.system('cls')
     print('¡ Hola',nom,'!')
salnom()
os.system('pause')
os.system('cls')

#-----------------------------3-------------------------------

def noeda():
     nombre = input('Ingrese su nombre: ')
     edad = input('Ingrese su edad: ')
     os.system('cls')
     print('Su nombre es',nombre,'y su edad es',edad)
noeda()
os.system('pause')
os.system('cls')

#-----------------------------4-------------------------------

def arit(*args):
     
     suma = args[0]
     resta = args[0]
     multipica = args[0]
     divi = args[0]
     
     for i in args[1:]: 
          suma += i
          resta -= i
          multipica *= i
          divi /= i
               
     print("Suma:", suma)
     print("Resta:", resta)
     print("Multiplicación:", multipica)
     print("División:", divi)

arit(2,1,2,1,2)
os.system('pause')
os.system('cls')   
