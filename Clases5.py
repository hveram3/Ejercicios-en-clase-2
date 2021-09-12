#fecha 19/07/21____23/07/21
import os
class Menu:
    def __init__ (self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...()]".format(len(self.opciones)))
        return opc
    
while opc !="5":
    men = Menu("Menu Principal",["1) calculadora","2) Numeros ","3)Listas","4)cadenas","5)salir"
    opc = men.menu()
    if opc == "1":
        menu1 = Menu("Menu Calculadora",["1)Suma", "2)Resta","3)Multiplicacion","4)Division","5)Salir")
        opc1 = menu1.menu()
            if opc1= =="1":
        print("suma de dos numeros")
        n1 = int(input("Ingrese numero1:"))
        n2 = int(input("Ingrese numero2:"))
        print(n1+n2)
        input("presione una tecla para continuar...")
        
    elif opc1 == "2":
        print("Resta de los numeros")
    
    elif opc1 == "3":
