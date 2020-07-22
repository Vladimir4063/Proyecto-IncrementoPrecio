from tkinter import *

def incrementar(entrada1, entrada2):
    incrementar=(entrada1.get())*(entrada2.get())
    return var.set(incrementar)
    
listaPrecio = [45, 56, 23, 43, 21]

#VENTANA GRAFICA!!!!!!!!

def main():
    ventana.title("Ventana")
    ventana.geometry("200x180")
    var=StringVar()
    
    Lbl1 = Label(ventana, text="IVA-5-40")
    Lbl2 = Label(ventana, text="IVA-5-30")
    Lbl3 = Label(ventana, text="30%")
    etiqueta1 = Label(ventana, text="Ingrese Opc: ")
    entrada1 = Entry(ventana)
    
    etiqueta2 = Label(ventana, text="Ingrese numero: ")
    entrada2 = Entry(ventana)
    
    botonSuma = Button(ventana, text= "Sumar", command=incrementar)
    
    res = Label(ventana, textvariable=var)
    
    #Llamador
    Lbl1.pack()
    Lbl2.pack()
    Lbl3.pack()
    etiqueta1.pack()
    entrada1.pack()
    
    etiqueta2.pack()
    entrada2.pack()
    
    botonSuma.pack()
    res.pack()
    
    ventana.mainloop()
    
ventana = Tk()
main()