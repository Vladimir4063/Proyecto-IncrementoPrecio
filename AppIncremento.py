import tkinter as tk

ventana = tk.Tk()
ventana.title("App Incr.")
ventana.geometry("200x200")

#Create Chekbutton
checkIva = tk.Checkbutton(ventana, text="IVA").pack()
check30 = tk.Checkbutton(ventana, text="30").pack()
check40 = tk.Checkbutton(ventana, text="40").pack()

ventana.mainloop()