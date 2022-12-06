from tkinter import *
# def boton():
#     print("Hola mundo")
    
    
# def name(args): 
#     Label(root, text="label creada dinamicamente").pack()
def sumar():
    r.set( float( n1.get()) + float(n2.get()))
    borrar()
    
def multiplicar():
    r.set( float( n1.get()) * float(n2.get()))
    borrar()
    
def resta():
    r.set( float( n1.get()) - float(n2.get()))
    borrar()       
     
def borrar():
    n1.set("")
    n2.set("")
    
root = Tk()
root.config(bd=15)
root.title("Calculadora")

          
n1 = StringVar()
n2 = StringVar()
r = StringVar()
   

Label(root,text= "Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack()#primer numero 

Label(root,text= "Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()#segundo numero

"""resultado"""
Label(root,text= "Resultado",pady=5).pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()#resultado


"""botones"""

Label(root,text= "").pack()

Button(root,text="Sumar", command=sumar).pack(side="left").pack()f

Button(root,text="Resta", command=resta).pack(side="lef")

Button(root,text="Multiplicar", command=multiplicar).pack(side="lef")




root.mainloop()