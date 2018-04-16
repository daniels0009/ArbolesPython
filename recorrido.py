class Nodo():
     izq , der, dato = None, None, 0
    def __init__(self, valor):
        self.valor= valor
        self.izquierda = izq
        self.derecha=der
        
def posorden(arbol):
    if arbol==None:
        return ""
    else:
        return posorden(arbol.izquierda)+posorden(arbol.derecha)+arbol.valor
def inorden(arbol):
    if arbol==None:
        return ""
    else:
        return inorden(arbol.izquierda)+arbol.valor+inorden(arbol.derecha)
    
def preorden(arbol):
     if arbol==None:
        return ""
     else:
        return arbol.valor+preorden(arbol.izquierda)+preorden(arbol.derecha)
    
   
arbol = Nodo('1500000 ',Nodo('2000004 '),Nodo('180000 ',Nodo('100 '),Nodo('10000 ')))
print("pre: "+preorden(arbol))
print("in: "+inorden(arbol))
print("pos: "+posorden(arbol))
