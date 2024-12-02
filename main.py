import csv
from Vehiculos import Vehiculo
from Vehiculos import Particular
from Vehiculos import Comercial
from ClaseColeccion1 import Coleccion
def GenerarColeccion():
    coleccion = Coleccion()
    with open("C:/Users/Usuario/Desktop/VehiculosPOO/vehiculos.csv",mode='r') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            tipo=fila[0]
            if tipo=='P':
                coleccion.insertar(
                    Particular(
                        marca=fila[1],
                        modelo=fila[2],
                        patente=fila[3],
                        ano=fila[4],
                        tsr=fila[5],
                        nda=int(fila[6]),
                        km=fila[7],
                        cgeneral=fila[8]
                    )
                )
            elif tipo=='C':
                coleccion.insertar(
                    Comercial(
                        marca=fila[1],
                        modelo=fila[2],
                        patente=fila[3],
                        ano=fila[4],
                        tsr=fila[5],
                        empresa=fila[6],
                        rubro=fila[7],
                        capacidadcarga=float(fila[8])
                    )
                )
        return coleccion
if __name__=='__main__':
    c=GenerarColeccion()
    opcion=0
    while opcion !='4':
        opcion=input('Ingrese 1 si desea saber la cantidad de vehiculos particulares con mas de 3 duenos y los comerciales con capacidad mayor a 10 toneladas.\nIngrese 2 si desea saber el importe total cobrado por el taller a todos los vehiculos\nIngrese 3 si desea saber tipo de vehiculo en posicion a ingresar\nIngrese 4 si desea actualizar el valor base del servicio')
        if opcion=='1':
            c.Cantidad()
        elif opcion=='2':
            c.ImporteTotal()
        elif opcion=='3':
            p=input('Ingrese posicion')
            try:
                c.Tipo(int(p)-1)
            except:
                print('Indice fuera de rango.')
        elif opcion =='4':
            print('Valor base anterior: {}'.format(Vehiculo.getvalorbase()))
            v=input('Ingrese el nuevo valor base de servicio')
            Vehiculo.setvalorbase(v)
            print('Nuevo valor base: {}'.format(Vehiculo.getvalorbase()))


