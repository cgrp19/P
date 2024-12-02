from Vehiculos import Particular
from Vehiculos import Comercial
class Nodo:
    __dato=object
    __siguiente=None
    def __init__(self,dato):
        self.__dato=dato
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getdato(self):
        return self.__dato
    def setdato(self,dato):
        self.__dato=dato
class Coleccion:
    __cabeza=None
    def __init__(self,cabeza):
        self.__cabeza=Nodo(cabeza)
    def insertar(self,nuevo_nodo):
        nodo=Nodo(nuevo_nodo)
        if self.__cabeza==None:
            self.__cabeza=nodo
        else:
            aux=self.__cabeza
            while aux.getsiguiente()!=None:
                aux=aux.getsiguiente()
            aux.setdato(nodo)
    def Cantidad(self):
        aux=self.__cabeza
        p=0
        c=0
        while aux.getsiguiente!=None:
            if isinstance(aux.getdato(),Particular):
                if aux.getdato().getnda()>3:
                    p+=1
            elif isinstance(aux.getdato(),Comercial):
                if aux.getdato().getcapacidadcarga()>5:
                    c+=1
        print('Cantidad de particulares con mas de 3 duenos: {}'.format(p))
        print('Cantidad de comerciales con capacidad mayor a 5 toneladas: {}'.format(c))
    


