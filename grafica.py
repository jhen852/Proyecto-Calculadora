import  tkinter as tk

sw =False
def sumar():
    print('Ingrese los parametros')
    resultado = int(numerorestarA.get()) + int(numerorestarB.get())
    print(resultado)
    return mensaje.set(resultado)
def restar() :
    print('Ingrese los parametros')
    resultado=int(numerorestarC.get())-int(numerorestarD.get())
    print(resultado)
    return mensaje.set(resultado)
def multiplicar():
    print('Ingrese los parametros')
    resultado = int(numerorestarE.get()) * int(numerorestarF.get())
    print(resultado)
    return mensaje.set(resultado)

def dividir():
    print('Ingrese los parametros')
    primero = int(numerorestarG.get())
    segundo = int(numerorestarH.get())
    if segundo==0:
        mensaje.set('No hay division entre cero')
    else:
     resultado=primero/segundo
     return mensaje.set(resultado)
def borar():
    numerorestarA.set(' ')
    numerorestarA.set(' ')
    numerorestarB.set(' ')
    numerorestarC.set(' ')
    numerorestarD.set(' ')
    numerorestarE.set(' ')
    numerorestarF.set(' ')
    numerorestarG.set(' ')
    numerorestarH.set(' ')



root = tk.Tk()
ver =tk.getint()
mensaje =tk.StringVar()
#variables para suma
numerorestarA=tk.StringVar()
numerorestarB=tk.StringVar()
#variables para resta
numerorestarC=tk.StringVar()
numerorestarD=tk.StringVar()
#variables para multiplicacion
numerorestarE=tk.StringVar()
numerorestarF=tk.StringVar()
#variables para divisor
numerorestarG=tk.StringVar()
numerorestarH=tk.StringVar()
root.geometry('800x650')
root.title('CALCULADORA')
root.configure(bg="#689F38")

#titulo
tk.Label(root, text='CALCULADORA',bg="#689F38",fg='#4a148c',font=('',35)).place(x=250,y=30)
#salir
tk.Button(root, text="salir", bd=0,command=root.destroy,font=('',15)).place(x=390, y=570)

#donde saldra el resultado
tk.Label(root,textvariable=mensaje,bg="black",fg='white' , font=('',20)).place(x=400,y=510)

#sumar
tk.Label(root, text='Sumatoria',bg="#689F38",fg='black',font=('',15)).place(x=100,y=150)
tk.Entry(root,justify='center' ,textvariable=numerorestarA).place(x=250,y=150)
tk.Entry(root,justify='center' ,textvariable=numerorestarB).place(x=450,y=150)
tk.Button(root, text="SUMAR", bd=0,command=sumar ,bg="#FFA000").place(x=620, y=150)

#estamos restando
tk.Label(root, text='Restar',bg="#689F38",fg='black',font=('',15)).place(x=100,y=250)
tk.Entry(root,justify='center' ,textvariable=numerorestarC).place(x=250,y=250)
tk.Entry(root,justify='center' ,textvariable=numerorestarD).place(x=450,y=250)
tk.Button(root, text="RESTAR", bd=0,command=restar,bg="#9C27B0").place(x=620, y=250)

#estamos multiplicando
tk.Label(root, text='Multiplicar',bg="#689F38",fg='black',font=('',15)).place(x=100,y=350)
tk.Entry(root,justify='center' ,textvariable=numerorestarE).place(x=250,y=350)
tk.Entry(root,justify='center' ,textvariable=numerorestarF).place(x=450,y=350)
tk.Button(root, text="MUTIPLICAR", bd=0,command=multiplicar, bg="#1976D2").place(x=620, y=350)

#estamos dividiendo
tk.Label(root, text='Dividir',bg="#689F38",fg='black',font=('',15)).place(x=100,y=450)
tk.Entry(root,justify='center' ,textvariable=numerorestarG).place(x=250,y=450)
tk.Entry(root,justify='center' ,textvariable=numerorestarH).place(x=450,y=450)
tk.Button(root, text="DIVIDIR", bd=0,command=dividir, bg="#BBDEFB").place(x=620, y=450)

#estamos limpiar
tk.Entry(root,justify='center' ,textvariable=numerorestarH).place(x=450,y=450)
tk.Button(root, text="Limpiar", bd=0,command=borar,font=('',15)).place(x=190, y=570)
root.mainloop()



