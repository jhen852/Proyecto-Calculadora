import  tkinter as tk



sw =False
def sumar():
    print('Ingrese los parametros')
    resultado = int(numerorestarA.get()) + int(numerorestarB.get())
    print(resultado)
    return mensaje.set(resultado)
def restar() :
    print('Ingrese los parametros')
    resultado=int(numerorestarA.get())-int(numerorestarB.get())
    print(resultado)
    return mensaje.set(resultado)
def multiplicar():
    print('Ingrese los parametros')
    resultado = int(numerorestarA.get()) * int(numerorestarB.get())
    print(resultado)
    return mensaje.set(resultado)


def dividir():
    print('Ingrese los parametros')
    primero = int(numerorestarA.get())
    segundo = int(numerorestarB.get())
    if segundo==0:
        mensaje.set('No hay division entre cero')

    else:
     resultado=primero/segundo
     return mensaje.set(resultado)

root = tk.Tk()
ver =tk.getint()
mensaje =tk.StringVar()
numerorestarA=tk.StringVar()
numerorestarB=tk.StringVar()
root.geometry('800x500')
root.title('CALCULADORA')
root.configure(bg="#689F38")

#titulo
tk.Label(root, text='CALCULADORA',bg="#689F38",fg='white',font=('',32)).place(x=250,y=30)
#salir
tk.Button(root, text="salir", bd=0,command=root.destroy).place(x=400, y=450)

#donde saldra el resultado
tk.Label(root,textvariable=mensaje,bg="black",fg='white').place(x=400,y=400)

#sumar
tk.Label(root, text='sumatoria',bg="#689F38",fg='white',font=('',15)).place(x=100,y=150)
tk.Entry(root,justify='center' ,textvariable=numerorestarA).place(x=250,y=150)
tk.Entry(root,justify='center' ,textvariable=numerorestarB).place(x=450,y=150)
tk.Button(root, text="SUMAR", bd=0,command=sumar).place(x=620, y=150)

#estamos restando
tk.Label(root, text='Restar',bg="blue",fg='red',font=('',15)).place(x=100,y=250)
tk.Entry(root,justify='center' ,textvariable=numerorestarA).place(x=250,y=250)
tk.Entry(root,justify='center' ,textvariable=numerorestarB).place(x=450,y=250)
tk.Button(root, text="Restar", bd=0,command=restar).place(x=620, y=250)

#estamos multiplicando
tk.Label(root, text='Multiplicar',bg="blue",fg='red',font=('',15)).place(x=100,y=350)
tk.Entry(root,justify='center' ,textvariable=numerorestarA).place(x=250,y=350)
tk.Entry(root,justify='center' ,textvariable=numerorestarB).place(x=450,y=350)
tk.Button(root, text="Multiplicar", bd=0,command=multiplicar).place(x=620, y=350)

#estamos dividiendo
tk.Label(root, text='Dividir',bg="blue",fg='red',font=('',15)).place(x=100,y=450)
tk.Entry(root,justify='center' ,textvariable=numerorestarA).place(x=250,y=450)
tk.Entry(root,justify='center' ,textvariable=numerorestarB).place(x=450,y=450)
tk.Button(root, text="Dividirr", bd=0,command=dividir).place(x=620, y=450)

root.mainloop()






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

