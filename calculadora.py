sw =True
def sumar():
    print('Ingrese los parametros')
    primero=int(input('A '))
    segundo=int(input('B '))
    resultado=primero+segundo
    print('La suma es ', resultado)

def restar() :
    print('Ingrese los parametros')
    primero = int(input())
    segundo = int(input())
    resultado=primero-segundo
    print(resultado)

def multiplicar():
    print('Ingrese los parametros')
    primero = int(input())
    segundo = int(input())
    resultado = primero * segundo
    print(resultado)

def dividir():
    print('Ingrese los parametros')
    primero = int(input())
    segundo = int(input())
    if segundo==0:
        print('No se puede dividir entre cero')

    else:
     resultado=primero/segundo
     print(resultado)
def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False
def opcion_no_disponible():
    print('Opcion no disponible')


menu = '''
======= CALCULADORA ======
1. Sumar
2. Restar
3. Multiplicar
4. dividir
5. Salir
6.Limpiar
7.limpiar
'''
while sw:
    print(menu)
    opcion = int(input('Ingrese opcion: '))
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion is 4:
        dividir()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()

