#30/08
class  Lista :
    def  __init__ ( self , listas ):
        def lista =  listas
        
    @propiedad
    def  lista ( self ): #getproperty
        volver a  sí mismo . __lista  
      
    # @ lista.setter
    # def lista (self, value): #getproperty
    # return self .__ lista == valor  
    
    #Busca un valor en la lista; retorna la posición si lo encuentra
    # y si no lo encuentra retorna -1     
    def  busquedaLineal ( self , buscado ):
        pos = 0
        enc = Falso
        lon = len ( yo . __lista )
        #recorre la lista hasta que la posicion sea igual a la longitud y found sea igual a True, o found sea verdadero
        while  pos  <  lon  y  enc == False :
            si  yo . __lista [ pos ] [ "nombre" ] == buscado :
                enc = Verdadero
                rotura
            otra cosa :
                pos = pos + 1
        if  enc : return  pos
        else : return  - 1
                    
    def  ordenar ( self , orden ):
        orden  =  orden . inferior ()
        if  orden  == "asc" :
            para  pos  en el  rango ( 0 , len ( self . __lista )):
                para  sig  en  rango ( pos + 1 , len ( self . __lista )):
                    si  yo . __lista [ pos ] [ "nombre" ] >  self . __lista [ sig ] [ "nombre" ]:
                        aux  =  self . __lista [ pos ]
                        yo . __lista [ pos ] = self . __lista [ sig ]
                        yo . __lista [ sig ] = aux
        otra cosa :
            if  orden  == "des" :
                para  pos  en el  rango ( 0 , len ( self . __lista )):
                    para  sig  en  rango ( pos + 1 , len ( self . __lista )):
                        si  yo . __lista [ pos ] [ "nombre" ] <  self . __lista [ sig ] [ "nombre" ]:
                            aux  =  self . __lista [ pos ]
                            yo . __lista [ pos ] = self . __lista [ sig ]
                            yo . __lista [ sig ] = aux
                            
                    
    def  busquedaBinaria ( self , buscado ):
        yo . ordenar ( "asc" )
        fin  =  len ( self . lista ) - 1  # Guarda la posición final del segmento lista
        inicio  =  0  #guarda la posición del segmento lista
        enc = Falso
        #se busca mientras que la posición sea menor que la final
        while  inicio  <=  fin  y  enc == Falso :
            medio  = ( inicio + fin ) // 2
            si  yo . lista [ medio ] [ "nombre" ] ==  buscado : enc = True
            elif  self . lista [ medio ] [ "nombre" ] <  buscado : fin = medio + 1
            else : inicio = medio - 1
        if  enc : return  medio
        else : return  - 1
        
    
    
notas = [{ "nombre" : "Daniel" , "n1" : 20 , "n2" : 40 },
       { "nombre" : "Danny" , "n1" : 30 , "n2" : 50 },
       { "nombre" : "Dayana" , "n1" : 40 , "n2" : 50 },
       { "nombre" : "Erick" , "n1" : 50 , "n2" : 40 },
       { "nombre" : "Romina" , "n1" : 55 , "n2" : 40 },
       { "nombre" : "Yady" , "n1" : 60 , "n2" : 40 }
]

bus  =  Lista ( notas )
# bus.lista = [3,5]
# posición = bus.busquedaLineal ("Erick")
# si posición! = - 1:
# print (bus.lista [posición])
# demás:
# print ("Nombre, no se encuentra en la lista")

posici ó n = bus . busquedaBinaria ( "Erick" )
si  posici ó n ! = - 1 :
    imprimir ( bus . lista [ posici ó n ])
otra cosa :
    print ( "Nombre, no se encuentra en la lista" )

# bus.ordenar ("des")
# print (bus.lista)    