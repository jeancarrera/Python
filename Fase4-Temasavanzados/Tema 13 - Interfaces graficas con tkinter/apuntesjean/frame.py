from tkinter import *

root = Tk()
root.title("Hola mundo") # title o titulo de ventana
root.iconbitmap("hola.ico") # iconbitmap ingresa imagenes al borde la ventana
root.resizable(1,1)# resizable para permitir  el movimento de la ventana

frame = Frame(root,width=480,height=320)
frame.pack(fill="both", expand=1)#fill ancla algun bloque interno de la navegacion ya sea en X o Y, expand permite ajustar el alto  
frame.config(cursor="pirate")#cursor  sirve para modificar el cursor dentro de la navegacion 
frame.config(bg="lightblue")# "bg" diminutivo de background se encarga del fondo de la navegacion 
frame.config(bd=20)#bd 
frame.config(relief="sunken")#relief  sirve para modificar el tipo de borde 
#frame.config()#la opcion config se usa para modificar el entorno y las configuraciones de la navegacion, "width" es ancho de la ventana y height es el alto de la ventana, se expresan en pixeles los digitos de amplitud  



root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


root.mainloop()# finaliza el bucle de la aplicación
