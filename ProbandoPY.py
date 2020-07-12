from tkinter import *

def incrementar(entrada1, entrada2):
    incrementar=(entrada1.get())*(entrada2.get())
    return var.set(incrementar)
    
def main():
    ventana.title("Ventana")
    ventana.geometry("200x180")
    ventana.configure(bg = "red")
    var=StringVar()
    
    etiqueta1 = Label(ventana, text="Ingrese valor: ")
    entrada1 = Entry(ventana)
    
    etiqueta2 = Label(ventana, text="Ingrese porcentaje: ")
    entrada2 = Entry(ventana)
    
    botonSuma = Button(ventana, text= "Sumar", command=incrementar)
    
    res = Label(ventana, textvariable=var)
    
    #Llamadores
    etiqueta1.pack()
    entrada1.pack()
    
    etiqueta2.pack()
    entrada2.pack()
    
    botonSuma.pack()
    res.pack()
    
    ventana.mainloop()
    
ventana = Tk()
main()