from Vehiculos import Particular
from Vehiculos import Comercial
from Vehiculos import Vehiculo
class Nodo:
    __vehiculo=Vehiculo
    __siguiente=object
    def __init__(self,vehiculo):
        self.__vehiculo=vehiculo
        self.__siguiente=None
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getvehiculo(self):
        return self.__vehiculo
    def setvehiculo(self,vehiculo):
        self.__vehiculo=vehiculo
class Coleccion:
    __cabeza=Nodo
    __actual=Nodo
    __indice=int
    __cant=int
    def __init__(self):
        self.__cabeza=None
        self.__actual=None
        self.__indice=0
        self.__cant=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__cant:
            self.__actual=self.__cabeza
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getvehiculo()
            self.__actual=self.__actual.getsiguiente()
            return dato
    def insertar(self,nuevo_nodo):
        nodo=Nodo(nuevo_nodo)
        if self.__cabeza==None:
            self.__cabeza=nodo
            self.__actual=self.__cabeza
        else:
            aux=self.__cabeza
            while aux.getsiguiente()!=None:
                aux=aux.getsiguiente()
            aux.setsiguiente(nodo)
        self.__cant+=1
    def Cantidad(self):
        print('_________________________________________________________________________________')
        
        p=0
        c=0
        
        for vehiculo in self :
            print('ooooooooooo')
            if isinstance(vehiculo,Particular):
                print('AAAAAAAAAAAAAA')
                if vehiculo.getnda()>3:
                    p+=1
                    print(p)
            elif isinstance(vehiculo,Comercial):
                if vehiculo.getcapacidadcarga()>5:
                    c+=1
                    print(c)
            
        print('Cantidad de particulares con mas de 3 duenos: {}'.format(p))
        print('Cantidad de comerciales con capacidad mayor a 5 toneladas: {}'.format(c))
    def ImporteTotal(self):
        aux=self.__cabeza
        while aux!=None:
            importe=aux.getvehiculo().CalculoImporte()
            print('Importe del vehiculo {} {}: {}'.format(aux.getvehiculo().getmarca(),aux.getvehiculo().getmodelo(),importe))
            aux=aux.getsiguiente()
    def Tipo(self,p):
        aux=self.__cabeza
        i=0
        while aux!=None and i!=p:
            i+=1
            aux=aux.getsiguiente()
        if isinstance(aux.getvehiculo(),Particular):
            print('El vehiculo en la posicion {} es particular'.format(p+1))
        elif isinstance(aux.getvehiculo(),Comercial):
            print('El vehiculo en la posicion {} es comercial.'.format(p+1))


    


