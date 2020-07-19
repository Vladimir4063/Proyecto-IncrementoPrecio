
lista = []
def Incrementar(opc):
    num = 1
    while num != 0:
        num = int(input("Ingrese numero: "))
        if opc == 1:
            resul = num * 1.21
            lista.append(resul)
        if opc == 2:
            resul = num * 1.3
    return lista
    print("Resultado " + str(Incrementar(num, opc)))


text = """ 
    1 - IVA
    2 - Ganancia
    """
print(text)

opc = int(input("Ingrese opc: "))
#num = int(input("Ingrese numero: "))
print(Incrementar(opc))