#import library
import tkinter as tk

def Mostrar():
    
    mensaje = ''
    
    if(intChek1.get()==1):
        mensaje=mensaje+"Compraste manzana"
    if(intChek2.get()==1):
        mensaje=mensaje+"Compraste pera"
    if((intChek1.get()==1) or (intChek2.get()==1)):
        mensaje=mensaje+"Genial, compraste ambas"

    else:
        mensaje=mensaje+ "No olvide comprar Fruta"
    lblMensaje.config(text=mensaje)

ventana = tk.Tk()
ventana.title("CheekButton")
ventana.geometry("300x100")


#Variables
intChek1 = tk.IntVar()
intChek2 = tk.IntVar()

#Label messaje
lblMensaje = tk.Label(ventana)
lblMensaje.pack()

#Create Checkbutton
chek1 = tk.Checkbutton(ventana, text= "Manzana", variable=intChek1).pack()
chek2 = tk.Checkbutton(ventana, text= "Pera", variable=intChek2).pack()

#Button
BtnMostrar = tk.Button(ventana, text= "Comprar", command= Mostrar).pack()

ventana.mainloop()