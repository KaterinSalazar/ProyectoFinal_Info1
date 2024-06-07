'''Katerin Salazar Atehortua - 1007373986'''


# Importacion de librerias

from datetime import datetime
from conexion import *
import mysql.connector 
from mysql.connector import errorcode


def ValidarFecha(fecha_str):
    '''
    Descripcion: Utiliza la libreria datetime para verificar tipo de dato (fecha)

    Parametros:
        Input: fecha ingresada por consola
        Output: string que indica si esta incorrecto.
    
    Return:
         fecha si es valida
    '''
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        return fecha
    except ValueError:
        print("Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
        return None
    
    
def ImprimirProveedores():
    '''
    Descripcion: Lee los registros dentro de la tabla proveedores y los imprime

    Parametros:
        Input: None
        Output: registros dentro de la tabla proveedores.
    
    Return:
         list(proveedores)
    '''
    try:
        database = ConexionDB()
        if database is None:
            return []
        
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre, apellido FROM proveedores")
        proveedores = cursor.fetchall()
        
        cursor.close()
        database.close()

        if proveedores:
            
            for proveedor in proveedores:
                print(f"Código: {proveedor[0]}, Nombre: {proveedor[1]}, Apellido: {proveedor[2]}")
        else:
            print("No hay proveedores registrados.")

        return (proveedores)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return []
    


def ValidarProveedor(proveedorCodigo):
    '''
    Descripcion: Valida si el codigo ingresado por el usuario corresponde a un registro dentro de la tabla ubicaciones
    Parametros:
        Input: codigo del proveedor
    
    Return:
         val=True en caso de coincidir, false en caso de no coincidir.
    '''

    try:
        database = ConexionDB()
        if database is None:
            return []
        
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre, apellido FROM proveedores")
        proveedores = cursor.fetchall()
        
        cursor.close()
        database.close()

        listap=[proveedor[0] for proveedor in proveedores]

        if not listap:
            print("Debe haber al menos un proveedor registrado para ingresar un medicamento.")
            return

        if proveedorCodigo in listap:
            val=True
            
        else:
            val=False
            print("Código de proveedor inválido. Intente nuevamente.")
        return(val)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return []


def ImprimirUbicaciones():
    '''
    Descripcion: Lee los registros dentro de la tabla ubicaciones y los imprime

    Parametros:
        Input: None
        Output: registros dentro de la tabla ubicaciones.
    
    Return:
         None
    '''
    try:
        database = ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre FROM ubicaciones")
        ubicaciones = cursor.fetchall()
        
        cursor.close()
        database.close()

        if ubicaciones:
  
            for ubicacion in ubicaciones:
                print(f"Código: {ubicacion[0]}, Nombre: {ubicacion[1]}")
        else:
            print("No hay ubicaciones registradas.")

    
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return []
    

def ValidarUbicacion(ubicacionCodigo):
    '''
    Descripcion: Valida si el codigo ingresado por el usuario corresponde a un registro dentro de la tabla ubicaciones
    Parametros:
        Input: codigo de la ubicacion
    
    Return:
         val=True en caso de coincidir, false en caso de no coincidir.
    '''

    try:
        database = ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre FROM ubicaciones")
        ubicaciones = cursor.fetchall()
        
        cursor.close()
        database.close()
        listau= [ubicacion[0] for ubicacion in ubicaciones]
   
        if not listau:
            print("Debe haber al menos una ubicacion registrada para ingresar un medicamento.")
            return

        if ubicacionCodigo in listau:
            val=True
        else:
            val=False
            print("Código de ubicacion inválido. Intente nuevamente.")
        return(val)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return []
    

def ExistenciaProveedor(codigo):
    '''
    Descripcion: Valida si el codigo del proveedor coincide con uno existente en la base de datos.

    Parametros:
        Input: codigo del proveedor
    
    Return:
         Existencia=True en caso de coincidir, false en caso de no coincidir.
    '''
    try:
        database = ConexionDB()
        if database is None:
            Existencia=True
            
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo FROM proveedores")
        proveedores = cursor.fetchall()
        cursor.close()
        database.close()
        listap=[proveedor[0] for proveedor in proveedores]

        if codigo in listap:
            print("=====EL CODIGO INGRESADO YA EXISTE E LA BASE DE DATOS=====")
            Existencia=True

        else :
            Existencia=False
        return(Existencia)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")


def ExistenciaUbicacion(codigo):
    '''
    Descripcion: Valida si el codigo de la coincide con uno existente en la base de datos.

    Parametros:
        Input: codigo de la ubicacion
    
    Return:
         Existencia=True en caso de coincidir, false en caso de no coincidir.
    '''
    try:
        database = ConexionDB()
        if database is None:
            Existencia=True
            
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo FROM ubicaciones")
        ubicaciones = cursor.fetchall()
        cursor.close()
        database.close()
        listau=[ubicacion[0] for ubicacion in ubicaciones]

        if str(codigo) in listau:
            print("=====EL CODIGO INGRESADO YA EXISTE E LA BASE DE DATOS=====")
            Existencia=True

        else :
            Existencia=False
        return(Existencia)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")


def ExistenciaMedicamento(lote):
    '''
    Descripcion: Valida si el lote del medicamento coincide con uno existente en la base de datos.

    Parametros:
        Input: lote del medicamneto
    
    Return:
         Existencia=True en caso de coincidir, false en caso de no coincidir.
    '''
    try:
        database = ConexionDB()
        if database is None:
            Existencia=True
            
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT lote FROM medicamentos")
        medicamentos = cursor.fetchall()
        cursor.close()
        database.close()
        listam=[medicamento[0] for medicamento in medicamentos]

        if str(lote) in listam:
            
            Existencia=True

        else :
            Existencia=False
        return(Existencia)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")

        return False

def ProveedoresVacios():
    '''
    Descripcion: Valida si la tabla proveedores esta vacia.

    Parametros:
        None
    
    Return:
         vacia =True en caso de estar vacia, false en caso de no estar vacia
    '''
    vacia = False
    try:
        database = ConexionDB()
        if database is None:
            return vacia

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT COUNT(*) FROM Proveedores")
        resultado = cursor.fetchone()

        cursor.close()
        database.close()

        vacia = (resultado[0] == 0)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        vacia = False
    return (vacia)


def UbicacionesVacias():
    '''
    Descripcion: Valida si la tabla ubicaciones esta vacia.

    Parametros:
        None
    
    Return:
         vacia =True en caso de estar vacia, false en caso de no estar vacia
    '''
    vacia = False
    try:
        database = ConexionDB()

        if database is None:
            return False

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT COUNT(*) FROM ubicaciones")
        resultado = cursor.fetchone()

        cursor.close()
        database.close()

        vacia = (resultado[0] == 0)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        vacia = False
    return (vacia)
