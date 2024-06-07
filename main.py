'''Katerin Salazar Atehortua - 1007373986'''

from funciones import *
from utils import *

 # creacion de base de datos e ingreso de valores predeterminados

CrearBd()
CrearTablas()
ValoresPredeterminados()

try:
    while True:
        #login
        usuario=input("Ingrese usuario:  ")
        contraseña=input("Ingrese contraseña:  ")
        val=login(usuario,contraseña)
        
        
        if val==True:
            while True:
                try:
                    opcion=int(input('''
                        ========MENU============
                        1. Gestionar Informacion Medicamentos
                        2. Gestionar Informacion Proveedores
                        3. Gestionar Informacion Ubicaciones
                        4. Salir
                        >'''))
                    if opcion==1:
                        while True:
                            
                                op1=int(input('''
                                ========MENU============
                                1. Crear Medicamento
                                2. Actualizar Medicamento
                                3. Eliminar Medicamento
                                4. Mostrar registros de medicamentos
                                5. Volver a menu principal
                                >'''))

                                if op1==1:

                                    while True:

                                        lote=input("Ingrese el lote del nuevo medicamento:  ")
                                        Existencia=ExistenciaMedicamento(lote)

                                        if Existencia==True:
                                            print("=====EL LOTE INGRESADO YA EXISTE EN LA BASE DE DATOS=====")
                                            continue

                                        else:
                                            #verifica si estan vacias las tablas(son llaves foraneas, es necesario la existencia de un registro)
                                            ubicaciones=UbicacionesVacias()
                                            proveedores=ProveedoresVacios()
                                            if ubicaciones==False and proveedores==False:
                                                CrearMedicamento(lote)
                                                break
                                            else:
                                                print("Debe existir al menos un registro de ubicaciones y proveedores para crear un medicamento.")

                                elif op1==2:

                                    while True:
                                        lote=input("Ingrese el lote del medicamento que desea actualizar: ")
                                        Existencia=ExistenciaMedicamento(lote)

                                        if Existencia==True:
                                            ActualizarMedicamento(lote)
                                            break
                                        else:
                                            print("========EL LOTE INGRESADO NO SE ENCUENTRA EN LA BASE DE DATOS=========")
                                            continue

                                elif op1==3:

                                    while True:
                                        lote=input("Ingrese el lote del medicamento que desea actualizar: ")
                                        Existencia=ExistenciaMedicamento(lote)
                                        if Existencia==True:
                                            #valida si el usuario esta seguro de eliminar el registro.
                                            while True:
                                                    conf=int(input(f'''¿Estas seguro de eliminar el registro del lote {lote} ? 
                                                                    
                                                    1. Si, eliminar registro
                                                    2. No, Volver a menu principal
                                                    >'''))
                                                    if conf==1:
                                                        EliminarMedicamento(lote)
                                                        break
                                                    elif conf==2:
                                                        pass
                                                    
                                                    else:
                                                        print("========La opcion ingresada no es valida=======")  
                                                    break
                                            break

                                elif op1==4:               
                                    MostrarMedicamentos()
                                    continue

                                elif op1==5:
                                    print("\n.......Regresando a menu principal.........\n")
                                    break
                                else:
                                    print("==========La opcion ingresada no esta en el menu===========")
                                    continue


                    elif opcion==2:
                        while True:
                            
                                op1=int(input('''
                                ========MENU============
                                1. Crear Proveedor
                                2. Actualizar Proveedor
                                3. Eliminar Proveedor
                                4. Mostrar registros de proveedores
                                4. Volver a menu principal
                                >'''))

                                if op1==1:

                                    while True:
                                        try:
                                            codigo=int(input("Ingrese el Codigo del nuevo proveedor:  "))
                                            Existencia=ExistenciaProveedor(codigo)
                                            if Existencia==True:
                                                print("=====EL CODIGO INGRESADO YA EXISTE EN LA BASE DE DATOS=====")
                                                continue
                                            else:
                                                CrearProveedor(codigo)
                                                break
                                        except ValueError:
                                            print("======INGRESE VALOR VALIDO PARA EL CAMPO=======")
                                            continue
                                        
                                elif op1==2:
                                    while True:
                                        try:
                                            codigo=int(input("Ingrese el codigo del proveedor que desea actualizar: "))
                                            Existencia=ExistenciaProveedor(codigo)

                                            if Existencia==True:
                                                ActualizarProveedor(codigo)
                                                break
                                            else:
                                                print("========EL CODIGO INGRESADO NO SE ENCUENTRA EN LA BASE DE DATOS=========")
                                                continue
                                        except ValueError:
                                            print("======INGRESE VALOR VALIDO PARA EL CAMPO=======")
                                            continue
                                        
                                elif op1==3:
                                    while True:
                                        try:
                                            codigo=int(input("Ingrese el codigo del proveedor que desea eliminar: "))
                                            Existencia=ExistenciaProveedor(codigo)
                                            if Existencia==True:
                                                while True:
                                                        conf=int(input(f'''¿Estas seguro de eliminar el registro del codigo {codigo} ? 
                                                                        
                                                        1. Si, eliminar registro
                                                        2. No, Volver a menu principal
                                                        >'''))
                                                        if conf==1:
                                                            EliminarProveedor(codigo)
                                                            break
                                                        elif conf==2:
                                                            pass
                                                        
                                                    
                                                        else:
                                                            print("========La opcion ingresada no es valida=======")  
                                                        break
                                                break
                                        except ValueError:
                                            print("======INGRESE VALOR VALIDO PARA EL CAMPO=======")
                                            continue
                                        
                                elif op1==4:               
                                    MostrarProveedores()
                                    continue
                                elif op1==5:
                                    print("\n.......Regresando a menu principal.........\n")
                                    break
                                else:
                                    print("==========La opcion ingresada no esta en el menu===========")
                                    continue
                                

                    elif opcion==3:
                        while True:
                            
                                op1=int(input('''
                                ========MENU============
                                1. Crear Ubicacion
                                2. Actualizar Ubicacion
                                3. Eliminar Ubicacion
                                4. Mostrar registros de Ubicacion
                                5. Volver a menu principal
                                >'''))
                            
                                if op1==1:
                                    while True:
                                        codigo=input("Ingrese el Codigo de la  nueva ubicacion:  ")
                                        Existencia=ExistenciaUbicacion(codigo)
                                        if Existencia==True:
                                            print("=====EL CODIGO INGRESADO YA EXISTE EN LA BASE DE DATOS=====")
                                            continue
                                        else:
                                            CrearUbicacion(codigo)
                                            break

                                elif op1==2:
                                    while True:
                                        codigo=input("Ingrese el codigo de la ubicacion que desea actualizar: ")
                                        Existencia=ExistenciaUbicacion(codigo)
                                        if Existencia==True:
                                            ActualizarUbicacion(codigo)
                                            break
                                        else:
                                            print("========EL CODIGO INGRESADO NO SE ENCUENTRA EN LA BASE DE DATOS=========")
                                            continue

                                elif op1==3:
                                    while True:
                                        codigo=input("Ingrese el codigo la ubicacion que desea eliminar: ")
                                        Existencia=ExistenciaUbicacion(codigo)
                                        if Existencia==True:
                                            while True:
                                                    conf=int(input(f'''¿Estas seguro de eliminar el registro del codigo {codigo} ? 
                                                                    
                                                    1. Si, eliminar registro
                                                    2. No, Volver a menu principal
                                                    >'''))
                                                    if conf==1:
                                                        EliminarUbicacion(codigo)
                                                        break
                                                    elif conf==2:
                                                        pass
                                                    
                                                
                                                    else:
                                                        print("========La opcion ingresada no es valida=======")  
                                                    break
                                            break
                                        else:
                                            print("========EL CODIGO INGRESADO NO SE ENCUENTRA EN LA BASE DE DATOS=========")
                                            continue
                                        

                                elif op1==4:               
                                    MostrarUbicaciones()
                                    continue

                                elif op1==5:
                                    print("\n.......Regresando a menu principal.........\n")
                                    break

                                else:
                                    print("==========La opcion ingresada no esta en el menu===========")
                                    continue
                    elif opcion==4:
                        print("***************** HASTA LA PROXIMA!! **********************************")
                        break

                    else: 
                        print("============ La opcion ingresada no se encuentra en el menu =====================")  

                except ValueError:
                        print("======INGRESE VALOR VALIDO PARA EL CAMPO=======")
                        continue
        else:
            print("==========Usuario o contraseña incorrecta============")
            continue
except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        print("=======USUARIO O CONTRASEÑA INCORRECTOS=====")





