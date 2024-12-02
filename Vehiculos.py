class Vehiculo:
    valorbase=20000
    __marca=str
    __modelo=str
    __patente=str
    __ano=int
    __tsr=str
    def __init__(self,marca,modelo,patente,ano,tsr):
        self.__marca=marca
        self.__modelo=modelo
        self.__patente=patente
        self.__ano=ano
        self.__tsr=tsr
    def CalculoImporte(self):
        i=self.valorbase+self.Importe()
        
        return i
    def Importe(self):
        pass
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    @classmethod
    def setvalorbase(self,nuevo_valor):
        self.valorbase=nuevo_valor
    @classmethod
    def getvalorbase(self):
        return self.valorbase

class Particular(Vehiculo):
    __nda=int
    __km=float
    __cgeneral=str
    def __init__(self,marca,modelo,patente,ano,tsr,nda,km,cgeneral):
        super().__init__(marca,modelo,patente,ano,tsr)
        self.__nda=nda
        self.__km=km
        self.__cgeneral=cgeneral
    def Importe(self):
        if self.__cgeneral=='Buena':
            
            return self.valorbase*10/100
        elif self.__cgeneral=='Regular':
            return 0
        elif self.__cgeneral=='Mala':
            return self.valorbase*20/100
    def getnda(self):
        return self.__nda

class Comercial(Vehiculo):
    __empresa=str
    __rubro=str
    __capacidadcarga=float
    def __init__(self,marca,modelo,patente,ano,tsr,empresa,rubro,capacidadcarga):
        super().__init__(marca,modelo,patente,ano,tsr)
        self.__empresa=empresa
        self.__rubro=rubro
        self.__capacidadcarga=capacidadcarga
    def Importe(self):
        if self.__capacidadcarga<=float(5):
            return self.valorbase*15/100
        else:
            return self.valorbase*25/100
    def getcapacidadcarga(self):
        return self.__capacidadcarga
        

