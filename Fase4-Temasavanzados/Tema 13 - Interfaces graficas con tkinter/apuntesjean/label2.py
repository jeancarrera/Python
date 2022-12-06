from tkinter import *   

root = Tk()
""""
texto= StringVar()
texto.set("un nuevo texto")

Label(root, text="Hooa mundo").pack(anchor="nw")
label = Label(root, text="otra etiqueta")
label.pack(anchor="center")
label(root,text="ultima etiqueta").pack(anchor="se") 

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable= texto)
"""
imagen = PhotoImage(file= "imagen.gif")
Label(root, image=imagen, bd=0 ).pack(side= "left" )

root.mainloop()

             