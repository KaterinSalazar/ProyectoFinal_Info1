'''Katerin Salazar Atehortua - 1007373986'''

from conexion import *
import mysql.connector
from mysql.connector import errorcode
from utils import *

def CrearTablas():
    '''
    Descripcion: Crea tablas "Medicamentos", "usuarios", "ubicaciones", "proveedores" en la base de datos si esta 
    no existen

    Parametros:
        Output: string que me indica si las tablas fueron creadas 
    
    Return:
        None
    '''
    try:
        database = ConexionDB()
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS usuarios(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        user VARCHAR(45),
                        password VARCHAR(45)
                       ) ENGINE=InnoDB''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS proveedores (
                       codigo INT NOT NULL,
                       nombre VARCHAR(50) NOT NULL,
                       apellido VARCHAR(50) NOT NULL,
                       documento VARCHAR(50) NOT NULL,
                       entidad VARCHAR(50),
                       PRIMARY KEY (codigo)
                       ) ENGINE=InnoDB''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS ubicaciones (
                       codigo VARCHAR(10) NOT NULL,
                       nombre VARCHAR(50) NOT NULL,
                       telefono VARCHAR(20),
                       PRIMARY KEY (codigo)
                       ) ENGINE=InnoDB''')
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS Medicamentos (
                       lote VARCHAR(45) NOT NULL PRIMARY KEY,
                       nombreMedicamento VARCHAR(100) NOT NULL,
                       distribuidor VARCHAR(100),
                       cantidadBodega INT NOT NULL,
                       fechaLlegada DATE NOT NULL,
                       precioVenta DECIMAL(10, 2) NOT NULL,
                       proveedorCodigo INT,
                       ubicacionCodigo VARCHAR(10),
                       CONSTRAINT fk_proveedor FOREIGN KEY (proveedorCodigo) REFERENCES proveedores (codigo) ON DELETE CASCADE,
                       CONSTRAINT fk_ubicacion FOREIGN KEY (ubicacionCodigo) REFERENCES ubicaciones (codigo) ON DELETE SET NULL
                       ) ENGINE=InnoDB''')
        database.commit()
        cursor.close()
        database.close()
        print("Tablas creadas correctamente.")

    except mysql.connector.Error as error:

        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Nombre de usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(f"Error al conectar a MySQL: {error}")

def ValoresPredeterminados():
    '''
    Descripcion: Llena las tablas de la base de datos con valores predeterminados si estas se encuenttran vacias

    Parametros:
        None
    
    Return:
        None
    '''
    try:
        database = ConexionDB()
        cursor = database.cursor()
        cursor.execute("USE informatica1")
        # Verifica si la tabla usuarios  está vacía
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        cont_usuarios = cursor.fetchone()[0]

        # Verifica si la tabla proveedores  está vacía
        cursor.execute("SELECT COUNT(*) FROM proveedores")
        cont_proveedores = cursor.fetchone()[0]

        # Verifica si la tabla ubicaciones  está vacía
        cursor.execute("SELECT COUNT(*) FROM ubicaciones")
        cont_ubicaciones = cursor.fetchone()[0]

        # Verifica si la tabla medicamentos  está vacía
        cursor.execute("SELECT COUNT(*) FROM medicamentos")
        cont_mediamentos = cursor.fetchone()[0]

        if cont_usuarios==0:

            sql="INSERT INTO usuarios (user,password) VALUES (%s,%s)"
            values=[
                ('informatica1','bio123'),
                ('katerin','kt123'),
                ('luisa','lu123'),
                ('admin','admin123'),
                ('fingenieria','ing123')

            ]
            cursor.executemany(sql, values)

            database.commit()
        if cont_proveedores==0:
            sql="INSERT INTO proveedores (codigo,nombre,apellido,documento,entidad) VALUES (%s,%s,%s,%s,%s)"
            values=[
                (101,'Cesar','Arredondo','111234256','Alqmed'),
                (102,'Katerin','Salazar','1007373986','Alfa medical S.A.S'),
                (103,'Ximena','Rueda','7098534331','Comedica'),
                (104,'Leidy','Atehortua','709536976','Colfar S.A.S'),
                (105, 'Felipe','Gallego','9837268374','Coodan')
            ]
            cursor.executemany(sql, values)
            database.commit()
        if cont_ubicaciones==0:
            sql="INSERT INTO ubicaciones (codigo,nombre,telefono) VALUES (%s,%s,%s)"
            values=[
                ('2012','Hospital San Vicente','60498212'),
                ('7829','Hospital Pablo Tobón Uribe','60498328'),
                ('5562','Hospital Alma Mater de Antioquia','60482932'),
                ('9823','Clínica del Norte','60472812')
            ]
            cursor.executemany(sql, values)
            database.commit()
        if cont_mediamentos==0:
            sql="INSERT INTO medicamentos (lote,nombreMedicamento,distribuidor,cantidadBodega,fechaLlegada,precioVenta,proveedorCodigo,ubicacionCodigo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values=[
                (2314,'Aripiprazol','Fedifar',87,'2024-07-09',7890.23,102,'7829'),
                (98272,'Bisoprolol','Asmed',45,'2024-06-28',12378.45,105,'2012'),
                (76523,'Dexketoprofeno','Disfarma',98,'2024-06-03',35683.09,103,'5562'),
                (98231,'Levotiroxina','Asmed',95,'2024-05-15',14550.78,101,'2012')
            ]
            cursor.executemany(sql, values)
            database.commit()

    except mysql.connector.Error as error:

        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Nombre de usuario o contraseña incorrectos.")

        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")

        else:
            print(f"Error al conectar a MySQL: {error}")

def Datosproveedores():

    '''
    Descripcion: Obtiene y valida datos de proveedores 

    Parametros:
        Output: nombre, apellido, documento, entidad que corresponden al proveedor
    
    Return:
         nombre, apellido, documento, entidad que corresponden al proveedor
    '''
    while True:

        try:
            nombre=input("Ingrese nombre del proveedor: ")
            apellido=input("Ingrese apellido del proveedor: ")

            while True:

                documento=int(input("Ingrese numero de documento del proveedor: "))

                #valida longitud de documento (son de 8 digitos antes de 2004)

                if len(str(documento))<8 or len(str(documento))>10:
                        print("======VALOR INGRESADO CON LONGITUD INCORRECTA=======")
                        continue
                else:
                    break

            entidad=input("Ingrese entidad a la que pertenece el proveedor: ")
            return(nombre,apellido,documento,entidad)
        
        except ValueError:

            print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
            continue
    

def DatosUbicacion():
  
    '''
    Descripcion: Obtiene y valida datos de ubicaciones 

    Parametros:
        Output: nombre, telefono que corresponden a la ubicacion
    
    Return:
        nombre, telefono que corresponden a la ubicacion
    '''
    while True:

        try:
            nombre=input("Ingrese nombre de ubicacion: ")

            while True:
             telefono=int(input("Ingrese numero de telefono:  "))

            # valida longitud del telefono ingresado

             if len(str(telefono))<7 or len(str(telefono))>12:
                    print("======VALOR INGRESADO CON LONGITUD INCORRECTA=======")
                    continue
             else:
                 break
            return(nombre,telefono)
        
        except ValueError:
            print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
            continue

def Datosmedicamentos():
    '''
    Descripcion: Obtiene y valida datos de medicamentos

    Parametros:
        Output: nombre, distribuidor, stock, fecha, precio venta, proveedor y ubicacion 
                 que corresponden al medicamento
    
    Return:
         variables nombreMedicamento, distribuidor, cantidadBodega, fechaLlegada, precioVenta, proveedorCodigo y 
         ubicacionCodigo que corresponden al medicamento
    '''
    while True:

        try:
            nombreMedicamento=input("Ingrese nombre del medicamento: ")
            distribuidor=input(f"Ingrese distribuidor correspondiente para {nombreMedicamento}: ")
            cantidadBodega=int(input(f"Ingrese cantidad de unidades de {nombreMedicamento} disponibles en bodega: "))

            while True:
             fecha=input("Ingrese fecha de llegada del medicamento: ")
             #Llamado a funcion validar fecha encontrada en utils.py
             fechaLlegada=ValidarFecha(fecha)

             if fechaLlegada:

                 break
 
            precioVenta=float(input(f"Ingrese precio de venta para {nombreMedicamento} con hasta dos cifras decimales: "))

            while True:
                print("\n=====LISTA DE PROVEEDORES======\n")
                ImprimirProveedores()
                proveedorCodigo = int(input("Ingrese el código del proveedor: "))
                val=ValidarProveedor(proveedorCodigo)
                if val==True:
                    break

            while True:
                print("\n=====LISTA DE UBICACIONES======\n")
                ImprimirUbicaciones()
                ubicacionCodigo=input(f"Ingrese el codigo de la ubicacion del medicamento: ")
                val=ValidarUbicacion(ubicacionCodigo)
                if val==True:

                    break
            return(nombreMedicamento,distribuidor,cantidadBodega,fecha,precioVenta,proveedorCodigo,ubicacionCodigo)
        
        except ValueError:
            print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
            continue


def CrearProveedor(codigo):
    '''
    Descripcion: Crea un nuevo proveedor en la base de datos

    Parametros:
        input: codigo del nuevo proveedor ingresado por consola
        Output: string que indica que el proveedor fue creado
    
    Return:
        None
    '''
    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        nombre,apellido,documento,entidad=Datosproveedores()
        sql="INSERT INTO proveedores (codigo,nombre,apellido,documento,entidad) VALUES (%s,%s,%s,%s,%s)"
        values=(codigo,nombre,apellido,documento,entidad)
        cursor.execute(sql, values)
        database.commit()

        print(".......Nuevo Proveedor Creado.......")

    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        print("=======PROVEEDOR NO CREADO EN LA BASE DE DATOS=========")  

def CrearUbicacion(codigo):

    '''
    Descripcion: Crea una nueva ubicacion en la base de datos

    Parametros:
        input: codigo de la nueva ubicacion ingresado por consola.
        Output: string que indica que la ubicacion fue creada.
    
    Return:
        None
    '''

    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        nombre,telefono=DatosUbicacion()

        sql="INSERT INTO ubicaciones (codigo,nombre,telefono) VALUES (%s,%s,%s)"
        values=(codigo,nombre,telefono)
        cursor.execute(sql, values)
        database.commit()

        print(".......Nueva Ubicacion Creada.......")

    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        print("=======UBICACION NO CREADA EN LA BASE DE DATOS=========")  


def CrearMedicamento(lote):
    '''
    Descripcion: Crea un nuevo medicamento en la base de datos

    Parametros:
        input: lote del nuevo medicamento ingresado por consola
        Output: string que indica que el medicamento fue creado
    
    Return:
        None
    '''
    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        nombreMedicamento,distribuidor,cantidadBodega,fecha,precioVenta,proveedorCodigo,ubicacionCodigo=Datosmedicamentos()
        sql="INSERT INTO medicamentos (lote,nombreMedicamento,distribuidor,cantidadBodega,fechaLlegada,precioVenta,proveedorCodigo,ubicacionCodigo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(lote,nombreMedicamento,distribuidor,cantidadBodega,fecha,precioVenta,proveedorCodigo,ubicacionCodigo)
        cursor.execute(sql, values)
        database.commit()

        print(".......Nueva Medicamento Creado.......")

    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        print("=======MEDICAMENTO NO CREADO EN LA BASE DE DATOS=========")  


def ActualizarMedicamento(lote):
    '''
    Descripcion: Despliega un menu que le permite al usuario elegir que dato desea actualizar de un medicamento
                 asociado a un codigo ingresado y lo actualiza en la base de datos.

    Parametros:
        input: lote del medicamento a actualizar ingresado por consola.
        Output: string que indica que el medicamento fue actualizado.
    
    Return:
        None
    '''
    while True:
        try:
            database=ConexionDB()
            if database is None:
                return []

            cursor = database.cursor()
            cursor.execute("USE informatica1")
            try:
                opcion=int(input('''
                                ========Ingrese la opcion Correspondiente al dato a actualizar============
                                1. Nombre Medicamento
                                2. Distribuidor
                                3. Cantidad en Bodega
                                4. Fecha de llegada
                                5. Precio de Venta
                                6. Codigo de proveedor
                                7. Codigo de ubicacion
                                8. Actualizar registro completo
                                >'''))
                if opcion==1:
                    nombreMedicamento=input("Ingrese nuevo nombre para medicamento: ")
                    sql = "UPDATE medicamentos SET nombreMedicamento = %s WHERE lote = %s"
                    val = (nombreMedicamento,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==2:
                    distribuidor=input("Ingrese nuevo Distribuidor: ")
                    sql = "UPDATE medicamentos SET distribuidor = %s WHERE lote = %s"
                    val = (distribuidor,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==3:  
                    while True : 
                        cantidadBodega=int(input("Ingrese nueva Cantidad en bodega: "))
                        break
                    sql = "UPDATE medicamentos SET cantidadBodega = %s WHERE lote = %s"
                    val = (cantidadBodega,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==4:
                    while True:
                        fecha=input("Ingrese fecha de llegada del medicamento: ")
                        fechaLlegada=ValidarFecha(fecha)
                        if fechaLlegada:

                            break
                    sql = "UPDATE medicamentos SET fechaLlegada = %s WHERE lote = %s"
                    val = (fecha,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==5:
                    while True:
                        precioVenta=float(input("Ingrese uevo valor de venta: "))
                        break
                    sql = "UPDATE medicamentos SET precioVenta = %s WHERE lote = %s"
                    val = (precioVenta,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==6:
                    while True:
                        print("\n=====LISTA DE PROVEEDORES======\n")
                        ImprimirProveedores()
                        proveedorCodigo= int(input("Ingrese nuevo código del proveedor: "))
                        val=ValidarProveedor(proveedorCodigo)
                        if val==True:
                            break

                    sql = "UPDATE medicamentos SET proveedorCodigo = %s WHERE lote = %s"
                    val = (proveedorCodigo,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==7:
                    while True:
                        print("\n=====LISTA DE UBICACIONES======\n")
                        ImprimirUbicaciones()
                        ubicacionCodigo=input(f"Ingrese el codigo de la nueva ubicacion del medicamento: ")
                        val=ValidarUbicacion(ubicacionCodigo)
                        if val==True:
                            break

                    sql = "UPDATE medicamentos SET ubicacionCodigo = %s WHERE lote = %s"
                    val = (ubicacionCodigo,lote)

                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==8:
                    nombreMedicamento,distribuidor,cantidadBodega,fecha,precioVenta,proveedorCodigo,ubicacionCodigo=Datosmedicamentos()
                    
                    sql = "UPDATE medicamentos SET nombreMedicamento = %s WHERE lote = %s"
                    val = (nombreMedicamento,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET distribuidor = %s WHERE lote = %s"
                    val = (distribuidor,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET cantidadBodega = %s WHERE lote = %s"
                    val = (cantidadBodega,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET fechaLlegada = %s WHERE lote = %s"
                    val = (fecha,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET precioVenta = %s WHERE lote = %s"
                    val = (precioVenta,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET proveedorCodigo = %s WHERE lote = %s"
                    val = (proveedorCodigo,lote)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE medicamentos SET ubicacionCodigo = %s WHERE lote = %s"
                    val = (ubicacionCodigo,lote)
                    cursor.execute(sql, val)
                    database.commit()
                                
                else:
                    print("El numero ingresado no corresponde a ninguna de las opciones del menu")
                    continue
            
            except ValueError:
                print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
                continue

        except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ACTUALIZADO=========")
            continue

        print(".....Registro Actualizado Corretamente.....")
        break        


def ActualizarProveedor(codigo):
    '''
    Descripcion: Despliega un menu que le permite al usuario elegir que dato desea actualizar de un proveedor
                 asociado a un codigo ingresado y lo actualiza en la base de datos.

    Parametros:
        input: codigo del proveedor a actualizar ingresado por consola.
        Output: string que indica que el proveedor fue actualizado.
    
    Return:
        None
    '''
    while True:
        try:
            database=ConexionDB()
            if database is None:
                return []

            cursor = database.cursor()
            cursor.execute("USE informatica1")
            try:
                opcion=int(input('''
                                ========Ingrese la opcion Correspondiente al dato a actualizar============
                                1. Nombre 
                                2. Apellido
                                3. Documento
                                4. Entidad
                                5. Actualizar registro completo
                                >'''))
                
                if opcion==1:
                    nombre=input("Ingrese nuevo nombre para el proveedor: ")
                    sql = "UPDATE proveedores SET nombre = %s WHERE codigo = %s"
                    val = (nombre,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==2:
                    apellido=input("Ingrese nuevo apellido para el proveedor: ")
                    sql = "UPDATE proveedores SET apellido = %s WHERE codigo = %s"
                    val = (apellido,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==3:
                    while True:
                        documento=int(input("Ingrese numero de documento del proveedor: "))
                        if len(str(documento))<8 or len(str(documento))>10:
                            print("======VALOR INGRESADO CON LONGITUD INCORRECTA=======")
                            continue
                        else:
                         break

                    sql = "UPDATE proveedores SET documento = %s WHERE codigo = %s"
                    val = (documento,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==4:
                    entidad=input("Ingrese nueva entidad para el proveedor: ")
                    sql = "UPDATE proveedores SET entidad = %s WHERE codigo = %s"
                    val = (entidad,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==5:
                    nombre,apellido,documento,entidad=Datosproveedores()

                    sql = "UPDATE proveedores SET nombre = %s WHERE codigo = %s"
                    val = (nombre,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE proveedores SET apellido = %s WHERE codigo = %s"
                    val = (apellido,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE proveedores SET documento = %s WHERE codigo = %s"
                    val = (documento,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE proveedores SET entidad = %s WHERE codigo = %s"
                    val = (entidad,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                else:
                    print("El numero ingresado no corresponde a ninguna de las opciones del menu")
                    continue

            except ValueError:
                print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
                continue

        except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ACTUALIZADO=========")
            continue

        print(".....Registro Actualizado Corretamente.....")
        break


def ActualizarUbicacion(codigo):
    '''
    Descripcion: Despliega un menu que le permite al usuario elegir que dato desea actualizar de una ubicacion
                 asociada a un codigo ingresado y lo actualiza en la base de datos.

    Parametros:
        input: codigo de la ubicacion a actualizar ingresado por consola.
        Output: string que indica que la ubicacion fue actualizado.
    
    Return:
        None
    '''
    while True:
        try:
            database=ConexionDB()
            if database is None:
                return []

            cursor = database.cursor()
            cursor.execute("USE informatica1")

            try:
                opcion=int(input('''
                                ========Ingrese la opcion Correspondiente al dato a actualizar============
                                1. Nombre 
                                2.Telefono
                                3. Actualizar registro completo
                                >'''))
                
                if opcion==1:

                    nombre=input("Ingrese nueva ubicacion: ")
                    sql = "UPDATE ubicaciones SET nombre = %s WHERE codigo = %s"
                    val = (nombre,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==2:

                    while True:
                        telefono=int(input("Ingrese numero de telefono"))
            
                        if len(str(telefono))<7 or len(str(telefono))>12:
                            print("======VALOR INGRESADO CON LONGITUD INCORRECTA=======")
                        else:
                            break
    
                
                    sql = "UPDATE ubicaciones SET telefono = %s WHERE codigo = %s"
                    val = (telefono,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                elif opcion==3:
                    nombre,telefono=DatosUbicacion()

                    sql = "UPDATE ubicaciones SET nombre = %s WHERE codigo = %s"
                    val = (nombre,codigo)
                    cursor.execute(sql, val)
                    database.commit()

                    sql = "UPDATE ubicaciones SET telefono = %s WHERE codigo = %s"
                    val = (telefono,codigo)
                    cursor.execute(sql, val)
                    database.commit()
                
                else:
                    print("El numero ingresado no corresponde a ninguna de las opciones del menu")
                    continue

            except ValueError:
                print("=====INGRESE VALOR VALIDO PARA EL CAMPO=====")
                continue

        except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ACTUALIZADO=========")
            continue
        print(".....Registro Actualizado Corretamente.....")
        break

   
def EliminarMedicamento(lote): 
    '''
    Descripcion: Valida si el usuario desea eliminar un registro de un medicamento y lo elimina.
    Parametros:
        input: lote del medicamento a eliminar ingresado por consola. VARCHAR
        Output: string que indica que el medicamento fue eliminado.
    
    Return:
        None
    '''
    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        sql="DELETE FROM medicamentos WHERE lote = %s"
        values=(lote,)
        cursor.execute(sql,values)
        database.commit()
        print(".....Registro Eliminado Corretamente.....")

    except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ELIMINADO=========")



def EliminarProveedor(codigo):
    '''
    Descripcion: Valida si el usuario desea eliminar un registro de un proveedor y lo elimina.
    Parametros:
        input: codigo del proveedor a eliminar ingresado por consola. INT
        Output: string que indica que el medicamento fue eliminado.
    
    Return:
        None
    '''
    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        sql="DELETE FROM proveedores WHERE codigo = %s"
        values=(codigo,)
        cursor.execute(sql,values)
        database.commit()

        
        print("\n.....Registro Eliminado Corretamente.....\n")


    except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ELIMINADO=========")


        
def EliminarUbicacion(codigo):
    '''
    Descripcion: Valida si el usuario desea eliminar un registro de una ubicacion y lo elimina.
    Parametros:
        input: codigo de la ubicacion a eliminar ingresado por consola.
        Output: string que indica que la ubicacion fue eliminada.
    
    Return:
        None
    '''
    try:
        database=ConexionDB()
        if database is None:
            return []

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        sql="DELETE FROM ubicaciones WHERE codio = %s"
        values=(codigo,)
        cursor.execute(sql,values)
        database.commit()
        print(".....Registro Eliminado Corretamente.....")

    except mysql.connector.Error as error:
            print(f"Error al conectar a MySQL: {error}")
            print("=======REGISTRO NO ELIMINADO=========")

 

def MostrarUbicaciones():
    '''
    Descripcion: Lee todos los datos encontrados en la la tabla ublicaciones dentro de la base de datos y las imprime
    Parametros:
        Output: Registros de la tabla ubicaciones
    
    Return:
        None
    '''
    try:
        database = ConexionDB()
        if database is None:
            return

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre, telefono FROM ubicaciones")
        ubicaciones = cursor.fetchall()

        print("\nInformación de Ubicaciones:")
        print("-" * 40)
        for ubicacion in ubicaciones:
            print(f"Código: {ubicacion[0]}")
            print(f"Nombre: {ubicacion[1]}")
            print(f"Teléfono: {ubicacion[2]}")
            print("-" * 40)

        cursor.close()
        database.close()
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")


def MostrarProveedores():
    '''
    Descripcion: Lee todos los datos encontrados en la la tabla proveedores dentro de la base de datos y las imprime
    Parametros:
        Output: Registros de la tabla proveedores
    
    Return:
        None
    '''
    try:
        database = ConexionDB()
        if database is None:
            return

        cursor = database.cursor()
        cursor.execute("USE informatica1")
        cursor.execute("SELECT codigo, nombre, apellido, documento, entidad FROM proveedores")
        proveedores = cursor.fetchall()

        print("\nInformación de Proveedores:")
        print("-" * 40)
        for proveedor in proveedores:
            print(f"Código: {proveedor[0]}")
            print(f"Nombre: {proveedor[1]}")
            print(f"Apellido: {proveedor[2]}")
            print(f"Número de Documento: {proveedor[3]}")
            print(f"Entidad: {proveedor[4]}")
            print("-" * 40)

        cursor.close()
        database.close()
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")


def MostrarMedicamentos():
    '''
    Descripcion: Lee todos los datos encontrados en la la tabla medicamentos dentro de la base de datos,
     crea una consulta mediante llaves foraneas en la tabla ubicaciones y proveedores y las asocia al codigo
     dentro de la tabla medicamentos las imprime.

    Parametros:
        Output: Registros de la tabla medicamentos, ubicaciones y proveedores asociados
    
    Return:
        None
    '''
    try:
        database = ConexionDB()
        if database is None:
            return

        cursor = database.cursor()
        cursor.execute("USE informatica1")

        #consulta sql para llamar datos de las tablas ubicaciones y proveedores

        sql = '''
        SELECT 
            m.lote, 
            m.nombreMedicamento, 
            m.distribuidor, 
            m.cantidadBodega, 
            m.fechaLlegada, 
            m.precioVenta, 
            p.codigo AS proveedorCodigo, 
            p.nombre AS proveedorNombre, 
            p.apellido AS proveedorApellido, 
            u.codigo AS ubicacionCodigo, 
            u.nombre AS ubicacionNombre
        FROM 
            Medicamentos m
        JOIN 
            Proveedores p ON m.proveedorCodigo = p.codigo
        JOIN 
            ubicaciones u ON m.ubicacionCodigo = u.codigo
        '''
        cursor.execute(sql)
        medicamentos = cursor.fetchall()

        print("\nInformación de Medicamentos:")
        print("-" * 80)
        for medicamento in medicamentos:
            print(f"Lote: {medicamento[0]}")
            print(f"Nombre del Medicamento: {medicamento[1]}")
            print(f"Distribuidor: {medicamento[2]}")
            print(f"Cantidad en Bodega: {medicamento[3]}")
            print(f"Fecha de Llegada: {medicamento[4]}")
            print(f"Precio de Venta: {medicamento[5]}")
            print(f"Código del Proveedor: {medicamento[6]}")
            print(f"Nombre del Proveedor: {medicamento[7]} {medicamento[8]}")
            print(f"Código de la Ubicación: {medicamento[9]}")
            print(f"Nombre de la Ubicación: {medicamento[10]}")
            print("-" * 80)

        cursor.close()
        database.close()
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")



def login(user, password):
    '''
    Descripcion: Valida si el usuario y contraseña ingresados por consola corresponden a un regisro 
    dentro de la tabla usuarios de la base de datos.

    Parametros:
        Input: usuario y contraseña solicitados por consola.
        Output: string que me indica  si no esta en la base de datos.
    
    Return:
         val=True en caso de coincidir, false en caso de no coincidir con un registro 
    '''
    try:
        database = ConexionDB()
        if database is None:
            val=False

        cursor= database.cursor()
        cursor.execute("USE informatica1")
        sql= "SELECT COUNT(*) FROM usuarios WHERE user = %s AND password = %s"
        cursor.execute(sql, (user, password))
        resultado= cursor.fetchone()
        cursor.close()
        database.close()
        val=resultado[0] == 1
 
        return(val)
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        print("=======USUARIO O CONTRASEÑA INCORRECTOS=====")










            
