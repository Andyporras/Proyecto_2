import tkinter
from tkinter import *
from tkinter import messagebox


def menu():
       

    ventana= Tk()

    ventana.geometry("600x600+0+0")
    ventana.title("Menú")
    ventana.configure(background="blue")
    #entry=tkinter.Entry(ventana,show="*")
    #entry.grid(column=3,row=6)
    #entry.focus()

    """
    receta para crear menús
    paso 1. crear la barra de Menús
    """
    barraMenu=Menu(ventana)
    #paso 2. Crear los Menús
    mnuArchivo=Menu(barraMenu,background="red")

    # Paso 3. Crear los comandos de los menús
    def mensaje():
            answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
            if(answer):
                    ventana.destroy()
    
    def Mantenimiento():
        ventana.destroy()
        def mensaje1():
            answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
            if(answer):
                ventAbrir.destroy()
                return menu()
                

        def Gestion_de_empresa():
            ventAbrir.destroy()
            def mensajeEmpresa():
                answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
                if(answer):
                    vetana_de_gestion_de_empresa.destroy()
                    return Mantenimiento()
                
            vetana_de_gestion_de_empresa=Tk()
            vetana_de_gestion_de_empresa.geometry("400x200+100+100")
            vetana_de_gestion_de_empresa.title("Gestion de empresa")
            vetana_de_gestion_de_empresa.config(width=300, height=200)
            barraEmpresa=Menu(vetana_de_gestion_de_empresa)
            menuEmpresa=Menu(barraEmpresa)
            
            menuEmpresa.add_command(label="incluir empresa",)
            menuEmpresa.add_command(label="eliminar empresa")
            menuEmpresa.add_command(label="modificar empresa")
            menuEmpresa.add_command(label="mostrar empresas")
            
            menuEmpresa.add_separator()
            menuEmpresa.add_command(label="Salir de gestion de empresa",command=mensajeEmpresa)
            barraEmpresa.add_cascade(label="gestion de empresa",menu=menuEmpresa)
            vetana_de_gestion_de_empresa.config(menu=barraEmpresa)

            vetana_de_gestion_de_empresa.mainloop()
        def transporte():
            def mensajeTransporte():
                answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
                if(answer):
                    ventanaDETransporte.destroy()
            ventanaDETransporte=Tk()
            ventanaDETransporte.geometry("300x200+100+100")
            ventanaDETransporte.title("Transporte")
            barraTransporte=Menu(ventanaDETransporte)
            menuTransporte=Menu(barraTransporte)
            menuTransporte.add_command(label="incluir empresa",)
            menuTransporte.add_command(label="eliminar empresa")
            menuTransporte.add_command(label="modificar empresa")
            menuTransporte.add_command(label="mostrar empresas")
            
            menuTransporte.add_separator()
            menuTransporte.add_command(label="Salir de gestion de empresa",command=mensajeTransporte)
            barraTransporte.add_cascade(label="Transporte",menu=menuTransporte)
            ventanaDETransporte.config(menu=barraTransporte)

            ventanaDETransporte.mainloop()
        def gestion_De_viaje():
            def mensajeViaje():
                aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                if(aceptar):
                        ventanaViaje.destroy()
            ventanaViaje=Tk()
            ventanaViaje.geometry("300x200+100+100")
            ventanaViaje.title("viaje")
            barraViaje=Menu(ventanaViaje)
            menuViaje=Menu(barraViaje)
            menuViaje.add_command(label="incluir Viaje",)
            menuViaje.add_command(label="eliminar Viaje")
            menuViaje.add_command(label="modificar Viaje")
            menuViaje.add_command(label="mostrar Viaje")
            
            menuViaje.add_separator()
            menuViaje.add_command(label="Salir de gestion de Viaje",command=mensajeViaje)
            barraViaje.add_cascade(label="Viaje",menu=menuViaje)
            ventanaViaje.config(menu=barraViaje)
            ventanaViaje.mainloop()

            
                

        ventAbrir=Tk()
        ventAbrir.geometry("400x200+100+100")
        ventAbrir.title("Mantenimiento")
        ventAbrir.configure(background="blue")
        barraMenu1=Menu(ventAbrir)
        mnuEdicion=Menu(barraMenu1,background="red")
        entry=tkinter.Entry(ventAbrir,show="*")
        entry.grid(column=3,row=6)
        #entry.focus()
        ventAbrir.config(menu=barraMenu1)
        def clicker():
            respuesta=entry.get()
            if(respuesta=="12345"):
                entry.destroy()
                boton.destroy()
                def historial_De_reservaciones():
                        def mensaje_Historial():
                            aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                            if(aceptar):
                                ventana_Historial.destroy()
                        ventana_Historial=Tk()
                        ventana_Historial.geometry("300x200+100+100")
                        ventana_Historial.title("historial de reservaciones")
                        barra_Historial=Menu(ventana_Historial)
                        menu_Historial=Menu(barra_Historial)
                        menu_Historial.add_command(label="Rango de fecha de salida")
                        menu_Historial.add_command(label="Rango de fecha de llegada")
                        menu_Historial.add_command(label="Rango de fecha de la reservación")
                        menu_Historial.add_command(label="Lugar de salida y llegada.")
                    
                        menu_Historial.add_separator()
                        menu_Historial.add_command(label="Salir de historial de reservaciones",command=mensaje_Historial)
                        barra_Historial.add_cascade(label="historial de reservaciones",menu=menu_Historial)
                        ventana_Historial.config(menu=barra_Historial)
                        ventana_Historial.mainloop()
                """def Estadistica_de_Viaje():
                        def mensaje_Estadisticas():
                            aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                            if(aceptar):
                                ventana_Estadistica.destroy()
                        ventana_Estadistica=Tk()
                        ventana_Estadistica.geometry("300x200+100+100")
                        ventana_Estadistica.title("Estadistica_de_Viaje")
                        barra_Estadistica=Menu(ventana_Estadistica)
                        menu_Estadistica=Menu(barra_Estadistica)
                        menu_Estadistica.add_command(label="Rango de fecha de salida")
                        menu_Estadistica.add_command(label="Rango de fecha de llegada")
                        menu_Estadistica.add_command(label="Rango de fecha de la reservación")
                        menu_Estadistica.add_command(label="Lugar de salida y llegada.")
                    
                        menu_Estadistica.add_separator()
                        menu_Estadistica.add_command(label="Salir de historial de reservaciones",command=mensaje_Estadisticas)
                        barra_Estadistica.add_cascade(label="Estadistica_de_Viaje",menu=menu_Estadistica)
                        ventana_Estadistica.config(menu=barra_Estadistica)
                        ventana_Estadistica.mainloop()
                       """ 
                mnuEdicion.add_command(label="Gestión de empresas",command=Gestion_de_empresa)
                mnuEdicion.add_command(label="Gestión de transporte por empresa",command=transporte)
                
                        
                mnuEdicion.add_command(label="Gestión de viaje",command=gestion_De_viaje)
                mnuEdicion.add_command(label="Consultar historial de reservaciones",command=historial_De_reservaciones)
                mnuEdicion.add_command(label=" Estadísticas de viaje")
                
                mnuEdicion.add_separator()
                mnuEdicion.add_command(label="Salir de mantenimiento",command=mensaje1)
                barraMenu1.add_cascade(label="Mantenimiento",menu=mnuEdicion)
                


        boton=tkinter.Button(ventAbrir,text="continuar",bg="gray",fg="black",command=clicker)
        boton.grid(column=6,row=6)
        
        ventAbrir.mainloop()


    mnuArchivo.add_command(label="Opciones administrativas",command=Mantenimiento)
    mnuArchivo.add_command(label="Opciones de usuario normal",command=busquedas_avanzadas)
    mnuArchivo.add_separator()
    mnuArchivo.add_command(label="Salir", command=mensaje)
    #-------------------------------------------

    #Paso 4. Agregar los Menús a la barra de menús
    barraMenu.add_cascade(label="Menú",menu=mnuArchivo)


    #Paso 5. Indicamos que la barra de menús estara en la ventana
    ventana.config(menu=barraMenu)

    ventana.mainloop()






    



def busquedas_avanzadas():
    
    #ventana.destroy()
    
    def mensaje2():
        answer2=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(answer2):
            ventana_Avanzada.destroy()
    def consulta_Viajes():
        def mensaje_consulta_Viajes():
            aceptar=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
            if(aceptar):
                     ventana_consulta.destroy()
        ventana_consulta=Tk()
        ventana_consulta.geometry("400x200+100+100")
        ventana_consulta.title("consulta_Viajes")
        barra_Consulta=Menu(ventana_consulta)
        menu_Consulta=Menu(barra_Consulta)
        menu_Consulta.add_command(label="Empresa")
        menu_Consulta.add_command(label="Lugar de salida")
        menu_Consulta.add_command(label="Lugar de llegada")
        menu_Consulta.add_command(label="Rango de fecha de salida.")
        menu_Consulta.add_command(label="Rango de fecha de llegada.")
                
                
        menu_Consulta.add_separator()
        menu_Consulta.add_command(label="Salir de consulta de viajes",command=mensaje_consulta_Viajes)
        barra_Consulta.add_cascade(label="consulta_Viajes",menu=menu_Consulta)
        ventana_consulta.config(menu=barra_Consulta)
        ventana_consulta.mainloop()
    def reservacion_de_viajes():
        def mensaje_reservacion():
           aceptar=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
           if(aceptar):
                    vetana_reservacion.destroy()
        ventana_reservacion=Tk()
        ventana_reservacion.geometry("400x200+100+100")
        ventana_reservacion.title("reservacion de viajes")
        barra_reservacion=Menu(ventana_reservacion)
        menu_reservacion=Menu(barra_reservacion)
        menu_reservacion.add_command(label="Salir de reservacion de viajes",command=mensaje_reservacion)
        barra_reservacion.add_cascade(label="reservacion de viajes",menu=menu_reservacion)
        ventana_reservacion.config(menu=barra_reservacion)
        ventana_reservacion.mainloop()
        
        
        

                
    ventana_Avanzada=Tk()
    ventana_Avanzada.geometry("300x200+100+100")
    ventana_Avanzada.title("Busquedas Avanzadas")
    barraMenu2=Menu(ventana_Avanzada)
    menu_avanzado=Menu(barraMenu2)

    menu_avanzado.add_command(label="Consulta de viajes",command=consulta_Viajes)
    menu_avanzado.add_command(label=" Reservación de viaje",command=reservacion_de_viajes)
    menu_avanzado.add_command(label=" Cancelación de reservación")

    menu_avanzado.add_separator()
    menu_avanzado.add_command(label="Salir de Busqueda Avanzadas",command=mensaje2)
    barraMenu2.add_cascade(label="Busquedas Avanzadas",menu=menu_avanzado)
    ventana_Avanzada.config(menu=barraMenu2)

    
    
    

    ventana_Avanzada.mainloop()







menu()
