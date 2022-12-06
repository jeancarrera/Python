# importa tkinter 
from tkinter import *

# configuracion de la raiz tkinter
root = Tk()
root.title("label")

# confirucacion de un marco o ventana de navegacion
frame = Frame(root,width=430,height=350)
frame.pack()

label= Label(frame,text="hola mundo")
label.place



# cerrar el tkinter
root.mainloop()