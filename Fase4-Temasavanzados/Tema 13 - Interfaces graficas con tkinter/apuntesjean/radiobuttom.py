from tkinter import * 

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
    
def reset():
    opcion.set(None)
    monitor.config(text="")

# inicio de tkinter 
root = Tk() 

# variable
opcion = IntVar()

# botones de esleccion 
Radiobutton(root,text="opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root,text="opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root,text="opcion 3", variable=opcion, value=3, command=seleccionar).pack()
 
# Show label de la seleccion  
monitor= Label(root)
monitor.pack()

# boton 
Button(root, text="Reiniciar", command=reset).pack()

# fin de tkinter
root.mainloop()


"""
from tkinter import * 
root = Tk() 
root.mainloop()
"""