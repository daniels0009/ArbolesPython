 class nodo:
    izq , der, dato = None, None, 0
 
    def __init__(self, dato):
       
        self.izq = None
        self.der = None
        self.dato = dato
 
class arbolBinario:
    def __init__(self):
        
        self.raiz = None
 
    def agregarNodo(self, dato):
     
        return nodo(dato)
    def inOrden(arbol):
     if arbol != None:
      inOrden(arbol.izquierda)
      print(arbol.valor)
      inOrden(arbol.derecha)
    def insertar (arbol,valor):
    if arbol==None:
        return ArbolBin(valor)
    if valor<arbol.valor:
        return ArbolBin(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return ArbolBin(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))
      
def listarEnArbol(arbol, lista):
    if lista==[]:
        return arbol
    else:
        return listarEnArbol(insertar(arbol,lista[0]),lista[1:])
    
inOrden(listarEnArbol((ArbolBin(15,ArbolBin(10,ArbolBin(0)),ArbolBin(55, ArbolBin(25)))),[5,50,20,30,35,45,40]))