text = """ 
    1 - IVA
    2 - Ganancia
    """
print(text)

lista = []
def Incrementar(opc):
    num = 1
    while num != 0:
        num = int(input("Ingrese numero: "))
        if opc == 1:
            resul = num * 1.21
            lista.append(resul)
            print(lista, "\n")
        if opc == 2:
            resul = num * 1.3
            lista.append(resul)
            print(lista, "\r\n")
            
    return lista
    print("Resultado " + str(Incrementar(num, opc)))

opc = int(input("Ingrese opc: "))
print(Incrementar(opc))