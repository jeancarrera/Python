from tkinter import *

# comando 
def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += ("Con leche")
    else:    
        cadena += ("Sin leche")
        
    if (azucar.get()):
        cadena += (" y con azucar")
    else:    
        cadena += (" y sin azucar")
 
    monitor.config(text=cadena)
    
# raiz
root = Tk() 
root.title("cafeteria")
root.config(bd=15)


# variables 
leche = IntVar()
azucar = IntVar() 

# imagen
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

# pregunta 
Label(frame, text="Como quieres el cafe?").pack(anchor="w")
# Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")


# botones de check 

Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

# Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

# Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")





monitor = Label(frame)
monitor.pack()

root.mainloop()