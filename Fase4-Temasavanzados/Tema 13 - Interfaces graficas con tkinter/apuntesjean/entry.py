from tkinter import *

root = Tk()



label = Label(root, text="Nombre")
label.grid(row=0, column=0,sticky="e",pady=5)

entry = Entry(root)
entry.grid(row=0, column=1)
entry.config(justify="center")

label2 = Label(root, text="contraseña")
label2.grid(row=1, column=0, sticky="e", pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1) 
entry2.config(justify="center",show="*")



root.mainloop()
