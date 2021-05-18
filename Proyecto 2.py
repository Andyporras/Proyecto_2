import tkinter
from tkinter import *
from tkinter import messagebox


def menu():
       

    ventana= Tk()

    ventana.geometry("400x400+0+0")
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
            answer=messagebox.askyesno("Regresar", "¿Desea regresar al menu principal? ")
            if(answer):
                ventAbrir.destroy()
                return menu()
                

        def Gestion_de_empresa():
            ventAbrir.destroy()
            def mensajeEmpresa():
                answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
                if(answer):
                    vetana_de_gestion_de_empresa.destroy()
                    return menu()
            def incluirEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventIncluir=Tk()
                ventIncluir.geometry("400x200+100+100")
                ventIncluir.title("Incluir Empresa")
                ventIncluir.config(width=300, height=200)
                etiqueta=tkinter.Label(ventIncluir,text="Ingrese la cedula jurídica.")
                etiqueta.place(x=80,y=10)
                entry=tkinter.Entry(ventIncluir)
                entry.place(x=80,y=30)
                def continuar():
                    respuesta=entry.get()
                    archivo=open("gestion de empresa.txt")
                    verificar=archivo.readlines()
                    if(len(respuesta) == 10):
                        if((respuesta+"\n") in verificar)==False:
                            archivo=open("gestion de empresa.txt","a")
                            archivo.write(respuesta+"\n")
                            #etiqueta.destroy()
                            #entry.destroy()
                            etiqueta=tkinter.Label(ventIncluir,text="Ingrese el nombre de la empresa.")
                            etiqueta.place(x=80,y=10)
                            #entrada=tkinter.Entry(ventIncluir)
                            #entrada.place(x=80,y=30)
                            #result1=entrada.get()
                            def continuar1():
                                respuesta=entry.get()
                                archivo.write(respuesta+"\n")
                                #etiqueta.destroy()
                                #entrada.destroy()
                                etiqueta=tkinter.Label(ventIncluir,text="Ingrese la provincia de la empresa.")
                                etiqueta.place(x=80,y=10)
                             #   entrada=tkinter.Entry(ventIncluir)
                              #  entrada.place(x=80,y=30)
                               # result2=entrada.get()
                                def continuar2():
                                    respuesta=entry.get()
                                    archivo.write(respuesta+"\n")
                                    etiqueta=tkinter.Label(ventIncluir,text="Ingrese la direccion exacta de la empresa.")
                                    etiqueta.place(x=80,y=10)
                               #     entrada=tkinter.Entry(ventIncluir)
                                #    entrada.place(x=80,y=30)
                                 #   result=entrada.get()
                                    def continuar3():
                                        respuesta=entry.get()
                                        archivo.write(respuesta+"\n")
                                        archivo.write("---------------------"+"\n")
                                        archivo.close()
                                        ventIncluir.destroy()
                                        return menu()
                                    boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar3)
                                    boton.place(x=110,y=70)
                                boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar2)
                                boton.place(x=110,y=70)
                        boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar1)
                        boton.place(x=110,y=70)
                    else:
                        answer=messagebox.askyesno("Error", "La cedula juridica no tiene 10 digitos desea intentar de nuevo.")
                        if(answer):
                            None
                        else:
                            return menu()
                            
                            

                        
                boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar)
                boton.place(x=110,y=70)
                
                ventIncluir.mainloop()
            def eliminarEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventEliminar=Tk()
                ventEliminar.geometry("400x200+100+100")
                ventEliminar.title("Eliminar Empresa")
                ventEliminar.config(width=300, height=200)
                entry=tkinter.Entry(ventEliminar)
                entry.place(x=100,y=30)
                etiqueta=tkinter.Label(ventEliminar,text="Ingrese la cedula juridica de la empresa a eliminar.")
                etiqueta.place(x=80,y=10)
                def Eliminar_empresa_aux():
                    archivo=open("gestion de empresa.txt")
                    comprobar=archivo.readlines()
                    eliminar=entry.get()
                    if(eliminar+"\n" in comprobar):
                        linea=comprobar.index(eliminar+"\n")
                        eliminar=Eliminar_Empresa1_aux(comprobar,linea,0)
                        archivo.close()
                        archivo=open("gestion de empresa.txt","w")
                        archivo.write(eliminar)
                        archivo.close()
                        etiqueta2=tkinter.Label(ventEliminar,text=f"se elimino la siguiente empresa{eliminar} exitosamente")
                        etiqueta2.place(x=70,y=80)
                        
                boton=tkinter.Button(ventEliminar,text="continuar",bg="gray",fg="black",command=Eliminar_empresa_aux)
                boton.place(x=120,y=50)

                ventEliminar.mainloop()
                
            def modificarEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventModificar=Tk()
                ventModificar.geometry("400x200+100+100")
                ventModificar.title("Modificar Empresa")
                ventModificar.config(width=300, height=200)
                etiqueta=tkinter.Label(ventModificar,text="Ingrese la cedula juridica de la empresa a modificar.")
                etiqueta.place(x=70,y=10)
                entry=tkinter.Entry(ventModificar)
                entry.place(x=80,y=30)
                def modificarEmpresa1():
                    result=entry.get()
                    archivo=open("gestion de empresa.txt")
                    empresas=archivo.readlines()
                    if(result+"\n") in empresas:
                        linea=empresas.index(result + "\n")
                        #Mostrar_Empresa(empresas, linea, 0)
                        ventModificar.destroy()
                        empresa_Modificada = Modificar_Empresa_Aux(empresas, linea + 1, 0)#Se creo una variable para ingresar los nuevos datos.
                        #Gestion = open("gestion de empresa.txt", "w")#Se abre el archivo en el modo que deseamos.
                        """
                        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        #Gestion.write(Convertir_A_String(empresa_Modificada))#Se escribe la modificación de la empresa en el archivo.
                        #Gestion.close()#Importante cerrar el archivo.
                        """
                        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        #print("\n", "\t", "\t", "\t","¡empresa modificado con éxito! ", "\n")
                        #return Gestion_de_empresas()
                    
                boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarEmpresa1)
                boton.place(x=100,y=50)

    
                               
            """
            Nombre: mostrar_empresas()
            Entradas:
                El archivo en modo de lectura.
            Salida:
                Va a dar una lista de todos lo contactos existentes en la agenda.
            Restricciones:
                Abrir el archivo de manera correcta.
            """        
            def mostrar_empresas():
                vetana_de_gestion_de_empresa.destroy()
                archivo="gestion de empresa.txt"
                agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
                """
                En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                contador =1
                datos=""
                for linea in agenda:
                    datos+="linea "+str(contador)+" : "+linea+"\n" #Imprimir todos los contactos existentes en la agenda.
                    contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
                agenda.close()#Importante cerrar el archivo.
                ventMostrar=Tk()
                ventMostrar.geometry("300x400")
                ventMostrar.title("Mostrar transporte.")
                etiqueta=tkinter.Label(ventMostrar,text=f"{datos}")
                etiqueta.pack()
                def salir():
                    ventMostrar.destroy()
                    return menu()
                boton=tkinter.Button(ventMostrar,text="salir",bg="gray",fg="black",command=salir)
                boton.pack()
                """
                En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                


                
            vetana_de_gestion_de_empresa=Tk()
            vetana_de_gestion_de_empresa.geometry("400x200+100+100")
            vetana_de_gestion_de_empresa.title("Gestion de empresa")
            vetana_de_gestion_de_empresa.config(width=300, height=200)
            barraEmpresa=Menu(vetana_de_gestion_de_empresa)
            menuEmpresa=Menu(barraEmpresa)
            
            menuEmpresa.add_command(label="incluir empresa",command=incluirEmpresa)
            menuEmpresa.add_command(label="eliminar empresa",command=eliminarEmpresa)
            menuEmpresa.add_command(label="modificar empresa",command=modificarEmpresa)
            menuEmpresa.add_command(label="mostrar empresas",command=mostrar_empresas)
            
            menuEmpresa.add_separator()
            menuEmpresa.add_command(label="Salir de gestion de empresa",command=mensajeEmpresa)
            barraEmpresa.add_cascade(label="gestion de empresa",menu=menuEmpresa)
            vetana_de_gestion_de_empresa.config(menu=barraEmpresa)

            vetana_de_gestion_de_empresa.mainloop()
        def transporte():
            ventAbrir.destroy()
            def mensajeTransporte():
                answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
                if(answer):
                    ventanaDETransporte.destroy()
                    return menu()
            def IncluirTransporte():
                ventanaDETransporte.destroy()
                ventIncluirT=Tk()
                ventIncluirT.geometry("400x200+100+100")
                ventIncluirT.title("Incluir transporte")
                ventIncluirT.config(width=300, height=200)
                etiqueta=tkinter.Label(ventIncluirT,text="ingrese la placa del transporte.")
                etiqueta.place(x=80,y=10)
                entry=tkinter.Entry(ventIncluirT)
                entry.place(x=80,y=30)
                def continuarT():
                    etiqueta.destroy()
                    respuesta=entry.get()
                    archivo=open("Gestion de Transporte.txt","a")
                    archivo=open("Gestion de Transporte.txt")
                    verificar=archivo.readlines()
                    if((respuesta+"\n")in verificar)==False:
                        archivo=open("Gestion de transporte.txt","a")
                        #respuesta=entry.get()
                        archivo.write(respuesta+"\n")
                        etiqueta2=tkinter.Label(ventIncluirT,text="selecione una de las opciones.",font="italic")
                        etiqueta2.place(x=80,y=10)
                        entry.destroy()
                        boton.destroy()
                        def buseta():
                            etiqueta2.destroy()
                            boton1.destroy()
                            boton2.destroy()
                            
                            entry=tkinter.Entry(ventIncluirT)
                            entry.place(x=90,y=50)
                            archivo.write("buseta"+"\n")
                            etiqueta1=tkinter.Label(ventIncluirT,text="ingrese la marca de la buseta.",font="bold")
                            etiqueta1.place(x=80,y=10)
                            def incluirT():
                                boton.destroy()
                                etiqueta1.destroy()
                                marca=entry.get()
                                
                                archivo.write(marca+"\n")
                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese el modelo de la buseta.")
                                etiqueta.place(x=80,y=10)
                                def modeloAux():
                                    etiqueta.destroy()
                                    boton1.destroy()
                                    
                                    
                                    modelo=entry.get()
                                    archivo.write(modelo+"\n")
                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese el año.")
                                    etiqueta1.place(x=80,y=10)
                                    def añoAUX():
                                        boton2.destroy()
                                        etiqueta1.destroy()
                                        año=entry.get()
                                        archivo.write(año+"\n")
                                        etiqueta=tkinter.Label(ventIncluirT,text="seleccione una de las empresas disponible",font="bold")
                                        etiqueta.pack()
                                        mostrar=open("gestion de empresa.txt")
                                        etiqueta2=tkinter.Label(ventIncluirT,text=f"{mostrar.read()}",font="italic")
                                        etiqueta2.pack()
                                        entry.pack()
                                        def empresaAUX():
                                            etiqueta.destroy()
                                            etiqueta2.destroy()
                                            boton.destroy()
                                        
                                            empresa=entry.get()
                                            archivo.write(empresa+"\n")
                                            etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento VIP")
                                            etiqueta1.place(x=80,y=10)
                                            entry.place(x=90,y=30)
                                            def VipAux():
                                                boton1.destroy()
                                                etiqueta1.destroy()
                                                Vip=entry.get()
                                                archivo.write(Vip+"\n")
                                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase normal",font="bold")
                                                etiqueta.place(x=0,y=10)
                                                entry.place(x=90,y=50)
                                                def normalAUX():
                                                    etiqueta.destroy()
                                                    boton.destroy()
                                                    normal=entry.get()
                                                    archivo.write(normal+"\n")
                                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase economico. ")
                                                    etiqueta1.place(x=70,y=10)
                                                    
                                                    def economicoAUX():
                                                        
                                                        economico=entry.get()
                                                        archivo.write(economico+"\n")
                                                        archivo,write("------------------------"+"\n")
                                                        archivo.close()
                                                        ventIncluirT.destroy()
                                                        return menu()
                                                    boton1=tkinter.Button(ventIncluirT,text="continuar",command=economicoAUX)
                                                    boton1.place(x=120,y=80)
                                                boton=tkinter.Button(ventIncluirT,text="continuar",command=normalAUX)
                                                boton.place(x=120,y=80)
                                            boton1=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=VipAux)
                                            boton1.place(x=140,y=100)
                                        boton=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=empresaAUX)
                                        boton.pack()
                                    boton2=tkinter.Button(ventIncluirT,text="agregar",command=añoAUX)
                                    boton2.place(x=120,y=70)
                                boton1=tkinter.Button(ventIncluirT,text="continuar",command=modeloAux)
                                boton1.place(x=120,y=70)
                                
                            boton=tkinter.Button(ventIncluirT,text="continuar",command=incluirT)
                            boton.place(x=130,y=80)

                        def limosina():
                            etiqueta2.destroy()
                            boton1.destroy()
                            boton2.destroy()
                            
                            entry=tkinter.Entry(ventIncluirT)
                            entry.place(x=90,y=50)
                            archivo.write("limosina"+"\n")
                            etiqueta1=tkinter.Label(ventIncluirT,text="ingrese la marca de la limosina.",font="bold")
                            etiqueta1.place(x=80,y=10)
                            def incluirT2():
                                boton.destroy()
                                etiqueta1.destroy()
                                marca=entry.get()
                                
                                archivo.write(marca+"\n")
                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese el modelo de la limosina.")
                                etiqueta.place(x=80,y=10)
                                def modeloAux2():
                                    etiqueta.destroy()
                                    boton1.destroy()
                                    
                                    
                                    modelo=entry.get()
                                    archivo.write(modelo+"\n")
                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese el año.")
                                    etiqueta1.place(x=80,y=10)
                                    def añoAUX2():
                                        boton2.destroy()
                                        etiqueta1.destroy()
                                        año=entry.get()
                                        archivo.write(año+"\n")
                                        etiqueta=tkinter.Label(ventIncluirT,text="seleccione una de las empresas disponible",font="bold")
                                        etiqueta.pack()
                                        mostrar=open("gestion de empresa.txt")
                                        etiqueta2=tkinter.Label(ventIncluirT,text=f"{mostrar.read()}",font="italic")
                                        etiqueta2.pack()
                                        entry.pack()
                                        def empresaAUX2():
                                            etiqueta.destroy()
                                            etiqueta2.destroy()
                                            boton.destroy()
                                        
                                            empresa=entry.get()
                                            archivo.write(empresa+"\n")
                                            etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento VIP")
                                            etiqueta1.place(x=80,y=10)
                                            entry.place(x=90,y=30)
                                            def VipAux2():
                                                boton1.destroy()
                                                etiqueta1.destroy()
                                                Vip=entry.get()
                                                archivo.write(Vip+"\n")
                                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase normal",font="bold")
                                                etiqueta.place(x=0,y=10)
                                                entry.place(x=90,y=50)
                                                def normalAUX2():
                                                    etiqueta.destroy()
                                                    boton.destroy()
                                                    normal=entry.get()
                                                    archivo.write(normal+"\n")
                                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase economico. ")
                                                    etiqueta1.place(x=70,y=10)
                                                    
                                                    def economicoAUX2():
                                                        
                                                        economico=entry.get()
                                                        archivo.write(economico+"\n")
                                                        archivo,write("------------------------"+"\n")
                                                        archivo.close()
                                                        ventIncluirT.destroy()
                                                        return menu()
                                                    boton1=tkinter.Button(ventIncluirT,text="continuar",command=economicoAUX2)
                                                    boton1.place(x=120,y=80)
                                                boton=tkinter.Button(ventIncluirT,text="continuar",command=normalAUX2)
                                                boton.place(x=120,y=80)
                                            boton1=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=VipAux2)
                                            boton1.place(x=140,y=100)
                                        boton=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=empresaAUX2)
                                        boton.pack()
                                    boton2=tkinter.Button(ventIncluirT,text="agregar",command=añoAUX2)
                                    boton2.place(x=120,y=70)
                                boton1=tkinter.Button(ventIncluirT,text="continuar",command=modeloAux2)
                                boton1.place(x=120,y=70)
                                
                            boton=tkinter.Button(ventIncluirT,text="continuar",command=incluirT2)
                            boton.place(x=130,y=80)

                            
                            
                            
                        boton1=tkinter.Button(ventIncluirT,text="Buseta",command=buseta)
                        boton1.place(x=70,y=50)
                        boton2=tkinter.Button(ventIncluirT,text="limosina",command=limosina)
                        boton2.place(x=150,y=50)
                        
                    else:
                        mensaje=messagebox.askyesno("Error","Error, Digite una palca que no este repetido. ¿desea salir?")
                        if(mensaje):
                            ventIncluirT,destroy()
                            return menu()
                boton=tkinter.Button(ventIncluirT,text="continuar",bg="gray",fg="black",command=continuarT)
                boton.place(x=110,y=50)

            def EliminarTransporte():
                barraTransporte.destroy()
                ventanaDETransporte.geometry("400x400")
                ventanaDETransporte.title("Eliminar Transporte")
                etiqueta=tkinter.Label(ventanaDETransporte,text="Ingrese la placa del transporte a eliminar",font="bold")
                etiqueta.place(x=10,y=10)
                entry=tkinter.Entry(ventanaDETransporte)
                entry.place(x=80,y=40)
                def eliminarTransporte_aux():
                    #boton.destroy()
                    archivo=open("Gestion de transporte.txt")
                    transportes=archivo.readlines()
                    placa=entry.get()
                    if((placa+"\n")in transportes):
                        linea = transportes.index(placa+"\n")
                        eliminar=Eliminar_transporte_aux(transportes,linea,0)
                        archivo.close()
                        archivo=open("Gestion de transporte.txt","w")
                        archivo.write(eliminar)
                        archivo.close()
                        ventanaDETransporte.destroy()
                        return eliminado(transportes,linea,0)
                    else:
                        mensaje=messagebox.showinfo("Error","La placa ingresada no exixte.")
                    #boton2=tkinter.Button(ventanaDETransporte,text="Eliminar")
                                                
                boton=tkinter.Button(ventanaDETransporte,text="Eliminar",command=eliminarTransporte_aux)
                boton.place(x=120,y=60)
            def ModificarTransporte():
                barraTransporte.destroy()
                ventanaDETransporte.title("Modificar Transporte")
                etiqueta=tkinter.Label(ventanaDETransporte,text="Ingrese la placa del transporte a modificar")
                etiqueta.place(x=10,y=10)
                entry=tkinter.Entry(ventanaDETransporte)
                entry.place(x=70,y=30)
                def modificarTransporte_aux():
                    placa=entry.get()
                    archivo=open("Gestion de transporte.txt")
                    transporte=archivo.readlines()
                    if((placa+"\n")in transporte):
                        linea = transporte.index(placa + "\n")
                        #Mostrar_transporte(transporte, linea, 0)
                        transporte_Modificado = Modificar_transporte_Aux(transporte, linea+1, 0)#Se creo una variable para ingresar los nuevos datos.
                        #Gestion = open("Gestion de transporte.txt", "w")#Se abre el archivo en el modo que deseamos.
                        """
                        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        #Gestion.write(Convertir_A_String(transporte_Modificado))#Se escribe la modificación de la empresa en el archivo.
                        #Gestion.close()#Importante cerrar el archivo.
                        """
                        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                        nombre de Gestion para que fuera de mejor entendimiento.
                        """
                        ventanaDETransporte.destroy()
                        #return menu
                             
                    
                    
                boton=tkinter.Button(ventanaDETransporte,text="Modificar",command=modificarTransporte_aux)
                boton.place(x=100,y=50)    
            
            def MostrarTransporte():
                archivo="Gestion de transporte.txt"
                agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
                """
                En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                contador =1
                datos=""
                for linea in agenda:
                    datos+="linea"+str(contador)+":"+linea#Imprimir todos los contactos existentes en la agenda.
                    contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
                agenda.close()#Importante cerrar el archivo.
                """
                En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                barraTransporte.destroy()
                ventanaDETransporte.title("Mostrar Transporte")
                ventanaDETransporte.geometry("300x800")

                etiqueta=tkinter.Label(ventanaDETransporte,text=f"{datos}",font="italic")
                etiqueta.pack()
                def continuarAuX():
                    ventanaDETransporte.destroy()
                    return menu()
                boton=tkinter.Button(ventanaDETransporte,text="Continuar",font="italic",command=continuarAuX)
                boton.pack()
            ventanaDETransporte=Tk()
            ventanaDETransporte.geometry("300x200+100+100")
            ventanaDETransporte.title("Transporte")
            barraTransporte=Menu(ventanaDETransporte)
            menuTransporte=Menu(barraTransporte)
            menuTransporte.add_command(label="incluir transporte",command=IncluirTransporte)
            menuTransporte.add_command(label="eliminar transporte",command=EliminarTransporte)
            menuTransporte.add_command(label="modificar transporte",command=ModificarTransporte)
            menuTransporte.add_command(label="mostrar transporte",command=MostrarTransporte)
            
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
        ventAbrir.geometry("300x200+100+100")
        ventAbrir.title("Mantenimiento")
        ventAbrir.configure(background="blue")
        etiqueta=tkinter.Label(ventAbrir,text="Ingrese la contraseña.")
        etiqueta.place(x=80,y=10)
        barraMenu1=Menu(ventAbrir)
        mnuEdicion=Menu(barraMenu1,background="red")
        entry=tkinter.Entry(ventAbrir,show="*")
        entry.place(x=80,y=40)
        #entry.focus()
        ventAbrir.config(menu=barraMenu1)
        def clicker():
            respuesta=entry.get()
            archivo=open("clave.txt")
            lineas=archivo.readlines()
            if(respuesta in lineas):
                etiqueta.destroy()
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
        boton.place(x=110,y=70)
        
        ventAbrir.mainloop()

    

    def busquedas_avanzadas():
        
        ventana.destroy()
        
        def mensaje2():
            answer2=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
            if(answer2):
                ventana_Avanzada.destroy()
                return menu()
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

#----------------------------------------------------------------------------------------------------------------------

                 ##############FUCIONES AUXILIARES DE ELIMINAR EMPRESAS#########    

def Eliminar_Empresa1_aux(empresas,linea,cont):
    if (cont==5):
        return Convertir_A_String(empresas)
    else:
        #(empresas[linea].rstrip()
        empresas.pop(linea)
        return Eliminar_Empresa1_aux(empresas,linea,cont+1)
def Convertir_A_String(lista):
    if isinstance(lista, list):#El parámetro de entrada debe de ser una lista(restricción).
        string = ""
        for linea in lista:
            string += linea
        return string
    else:#Se imprime el error en el caso de que el parámetro de entrada no cumple con las restriciones predeterminadas.
        #print("Error: No se puede convertir a string, debido a que el tipo de dato de entrada no es una lista.")
         None
#----------------------------------------------------------------------------------------------------------------------

                 ##############FUCIONES AUXILIARES DE MODIFICAR EMPRESAS########    


def Modificar_Empresa_Aux(agenda, linea, contador):
    ventModificar=Tk()
    ventModificar.geometry("400x200+100+100")
    ventModificar.title("Modificar Empresa")
    ventModificar.config(width=300, height=200)
    etiqueta=tkinter.Label(ventModificar,text="Ingrese el nuevo nombre de la empresa.")
    etiqueta.place(x=70,y=10)
    entry=tkinter.Entry(ventModificar)
    entry.place(x=80,y=30)
    if contador == 3:
        Gestion = open("gestion de empresa.txt", "w")
        Gestion.write(Convertir_A_String(agenda))#Archivo al cual le se le dió ese nombre.
        Gestion.close()
        ventModificar.destroy()
        return menu()
    else:#Se hacen las modificaciones del contacto respectivamente.
        if contador == 0:
            def modificarSegundoDato():
                Empresa_Modificado = entry.get()
                agenda[linea] =Empresa_Modificado + "\n"
                boton.destroy()
                ventModificar.destroy()
                return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarSegundoDato)
            boton.place(x=100,y=50)
        elif(contador==1):
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la nueva provincia de la empresa.")
            etiqueta.place(x=70,y=10)
            def modificarTercerDato():
                Empresa_Modificado=entry.get()
                agenda[linea]=Empresa_Modificado+"\n"
                boton.destroy()
                ventModificar.destroy()
                return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarTercerDato)
            boton.place(x=100,y=50)
        else:
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la nueva ubicacion exacta de la empresa.")
            etiqueta.place(x=70,y=10)
            def modificarCuartoDato():
                Empresa_Modificado=entry.get()
                agenda[linea]=Empresa_Modificado+"\n"
                boton.destroy()
                ventModificar.destroy()
                return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarCuartoDato)
            boton.place(x=100,y=50)
            

#--------------------------------------------------------------------------------------------------------------------------------
            ##############Eliminar transporte auxiliar###########
"""
nombre:Eliminar_transporte_aux
entrada: transporte=la informacion de los transporte en lista
linea= linea de la lista que se desea eliminar
cont=un numero cero que ira aumentado su valor por uno por cada recursion que se realice hasta que se cumpla la condición.
salida: la lineas o indice de la lista que fue eliminada de la lista.
restricciones: el cont(contador) debe tener el valor de 9 para terminar la recurción 
"""
def Eliminar_transporte_aux(transporte,linea,cont):
    eliminado=""
    while cont <=9:
        eliminado+=transporte[linea].rstrip()+"\n"
        transporte.pop(linea)
        transporte
        linea
        cont+=1
    return Convertir_A_String(transporte)




def eliminado(transporte,linea,cont):      
    result=""
    
    while cont <=9:
        result+=transporte[linea].rstrip()+"\n"
        transporte.pop(linea)
        transporte
        linea
        cont+=1
    ventanaEliminado=Tk()
    ventanaEliminado.title("transporte eliminado")
    ventanaEliminado.geometry("300x400")
    etiqueta=tkinter.Label(ventanaEliminado,text=f"Transportes eliminado.",font="italic")
    etiqueta.pack()
    etiqueta1=tkinter.Label(ventanaEliminado,text=f"{result}",font="italic")
    etiqueta1.pack()
    def continuarAUX():
        ventanaEliminado.destroy()
        return menu()

    boton=tkinter.Button(ventanaEliminado,text="Continuar",font="bold",command=continuarAUX)
    boton.pack()
#--------------------------------------------------------------------------------------------------------
            #############Modificar transporte auxiliar###########

def Modificar_transporte_Aux(transporte, linea , cont):
    ventModificar=Tk()
    ventModificar.geometry("400x200+100+100")
    ventModificar.title("Modificar Transporte")
    ventModificar.config(width=300, height=200)
    #etiqueta=tkinter.Label(ventModificar,text="Ingrese el nuevo nombre de la empresa.")
    #etiqueta.place(x=70,y=10)
    
    if cont == 8:
        Gestion = open("Gestion de transporte.txt", "w")#Se abre el archivo en el modo que deseamos.
        """
        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
        nombre de agenda para que fuera de mejor entendimiento.
        """
        Gestion.write(Convertir_A_String(transporte))#Se escribe la modificación de la empresa en el archivo.
        Gestion.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de Gestion para que fuera de mejor entendimiento.
        """
        ventModificar.destroy()
        return menu()
         #Archivo al cual le se le dió ese nombre.
    else:#Se hacen las modificaciones del contacto respectivamente.
        if cont == 0:
            etiqueta =tkinter.Label(ventModificar,text="Eliga el tipo de transporte. ",font="italic")
            etiqueta.pack()
            def Buseta_AUX():
                transporte[linea] ="Buseta"+ "\n"
            #    boton.destroy()
             #   boton2.destroy()
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            def Limosina_AUX():
               transporte[linea] ="Limosina"+ "\n"
              # boton.destroy()
               #boton2.destroy()
               ventModificar.destroy()
               return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Buseta",command=Buseta_AUX)
            boton.pack()
            boton2=tkinter.Button(ventModificar,text="Limosina",command=Limosina_AUX)
            boton2.pack()
        elif(cont==1):
            #etiqueta.destroy()
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la nueva marca del transporte.",font="bold")
            etiqueta1.pack()
            entry=tkinter.Entry(ventModificar)
            entry.pack()
            def marcaAUX():
                marca=entry.get()
                transporte[linea]=marca+"\n"
                etiqueta1.destroy()
                boton.destroy()
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",command= marcaAUX)
            boton.place(x=80,y=60)
        elif(cont==2):
            etiqueta=tkinter.Label(ventModificar,text="Ingrese el nuevo modelo del transporte: ")
            etiqueta.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            def modeloAUX():
                modelo=entry.get()
                transporte[linea]=modelo+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",command=modeloAUX)
            boton.place(x=80,y=60)
        elif(cont==3):
            #etiqueta.destroy()
            #boton.destroy()
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese el nuevo año del transporte: ")
            etiqueta1.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            def AñoAUX():
                año=entry.get()
                transporte[linea]=año+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar",command=AñoAUX)
            boton1.place(x=80,y=60)
        elif(cont==4):
            #etiqueta1.destroy()
            #boton1.destroy()
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la nueva empresa del transporte: ")
            etiqueta.place(x=10,y=10)
            def EmpresaAUX():
                empresa=entry.get()
                transporte[linea]=empresa+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",command=EmpresaAUX)
            boton.place(x=80,y=60)

        elif(cont==5):
            #etiqueta.destroy()
            #boton.destroy()
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la cantidad de asiento de clase Vip. ")
            etiqueta1.place(x=10,y=10)
            def VipAUX():
                VIP=entry.get()
                transporte[linea]=VIP+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar",command=VipAUX)
            boton1.place(x=80,y=60)
           
        elif(cont==6):
            #etiqueta1.destroy()
            #boton1.destroy()
            etiqueta=tkinter.Label(ventModificar,text=" Ingrese la cantidad de asiento de clase normal. ")
            etiqueta.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            def NORMAL_AUX():
                normal=entry.get()
                transporte[linea]=normal+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",command=NORMAL_AUX)
            boton.place(x=80,y=60)

        else:
            #etiqueta.destroy()
            #boton.destroy()
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la cantidad de asiento de clase económica. ")
            etiqueta1.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar)
            entry.place(x=80,y=30)
            def EconomicoAUX():
                economico=entry.get()
                transporte[linea]=economico+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar",command=EconomicoAUX)
            boton1.place(x=80,y=60)
           
              
    




menu()
