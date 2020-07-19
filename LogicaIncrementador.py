
num = int(input("Ingrese numero: "))
text = """ 
    1 - IVA
    2 - Ganancia
"""
print(text)
opc = int(input("Ingrese opc: "))

def Incrementar(num, opc):
    if opc == 1:
        resul = num * 1.21
    if opc == 2:
        resul = num * 1.3
    return resul

print("Resultado " + str(Incrementar(num, opc)))