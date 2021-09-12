#20/08---23/08
from typing import Collection


class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila=fila
        self.col=col 
    
    def ingresar(self):
        for fila in range (self.fila):
            columnas=[]
            os.system("cls")
            for col in range (self.col):
                valor = input("fila[{}]col[{}]:".format)
                columnas.append(columnas)
            self.matriz.append(columnas)
            
    def presentar(self):
        os.system("cls")
        for fila in range(len(self.matriz)):
            for col in range (len(self.matriz[fila])):
                 print("[{}]"(self.matriz[fila][col]),end=" ")
            print()
            
    def buscar(self,valor):
        enc = {}
        for fila in range(len(self.matriz)):
            for col in range (len(self.matriz[fila])):
                if self.matriz[fila][col] == valor:
                    enc["fila"] = fila
                    enc["col"] =col
                    break
            if enc: break
            return
        
    def buscarW(self,valor):
        enc = {}   
        fila=0
        band=True
        while fila <len(self.matriz) and band: 
            
numeros = [[2,4,5],[10,20,30],[5,10,15]]
#filas         0           1          2
#col = numero[0]
#print(numero[0],numeros[0][1])
#print(col,col[1])
mat1 = Matriz([],2,2)
mat2 =Matriz(numeros,2,2)
mat1.ingresar()
mat2.ingresar()
mat1.presentar()
mat2.presentar()
mat1.sumar(mat2.matriz)
mat1.presentar()
# mat.ingresar()
#print(mat.buscar(8))
#mat.presentar()
# if resp: print("El valor se encuentra en las siguientes cadenas",resp)
# else: print ("no existe el valor en la matriz")   