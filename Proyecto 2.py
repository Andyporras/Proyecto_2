import tkinter
from tkinter import *
from tkinter import messagebox

"""
nombre:menu
entrada:ninguna definida
salida: una ventana de tkinter
restrincciones: no hay una definida
"""
def menu():
       

    ventana= Tk()

    ventana.geometry("500x200+10+10")
    ventana.title("Menú")
    ventana.configure(background="blue")
    etiqueta=tkinter.Label(ventana,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.place(x=0,y=50)
        

  
    barraMenu=Menu(ventana)
    
    mnuArchivo=Menu(barraMenu,background="red")
    """
    nombre:mensaje
    entrada: ninguna definida
    salida: una ventana con dos botones
    restricciones: no hay una definida 
    """
    def mensaje():
            answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
            if(answer):
                    ventana.destroy()
    """
    nombre:Mantenimiento
    salida: una ventana con un menu
    restricciones: debe ingresar la contraseña correcta para mostrar el menu
    """
    def Mantenimiento():
        ventana.destroy()
        """
        nombre:mensaje1
        entrada: ninguna definida
        salida: una ventana con dos botones
        restricciones: no hay una definida 
        """
        def mensaje1():
            answer=messagebox.askyesno("Regresar", "¿Desea regresar al menu principal? ")
            if(answer):
                ventAbrir.destroy()
                return menu()
                
        """
        nombre:Gestion_de_empresa
        salida: una ventana con un menu
        """
        def Gestion_de_empresa():
            ventAbrir.destroy()
            """
            nombre:mensajeEmpresa
            entrada: ninguna definida
            salida: una ventana con dos botones
            restricciones: no hay una definida 
            """
            def mensajeEmpresa():
                answer=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
                if(answer):
                    vetana_de_gestion_de_empresa.destroy()
                    return menu()
            """
            nombre: incluirEmpresa
            entrada: cedula= numero de la cedula juridica
            nombre=nombre de la empresa
            Provincia=Provincia de la empresa
            ciudad:ciudad de la empresa
            salida: return del menu de Gestion_de_empresas 
            retricciones: la cedula debe tener 10 digito y debe ser caracteres los datos ingresado.
             
            """
            def incluirEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventIncluir=Tk()
                ventIncluir.geometry("400x200+100+100")
                ventIncluir.configure(background="aqua")
                ventIncluir.title("Incluir Empresa")
                ventIncluir.config(width=300, height=200)
                etiqueta=tkinter.Label(ventIncluir,text="Ingrese la cedula jurídica.", font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.place(x=80,y=10)
                entry=tkinter.Entry(ventIncluir, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=80,y=30)
                def continuar():
                    respuesta=entry.get()
                    archivo=open("gestion de empresa.txt")
                    verificar=archivo.readlines()
                    if(len(respuesta) == 10):
                        if((respuesta+"\n") in verificar)==False:
                            etiqueta.destroy()
                            archivo=open("gestion de empresa.txt","a")
                            archivo.write(respuesta+"\n")
                        
                            etiqueta1=tkinter.Label(ventIncluir,text="Ingrese el nombre de la empresa.",
                                                    font=("Times New Roman",14), bg="white", fg="Black")
                            etiqueta1.place(x=80,y=10)
                            entry.place(x=90,y=40)
                            
                            def continuar1():
                                respuesta=entry.get()
                                archivo.write(respuesta+"\n")
                                
                                etiqueta=tkinter.Label(ventIncluir,text="Ingrese la provincia de la empresa.",
                                                       font=("Times New Roman",14), bg="white", fg="Black")
                                etiqueta.place(x=80,y=10)
                            
                                def continuar2():
                                    respuesta=entry.get()
                                    archivo.write(respuesta+"\n")
                                    etiqueta=tkinter.Label(ventIncluir,text="Ingrese la direccion exacta de la empresa.",
                                                           font=("Times New Roman",14), bg="white", fg="Black")
                                    etiqueta.place(x=80,y=10)
                              
                                    def continuar3():
                                        respuesta=entry.get()
                                        archivo.write(respuesta+"\n")
                                        archivo.write("---------------------"+"\n")
                                        archivo.close()
                                        ventIncluir.destroy()
                                        answer=messagebox.showinfo("Agregado", "Empresa agregado.")
                                        return menu()
                                    boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar3)
                                    boton.place(x=110,y=70)
                                boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar2)
                                boton.place(x=110,y=70)
                            boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar1)
                            boton.place(x=110,y=70)
                        else:
                            answer=messagebox.showerror("Error", "La cedula juridica ya existe.")
                    else:
                        answer=messagebox.askyesno("Error", "La cedula juridica no tiene 10 digitos desea intentar de nuevo.")
                        if(answer):
                            None
                        else:
                            return menu()
                            
                            

                        
                boton=tkinter.Button(ventIncluir,text="continuar",bg="gray",fg="black",command=continuar)
                boton.place(x=110,y=70)
                
                ventIncluir.mainloop()
            """
            nombre:eliminarEmpresa
            entrada:la cedula del transporte
            salida: borrar la empresa seleccionada
            retrincciones:debe ingresar una placa existente o guardada en el archivo .txt
            """
            def eliminarEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventEliminar=Tk()
                ventEliminar.geometry("400x200+100+100")
                ventEliminar.title("Eliminar Empresa")
                ventEliminar.configure(background="purple")
                ventEliminar.config(width=300, height=300)
                
                etiqueta=tkinter.Label(ventEliminar,text="Ingrese la cedula juridica de la empresa a eliminar.",
                                       font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.place(x=10,y=10)
                entry=tkinter.Entry(ventEliminar,text="",font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=80,y=50)
                def Eliminar_empresa_aux():
                    archivo=open("gestion de empresa.txt")
                    comprobar=archivo.readlines()
                    eliminar=entry.get()
                    if(eliminar+"\n" in comprobar):
                        archivo1=open("Gestion de Transporte.txt")
                        comprobar2=archivo1.readlines()
                        linea=comprobar.index(eliminar+"\n")
                        if(comprobar[linea+1])in comprobar2 :
                             answer=messagebox.showinfo("Salir", "¿Desea Salir?, Confirme...")
                             
                            
                        else:
                            
                            etiqueta.destroy()
                            entry.destroy()
                            boton.destroy()
                            ventEliminar.geometry("300x300")
                            lista=Listbox(ventEliminar,font=("Times New Roman",14), bg="white", fg="Black")
                            lista.pack()
                            cont=1
                            lista.insert(0,f"empresa eliminado")
                            for linea in comprobar[linea:linea+5]:
                                lista.insert(cont,f"linea {cont}: {linea}")
                                cont+=1
                            linea=comprobar.index(eliminar+"\n")
                            eliminar=Eliminar_Empresa1_aux(comprobar,linea,0)
                            archivo.close()
                            archivo=open("gestion de empresa.txt","w")
                            archivo.write(eliminar)
                            archivo.close()
                            
                            def Eliminar1_empresa_aux():
                                ventEliminar.destroy()
                                return menu()
                            boton1=tkinter.Button(ventEliminar,text="continuar",bg="gray",fg="black",command=Eliminar1_empresa_aux)
                            boton1.pack()
                            
                        
                boton=tkinter.Button(ventEliminar,text="continuar",bg="gray",fg="black",command=Eliminar_empresa_aux)
                boton.place(x=150,y=80)

                ventEliminar.mainloop()
            """
            nombre:modificarEmpresa
            entrada: la cedula de la empresa
            salida: un mensaje de que la empresa a sido modificada con exito
            restricciones:la cedula debe existir en el archivo de empresas
            """    
            def modificarEmpresa():
                vetana_de_gestion_de_empresa.destroy()
                ventModificar=Tk()
                ventModificar.geometry("410x200+100+100")
                ventModificar.title("Modificar Empresa")
                ventModificar.configure(background="violet")
                ventModificar.config(width=300, height=200)
                etiqueta=tkinter.Label(ventModificar,text="Ingrese la cedula juridica de la empresa a modificar.",
                                       font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.place(x=5,y=10)
                entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=90,y=50)
                def modificarEmpresa1():
                    result=entry.get()
                    archivo=open("gestion de empresa.txt")
                    empresas=archivo.readlines()
                    if(result+"\n") in empresas:
                        linea=empresas.index(result + "\n")
                        
                        ventModificar.destroy()
                        Modificar_Empresa_Aux(empresas, linea + 1, 0)#Se creo una variable para ingresar los nuevos datos.
                        """
                        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        archivo.close()
                        """
                        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                       
                    else:
                        messagebox.showerror("Error", "La cedula juridica ingresado no existe")
                boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarEmpresa1)
                boton.place(x=150,y=80)

    
                               
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
                ventMostrar=Tk()
                ventMostrar.geometry("300x400")
                ventMostrar.title("Mostrar Empresa.")
                ventMostrar.configure(background="purple")
                lista=Listbox(ventMostrar, font=("Times New Roman",14), bg="white", fg="Black")
                lista.pack()
                contador =1
                datos=""
                for linea in agenda:
                    lista.insert(contador,f"linea {contador} :  {linea}")#Imprimir todos los contactos existentes en la agenda.
                    contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
                agenda.close()#Importante cerrar el archivo.
                
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
            vetana_de_gestion_de_empresa.geometry("500x200+100+100")
            vetana_de_gestion_de_empresa.title("Gestion de empresa")
            vetana_de_gestion_de_empresa.configure(background="green")
            vetana_de_gestion_de_empresa.config(width=300, height=200)
            etiqueta=tkinter.Label(vetana_de_gestion_de_empresa,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=0,y=50)
            barraEmpresa=Menu(vetana_de_gestion_de_empresa)
            menuEmpresa=Menu(barraEmpresa,background="olive")
            
            menuEmpresa.add_command(label="incluir empresa", font=("Times New Roman",14), command=incluirEmpresa)
            menuEmpresa.add_command(label="eliminar empresa", font=("Times New Roman",14),  command=eliminarEmpresa)
            menuEmpresa.add_command(label="modificar empresa",font=("Times New Roman",14),  command=modificarEmpresa)
            menuEmpresa.add_command(label="mostrar empresas", font=("Times New Roman",14), command=mostrar_empresas)
            
            menuEmpresa.add_separator()
            menuEmpresa.add_command(label="Salir de gestion de empresa", font=("Times New Roman",14),command=mensajeEmpresa)
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
                ventIncluirT.configure(background="fuchsia")
                ventIncluirT.config(width=300, height=200)
                etiqueta=tkinter.Label(ventIncluirT,text="ingrese la placa del transporte.", font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.place(x=80,y=10)
                entry=tkinter.Entry(ventIncluirT,text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=90,y=40)
                def continuarT():
                    respuesta=entry.get()
                    archivo=open("Gestion de Transporte.txt","a")
                    archivo=open("Gestion de Transporte.txt")
                    verificar=archivo.readlines()
                    if((respuesta+"\n")in verificar)==False:
                        etiqueta.destroy()
                        archivo=open("Gestion de transporte.txt","a")
                        archivo.write(respuesta+"\n")
                        etiqueta2=tkinter.Label(ventIncluirT,text="selecione una de las opciones.",
                                                font="italic",bg="white", fg="Black")
                        etiqueta2.place(x=80,y=10)
                        entry.destroy()
                        boton.destroy()
                        def buseta():
                            etiqueta2.destroy()
                            boton1.destroy()
                            boton2.destroy()
                            
                            entry=tkinter.Entry(ventIncluirT, text="", font=("Times New Roman",14), bg="white", fg="Black")
                            entry.place(x=90,y=50)
                            archivo.write("buseta"+"\n")
                            etiqueta1=tkinter.Label(ventIncluirT,text="ingrese la marca de la buseta.",font="bold")
                            etiqueta1.place(x=80,y=10)
                            def incluirT():
                                boton.destroy()
                                etiqueta1.destroy()
                                marca=entry.get()
                                
                                archivo.write(marca+"\n")
                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese el modelo de la buseta.",font=("Times New Roman",14), bg="white", fg="Black")
                                etiqueta.place(x=80,y=10)
                                def modeloAux():
                                    etiqueta.destroy()
                                    boton1.destroy()
                                    
                                    
                                    modelo=entry.get()
                                    archivo.write(modelo+"\n")
                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese el año.",font=("Times New Roman",14), bg="white", fg="Black")
                                    etiqueta1.place(x=80,y=10)
                                    def añoAUX():
                                        boton2.destroy()
                                        etiqueta1.destroy()
                                        año=entry.get()
                                        mostrar=open("gestion de empresa.txt")
                                        lista=mostrar.readlines()
                                        datos=Listbox(ventIncluirT,font=("Times New Roman",14),
                                                      bg="white", fg="Black")
                                        datos.pack()
                                        ventIncluirT.geometry("600x500")
                                        cont=0
                                        for linea in lista:
                                            datos.insert(cont,f"{cont} linea : {linea}")
                                            cont+=1
                                        archivo.write(año+"\n")
                                        etiqueta=tkinter.Label(ventIncluirT,text="Ingresela la cedula juridica de una de las empresas disponible",font="bold")
                                        etiqueta.pack()                                       
                                        entry.pack()
                                        def empresaAUX():
                                            etiqueta.destroy()
                                            
                                            boton.destroy()
                                            datos.destroy()
                                            empresa=entry.get()
                                            archivo.write(empresa+"\n")
                                            etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento VIP",
                                                                    font=("Times New Roman",14), bg="white", fg="Black")
                                            etiqueta1.place(x=80,y=10)
                                            entry.place(x=100,y=50)
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
                                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase economico. ", font=("Times New Roman",14), bg="white", fg="Black")
                                                    etiqueta1.place(x=70,y=10)
                                                    
                                                    def economicoAUX():
                                                        economico=entry.get()
                                                        archivo.write(economico+"\n")
                                                        archivo.write("------------------------"+"\n")
                                                        archivo.close()
                                                        ventIncluirT.destroy()
                                                        return menu()
                                                    boton1=tkinter.Button(ventIncluirT,text="continuar",
                                                                          font=("Times New Roman",14),command=economicoAUX)
                                                    boton1.place(x=150,y=100)
                                                boton=tkinter.Button(ventIncluirT,text="continuar", font=("Times New Roman",14),command=normalAUX)
                                                boton.place(x=150,y=100)
                                            boton1=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=VipAux)
                                            boton1.place(x=160,y=100)
                                        boton=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=empresaAUX)
                                        boton.pack()
                                    boton2=tkinter.Button(ventIncluirT,text="agregar", font=("Times New Roman",14), command=añoAUX)
                                    boton2.place(x=150,y=100)
                                boton1=tkinter.Button(ventIncluirT,text="continuar",font=("Times New Roman",14),command=modeloAux)
                                boton1.place(x=150,y=100)
                                
                            boton=tkinter.Button(ventIncluirT,text="continuar", font=("Times New Roman",14), bg="white", fg="Black",command=incluirT)
                            boton.place(x=150,y=100)

                        def limosina():
                            etiqueta2.destroy()
                            boton1.destroy()
                            boton2.destroy()
                            
                            entry=tkinter.Entry(ventIncluirT, text="", font=("Times New Roman",14), bg="white", fg="Black")
                            entry.place(x=90,y=50)
                            archivo.write("limosina"+"\n")
                            etiqueta1=tkinter.Label(ventIncluirT,text="ingrese la marca de la limosina.",font="bold")
                            etiqueta1.place(x=80,y=10)
                            def incluirT2():
                                boton.destroy()
                                etiqueta1.destroy()
                                marca=entry.get()
                                
                                archivo.write(marca+"\n")
                                etiqueta=tkinter.Label(ventIncluirT,text="Ingrese el modelo de la limosina.",font=("Times New Roman",14), bg="white", fg="Black")
                                etiqueta.place(x=80,y=10)
                                def modeloAux2():
                                    etiqueta.destroy()
                                    boton1.destroy()
                                    
                                    
                                    modelo=entry.get()
                                    archivo.write(modelo+"\n")
                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese el año.", font=("Times New Roman",14))
                                    etiqueta1.place(x=80,y=10)
                                    def añoAUX2():
                                        boton2.destroy()
                                        etiqueta1.destroy()
                                        año=entry.get()
                                        archivo.write(año+"\n")
                                        mostrar=open("gestion de empresa.txt")
                                        lista=mostrar.readlines()
                                        datos=Listbox(ventIncluirT, text="", font=("Times New Roman",14), bg="white", fg="Black")
                                        datos.pack()
                                        cont=0
                                        for linea in lista:
                                            datos.insert(cont,f"{cont} linea : {linea}")
                                            cont+=1
                                        
                                        etiqueta=tkinter.Label(ventIncluirT,text="Ingrese la cedula juridica de una de las empresas disponible",font="bold")
                                        etiqueta.pack()
                                        entry.pack()
                                        def empresaAUX2():
                                            etiqueta.destroy()
                                            datos.destroy()
                                            boton.destroy()
                                        
                                            empresa=entry.get()
                                            archivo.write(empresa+"\n")
                                            etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento VIP", font=("Times New Roman",14))
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
                                                    etiqueta1=tkinter.Label(ventIncluirT,text="Ingrese la cantidad de asiento clase economico. " , font=("Times New Roman",14))
                                                    etiqueta1.place(x=70,y=10)
                                                    
                                                    def economicoAUX2():
                                                        
                                                        economico=entry.get()
                                                        archivo.write(economico+"\n")
                                                        archivo,write("------------------------"+"\n")
                                                        archivo.close()
                                                        ventIncluirT.destroy()
                                                        return menu()
                                                    boton1=tkinter.Button(ventIncluirT,text="continuar", font=("Times New Roman",14),command=economicoAUX2)
                                                    boton1.place(x=120,y=80)
                                                boton=tkinter.Button(ventIncluirT,text="continuar", font=("Times New Roman",14),command=normalAUX2)
                                                boton.place(x=120,y=80)
                                            boton1=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=VipAux2)
                                            boton1.place(x=140,y=100)
                                        boton=tkinter.Button(ventIncluirT,text="continuar",font="italic",command=empresaAUX2)
                                        boton.pack()
                                    boton2=tkinter.Button(ventIncluirT,text="agregar", font=("Times New Roman",14), command=añoAUX2)
                                    boton2.place(x=120,y=70)
                                boton1=tkinter.Button(ventIncluirT,text="continuar",font=("Times New Roman",14),command=modeloAux2)
                                boton1.place(x=120,y=70)
                                
                            boton=tkinter.Button(ventIncluirT,text="continuar",font=("Times New Roman",14),command=incluirT2)
                            boton.place(x=130,y=80)

                            
                            
                            
                        boton1=tkinter.Button(ventIncluirT,text="Buseta", font=("Times New Roman",14), command=buseta)
                        boton1.place(x=70,y=50)
                        boton2=tkinter.Button(ventIncluirT,text="limosina",font=("Times New Roman",14), command=limosina)
                        boton2.place(x=150,y=50)
                        
                    else:
                        mensaje=messagebox.showerror("Error","Error, Digite una placa que no este repetido.")
                        
                boton=tkinter.Button(ventIncluirT,text="continuar",bg="gray",fg="black",command=continuarT)
                boton.place(x=150,y=70)

            def EliminarTransporte():
                barraTransporte.destroy()
                etiqueta.destroy()
                ventanaDETransporte.geometry("400x400")
                ventanaDETransporte.title("Eliminar Transporte")
                ventanaDETransporte.configure(background="lime")
                etiqueta2=tkinter.Label(ventanaDETransporte,text="Ingrese la placa del transporte a eliminar",font="bold")
                etiqueta2.place(x=10,y=10)
                entry=tkinter.Entry(ventanaDETransporte,text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=80,y=40)
                def eliminarTransporte_aux():
                
                    archivo=open("Gestion de transporte.txt")
                    transportes=archivo.readlines()
                    placa=entry.get()
                    if((placa+"\n")in transportes):
                        archivo2=open("Gestion de viaje.txt")
                        viajes=archivo2.readlines()
                        if(seEncuentra_Aux(placa,viajes)==False):
                            ventanaDETransporte.destroy()
                            linea = transportes.index(placa+"\n")
                            eliminar=Eliminar_transporte_aux(transportes,linea,0)
                            archivo.close()
                        else:
                            mensaje=messagebox.showinfo("Error","El transporte esta asociado a un viaje.")
                    else:
                        mensaje=messagebox.showinfo("Error","La placa ingresada no exixte.")
                    
                                                
                boton=tkinter.Button(ventanaDETransporte,text="Eliminar", font=("Times New Roman",14), command=eliminarTransporte_aux)
                boton.place(x=130,y=70)
            def ModificarTransporte():
                barraTransporte.destroy()
                etiqueta.destroy()
                ventanaDETransporte.title("Modificar Transporte")
                ventanaDETransporte.configure(background="olive")
                etiqueta2=tkinter.Label(ventanaDETransporte,text="Ingrese la placa del transporte a modificar", font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta2.place(x=10,y=10)
                entry=tkinter.Entry(ventanaDETransporte)
                entry.place(x=70,y=50)
                def modificarTransporte_aux():
                    placa=entry.get()
                    archivo=open("Gestion de transporte.txt")
                    transporte=archivo.readlines()
                    if((placa+"\n")in transporte):
                        linea = transporte.index(placa + "\n")
                        Modificar_transporte_Aux(transporte, linea+1, 0)#Se creo una variable para ingresar los nuevos datos.
                        """
                        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        archivo.close()
                        """
                        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                        nombre de Gestion para que fuera de mejor entendimiento.
                        """
                        ventanaDETransporte.destroy()
                    else:
                        messagebox.showinfo("Error","La placa ingresada no exixte.")
                        
                             
                    
                    
                boton=tkinter.Button(ventanaDETransporte,text="Modificar",font=("Times New Roman",14),command=modificarTransporte_aux)
                boton.place(x=100,y=80)    
            
            def MostrarTransporte():
                archivo="Gestion de transporte.txt"
                agenda= open (archivo)#Se abre el archivo en el modo que deseamos.
                """
                En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                etiqueta.destroy()
                barraTransporte.destroy()
                lista=agenda.readlines()
                ventanaDETransporte.title("Mostrar Transporte")
                ventanaDETransporte.geometry("300x500")
                ventanaDETransporte.configure(background="pink")
                datos=Listbox(ventanaDETransporte,font=("Times New Roman",14), bg="white", fg="Black")
                datos.pack()
                
                contador =0
                
                for linea in lista:
                    datos.insert(contador,f"linea {contador} : {linea}")#Imprimir todos los contactos existentes en la agenda.
                    contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
                agenda.close()#Importante cerrar el archivo.
                """
                En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                
                def continuarAuX():
                    ventanaDETransporte.destroy()
                    return menu()
                boton=tkinter.Button(ventanaDETransporte,text="Continuar",font="italic",command=continuarAuX)
                boton.pack()
            ventanaDETransporte=Tk()
            ventanaDETransporte.geometry("500x200+100+100")
            ventanaDETransporte.title("Transporte")
            ventanaDETransporte.configure(background="fuchsia")
            etiqueta=tkinter.Label(ventanaDETransporte,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=0,y=50)
            barraTransporte=Menu(ventanaDETransporte)
            menuTransporte=Menu(barraTransporte,background="green")
            menuTransporte.add_command(label="incluir transporte", font=("Times New Roman",14),command=IncluirTransporte)
            menuTransporte.add_command(label="eliminar transporte",font=("Times New Roman",14),command=EliminarTransporte)
            menuTransporte.add_command(label="modificar transporte",font=("Times New Roman",14),command=ModificarTransporte)
            menuTransporte.add_command(label="mostrar transporte", font=("Times New Roman",14),command=MostrarTransporte)
            
            menuTransporte.add_separator()
            menuTransporte.add_command(label="Salir de gestion de empresa", font=("Times New Roman",14),command=mensajeTransporte)
            barraTransporte.add_cascade(label="Transporte",menu=menuTransporte)
            ventanaDETransporte.config(menu=barraTransporte)

            ventanaDETransporte.mainloop()
        def gestion_De_viaje():
            ventAbrir.destroy()
            def mensajeViaje():
                aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                if(aceptar):
                        ventanaViaje.destroy()
            def IncluirViajes():
                ventanaViaje.destroy()
                ventIncluirV=Tk()
                ventIncluirV.geometry("400x200+100+100")
                ventIncluirV.title("Incluir Viajes.txt")
                ventIncluirV.configure(background="aqua")
                ventIncluirV.config(width=300, height=200)
                etiqueta=tkinter.Label(ventIncluirV,text="Ingrese la provincia de salidad.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                etiqueta.place(x=80,y=10)
                entry=tkinter.Entry(ventIncluirV, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=80,y=50)
                def agregarprovincia():
                    provincia=entry.get()
                    etiqueta.destroy()
                    boton.destroy()
                    numeroDeViaje=numeroDeViaje_aux()
                    archivo=open("Gestion de viaje.txt","a")
                    archivo.write(numeroDeViaje+"\n")
                    archivo.write(provincia+"\n")
                    etiqueta1=tkinter.Label(ventIncluirV,text="Ingrese la ciudad de salidad.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                    etiqueta1.place(x=80,y=10)
                    def agregarciudad():
                        etiqueta1.destroy()
                        boton1.destroy()
                        ciudad=entry.get()
                        archivo.write(ciudad+"\n")
                        etiqueta=tkinter.Label(ventIncluirV,text="Ingrese la fecha de salidad.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                        etiqueta.place(x=80,y=10)
                        def agregarFechaSA():
                            etiqueta.destroy()
                            boton.destroy()
                            fecha=entry.get()
                            archivo.write(fecha+"\n")
                            etiqueta1=tkinter.Label(ventIncluirV,text="Ingrese la hora de salidad.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                            etiqueta1.place(x=80,y=10)
                            def agregarhora():
                                etiqueta1.destroy()
                                boton1.destroy()
                                hora=entry.get()
                                archivo.write(hora+"\n")
                                etiqueta=tkinter.Label(ventIncluirV,text="Ingrese la provincia de llegada.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                etiqueta.place(x=80,y=10)
                                def agregarProvinciaLLE():
                                    etiqueta.destroy()
                                    boton.destroy()
                                    provincia=entry.get()
                                    archivo.write(provincia+"\n")
                                    etiqueta1=tkinter.Label(ventIncluirV,text="Ingrese la ciudad de llegada.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                    etiqueta1.place(x=80,y=10)
                                    def agregarciudadLLE():
                                        etiqueta1.destroy()
                                        boton1.destroy()
                                        ciudad=entry.get()
                                        archivo.write(ciudad+"\n")
                                        etiqueta=tkinter.Label(ventIncluirV,text="Ingrese la fecha de llegada.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                        etiqueta.place(x=80,y=10)
                                        def agregarFechaLLE():
                                            etiqueta.destroy()
                                            boton.destroy()
                                            fecha=entry.get()
                                            archivo.write(fecha+"\n")
                                            etiqueta1=tkinter.Label(ventIncluirV,text="Ingrese la hora de llegada.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                            etiqueta1.place(x=80,y=10)
                                            def agregarHoraLLE():
                                                
                                                etiqueta1.destroy()
                                                boton1.destroy()
                                                hora=entry.get()
                                                entry.destroy()
                                                archivo.write(hora+"\n")
                                                archivo2=open("gestion de Transporte.txt")
                                                datos=archivo2.readlines()
                                                cont=0
                                                lista=Listbox(ventIncluirV, font=("Times New Roman",14), bg="white", fg="Black")
                                                lista.pack()
                                                for linea in datos:
                                                    lista.insert(cont,f"linea {cont} : {linea}")
                                                    cont+=1
                                                etiqueta2=tkinter.Label(ventIncluirV,text="Ingrese la cedula juridica de la empresa.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                                etiqueta2.pack()
                                                entry1=tkinter.Entry(ventIncluirV,text="", font=("Times New Roman",14), bg="white", fg="Black")
                                                entry1.pack()
                                                def AgregraEmpresa1():
                                        
                                                    archivo1=open("Gestion de Transporte.txt")
                                                    transporte=archivo1.readlines()
                                                    empresa=entry1.get()
                                                    if(empresa+"\n" )in transporte:
                                                        archivo.write(empresa+"\n")
                                                        etiqueta2.destroy()
                                                        boton.destroy()
                
                                                        etiqueta3=tkinter.Label(ventIncluirV,text="Ingrese la placa del transporte.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                                        etiqueta3.pack()
                                                        def agregartransporte1():
                                                            datos=entry1.get()
                                                            if(datos+"\n") in transporte:
                                                                archivo.write(datos+"\n")
                                                                etiqueta3.destroy()
                                                                boton1.destroy()
                                                                lista.destroy()
                                                                etiqueta=tkinter.Label(ventIncluirV,text="Ingrese el valor del voleto VIP.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                                                etiqueta.pack()
                                                                def agregarVIP():
                                                                    datos=entry1.get()
                                                                    archivo.write(datos+"\n")
                                                                    etiqueta.destroy()
                                                                    boton.destroy()
                                                                    etiqueta1=tkinter.Label(ventIncluirV,text="Ingrese el valor del voleto Normal .",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                                                    etiqueta1.pack()
                                                                    def agregarNormal():
                                                                        datos=entry1.get()
                                                                        archivo.write(datos+"\n")
                                                                        etiqueta1.destroy()
                                                                        boton1.destroy()
                                                                        etiqueta=tkinter.Label(ventIncluirV,text="Ingrese el valor del voleto Economico.",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black")
                                                                        etiqueta.pack()
                                                                        def agregarEconomico():
                                                                            datos=entry1.get()
                                                                            archivo.write(datos+"\n")
                                                                            archivo.write("------------------------"+"\n")
                                                                            archivo.close()
                                                                            ventIncluirV.destroy()
                                                                            return menu()
                                                                        boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarEconomico)
                                                                        boton.pack()
                                                                    boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarNormal)
                                                                    boton1.pack()
                                                                boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarVIP)
                                                                boton.pack()
                                                        boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregartransporte1)
                                                        boton1.pack()
                                                    else:
                                                        mensaje=messagebox.showinfo("Error","nombre de la empresa no existe.") 
                                                boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=AgregraEmpresa1)
                                                boton.pack()
                                            boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarHoraLLE)
                                            boton1.place(x=100,y=80) 
                                        boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarFechaLLE)
                                        boton.place(x=100,y=80) 
                                    
                                    boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarciudadLLE)
                                    boton1.place(x=100,y=80) 
                                    
                                boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarProvinciaLLE)
                                boton.place(x=100,y=80) 
                            boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarhora)
                            boton1.place(x=100,y=80) 
                        boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarFechaSA)
                        boton.place(x=100,y=80) 
                        
                    boton1=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarciudad)
                    boton1.place(x=100,y=80)             
                boton=tkinter.Button(ventIncluirV,text="Continuar",font=("Times New Roman", 18),bg="RoyalBlue2" , fg="Black",command=agregarprovincia)
                boton.place(x=100,y=80)
            def EliminarViajes():
                barraViaje.destroy()
                etiqueta.destroy()
                ventanaViaje.geometry("400x400")
                ventanaViaje.title("Eliminar Viaje")
                ventanaViaje.configure(background="cyan")
                etiqueta2=tkinter.Label(ventanaViaje,text="Ingrese el numero de viaje a eliminar",font="bold")
                etiqueta2.place(x=10,y=10)
                entry=tkinter.Entry(ventanaViaje, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=80,y=40)
                def eliminarViajes_aux():
                    
                    archivo=open("Gestion de viaje.txt")
                    Viajes=archivo.readlines()
                    numero=entry.get()
                    if((numero+"\n")in Viajes):
                        linea = Viajes.index(numero+"\n")
                        eliminar=Eliminar_Viaje_aux(Viajes,linea,0)
                        archivo.close()
                        archivo=open("Gestion de Viaje.txt","w")
                        archivo.write(eliminar)
                        archivo.close()
                        ventanaViaje.destroy()
                    else:
                        mensaje=messagebox.showinfo("Error","El numero de viaje ingresado no exixte.")
              
                                                
                boton=tkinter.Button(ventanaViaje,text="Eliminar",command=eliminarViajes_aux)
                boton.place(x=120,y=70)

            def ModificarViajes():
                barraViaje.destroy()
                etiqueta.destroy()
                ventanaViaje.title("Modificar Viaje")
                ventanaViaje.configure(background="aqua")
                etiqueta2=tkinter.Label(ventanaViaje,text="Ingrese el numero del viaje a modificar", font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta2.place(x=10,y=10)
                entry=tkinter.Entry(ventanaViaje, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.place(x=70,y=40)
                def ModificarViajes_aux():
                    numero=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    Viajes=archivo.readlines()
                    if((numero+"\n")in Viajes):
                        linea = Viajes.index(numero + "\n")
                        Modificar_Viajes_Aux(Viajes, linea+1, 0)#Se creo una variable para ingresar los nuevos datos.
                        """
                        En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                        que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                        nombre de agenda para que fuera de mejor entendimiento.
                        """
                        archivo.close()
                        """
                        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                        nombre de Gestion para que fuera de mejor entendimiento.
                        """
                        ventanaViaje.destroy()
                    else:
                        messagebox.showinfo("Error","El numero de viaje ingresado no exixte.")

                        
                        
                             
                    
                    
                boton=tkinter.Button(ventanaViaje,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=ModificarViajes_aux)
                boton.place(x=100,y=80)    
                

            def mostrar_viajes():
                archivo="Gestion de viaje.txt"
                agenda= open (archivo)#Se abre el archivo en el modo que deseamos.
                """
                En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
                que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                barraViaje.destroy()
                etiqueta.destroy()
                ventanaViaje.title("Mostrar Viajes")
                ventanaViaje.configure(background="aqua")
                ventanaViaje.geometry("300x500")
                datos=Listbox(ventanaViaje , font=("Times New Roman",14), bg="white", fg="Black")
                datos.pack()
                
                contador =0
                
                for linea in agenda:
                    datos.insert(contador,f"linea {contador} : {linea}")#Imprimir todos los contactos existentes en la agenda.
                    contador+=1 #Agregamos un contador para que el usuario pueda ver en que linea corresponde a cada dato. 
                agenda.close()#Importante cerrar el archivo.
                """
                En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
                nombre de agenda para que fuera de mejor entendimiento.
                """
                

                def continuarAuX1():
                    ventanaViaje.destroy()
                    return menu()
                boton=tkinter.Button(ventanaViaje,text="Continuar",font="italic",command=continuarAuX1)
                boton.pack()
                
            ventanaViaje=Tk()
            ventanaViaje.geometry("500x400+100+100")
            ventanaViaje.title("viaje")
            ventanaViaje.configure(background="aqua")
            barraViaje=Menu(ventanaViaje)
            menuViaje=Menu(barraViaje,background="coral")
            etiqueta=tkinter.Label(ventanaViaje,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=0,y=50)
            menuViaje.add_command(label="incluir Viaje",
                                  font=("Times New Roman",14),command=IncluirViajes)
            menuViaje.add_command(label="eliminar Viaje", font=("Times New Roman",14),command=EliminarViajes)
            menuViaje.add_command(label="modificar Viaje",font=("Times New Roman",14),command=ModificarViajes)
            menuViaje.add_command(label="mostrar Viaje",font=("Times New Roman",14),command=mostrar_viajes)
            
            menuViaje.add_separator()
            menuViaje.add_command(label="Salir de gestion de Viaje",font=("Times New Roman",14),command=mensajeViaje)
            barraViaje.add_cascade(label="Viaje", font=("Times New Roman",14),menu=menuViaje)
            ventanaViaje.config(menu=barraViaje)
            ventanaViaje.mainloop()

            
                

        ventAbrir=Tk()
        ventAbrir.geometry("300x200+100+100")
        ventAbrir.title("Mantenimiento")
        ventAbrir.configure(background="blue")
        etiqueta=tkinter.Label(ventAbrir,text="Ingrese la contraseña.",font=("Times New Roman",14))
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
                ventAbrir.geometry("500x200+100+100")
                etiqueta1=tkinter.Label(ventAbrir,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta1.place(x=0,y=50)
                """
                nombre: Consultar_historial_de_reservaciones
                entrada: op=una de las opciones disponible.
                salida: imprime un menu y despues retorna la opcion seleccionada por el usuario.
                restricciones: debe seleccionar una de las opciones disponible. 
                """

                def historial_De_reservaciones():
                    def mensaje_Historial():
                        aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                        if(aceptar):
                            ventana_Historial.destroy()
                    ventana_Historial=Tk()
                    ventana_Historial.geometry("500x200+100+100")
                    ventana_Historial.title("historial de reservaciones")
                    ventana_Historial.configure(background="aqua")
                    etiqueta1=tkinter.Label(ventana_Historial,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
                    etiqueta1.place(x=0,y=50)
                    def rango_de_fecha_de_salida():
                        etiqueta1.destroy()
                        barra_Historial.destroy()
                        ventana_Historial.geometry("400x300")
                        ventana_Historial.configure(background="aqua")
                        archivo=open("Reservacion.txt")
                        lineas=archivo.readlines()
                        etiqueta=tkinter.Label(ventana_Historial,text="Ingrese el rango de fecha de salida a buscar",
                                               font=("Times New Roman",14), bg="white", fg="Black")
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Historial, text="", font=("Times New Roman",14), bg="white", fg="Black")
                        entry.pack()
                        def continuar5():
                            #rango=input("Ingrese el rango de fecha de salida a buscar: ")
                            buscar=entry.get()
                            filtrar_por_informacion(lineas,buscar,9,False,9)
                            archivo.close()
                        boton=tkinter.Button(ventana_Historial, text="Continuar", font=("Times New Roman",14), bg="white", fg="Black",command=continuar5)
                        boton.pack()

                    def rango_de_fecha_de_llegada():
                        etiqueta1.destroy()
                        barra_Historial.destroy()
                        ventana_Historial.geometry("400x300")
                        ventana_Historial.configure(background="aqua")
                        archivo=open("Reservacion.txt")
                        lineas=archivo.readlines()
                        etiqueta=tkinter.Label(ventana_Historial,text="Digite el rango de la fecha de llegada a filtar:",
                                               font=("Times New Roman",14), bg="white", fg="Black")
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Historial, text="", font=("Times New Roman",14), bg="white", fg="Black")
                        entry.pack()
                        def continuar6():
                            #rango=input("Ingrese el rango de fecha de salida a buscar: ")
                            buscar=entry.get()
                            filtrar_por_informacion(lineas,buscar,13,False,13)
                            archivo.close()
                        boton=tkinter.Button(ventana_Historial, text="Continuar", font=("Times New Roman",14),
                                            bg="white", fg="Black",command=continuar6)
                        boton.pack()
                        

                    def rango_de_fecha_de_la_reservacion():
                        etiqueta1.destroy()
                        barra_Historial.destroy()
                        ventana_Historial.geometry("400x300")
                        ventana_Historial.configure(background="aqua")
                        archivo=open("Reservacion.txt")
                        lineas=archivo.readlines()
                        etiqueta=tkinter.Label(ventana_Historial,text="Digite el rango de la fecha de reservacion a buscar:",
                                               font=("Times New Roman",14), bg="white", fg="Black")
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Historial, text="", font=("Times New Roman",14), bg="white", fg="Black")
                        entry.pack()
                        def continuar7():
                            #rango=input("Ingrese el rango de fecha de salida a buscar: ")
                            buscar=entry.get()
                            filtrar_por_informacion(lineas,buscar,3,False,3)
                            archivo.close()
                        boton=tkinter.Button(ventana_Historial, text="Continuar", font=("Times New Roman",14),
                                             bg="white", fg="Black",command=continuar7)
                        boton.pack()

                    def Buscar_lugar_de_salida():
                        etiqueta1.destroy()
                        barra_Historial.destroy()
                        ventana_Historial.geometry("400x300")
                        ventana_Historial.configure(background="aqua")
                        archivo=open("Reservacion.txt")
                        lineas=archivo.readlines()
                        etiqueta=tkinter.Label(ventana_Historial,text="digite el lugar de salida a buscar: ",
                                               font=("Times New Roman",14), bg="white", fg="Black")
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Historial, text="", font=("Times New Roman",14), bg="white", fg="Black")
                        entry.pack()
                        def continuar8():
                            #rango=input("Ingrese el rango de fecha de salida a buscar: ")
                            buscar=entry.get()
                            filtrar_por_informacion1(lineas,buscar,7,False,7)
                            archivo.close()
                        boton=tkinter.Button(ventana_Historial, text="Continuar", font=("Times New Roman",14),
                                             bg="white", fg="Black",command=continuar8)
                        boton.pack()


                    def Buscar_lugar_de_llegada():
                        etiqueta1.destroy()
                        barra_Historial.destroy()
                        ventana_Historial.geometry("400x300")
                        ventana_Historial.configure(background="aqua")
                        archivo=open("Reservacion.txt")
                        lineas=archivo.readlines()
                        etiqueta=tkinter.Label(ventana_Historial,text="digite el lugar de llegada a buscar: ",
                                               font=("Times New Roman",14), bg="white", fg="Black")
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Historial, text="", font=("Times New Roman",14), bg="white", fg="Black")
                        entry.pack()
                        def continuar9():
                            #rango=input("Ingrese el rango de fecha de salida a buscar: ")
                            buscar=entry.get()
                            filtrar_por_informacion1(lineas,buscar,11,False,11)
                            archivo.close()
                        boton=tkinter.Button(ventana_Historial, text="Continuar", font=("Times New Roman",14),
                                             bg="white", fg="Black",command=continuar9)
                        boton.pack()
                            

                            
                    barra_Historial=Menu(ventana_Historial)
                    menu_Historial=Menu(barra_Historial,background="lime")
                    menu_Historial.add_command(label="Rango de fecha de salida",font=("Times New Roman",14),command=rango_de_fecha_de_salida)
                    menu_Historial.add_command(label="Rango de fecha de llegada",font=("Times New Roman",14),command=rango_de_fecha_de_llegada)
                    menu_Historial.add_command(label="Rango de fecha de la reservación", font=("Times New Roman",14),command=rango_de_fecha_de_la_reservacion)
                    menu_Historial.add_command(label="Lugar de salida.", font=("Times New Roman",14),command=Buscar_lugar_de_salida)
                    menu_Historial.add_command(label="Lugar de llegada.", font=("Times New Roman",14),command=Buscar_lugar_de_llegada)

                    
                    menu_Historial.add_separator()
                    menu_Historial.add_command(label="Salir de historial de reservaciones", font=("Times New Roman",14),command=mensaje_Historial)
                    barra_Historial.add_cascade(label="historial de reservaciones",menu=menu_Historial)
                    ventana_Historial.config(menu=barra_Historial)
                    ventana_Historial.mainloop()
                def Estadistica_de_Viaje():
                        def mensaje_Estadisticas():
                            aceptar=messagebox.askyesno("salir","¡Desea salir?, Confirme")
                            if(aceptar):
                                ventana_Estadistica.destroy()
                        ventana_Estadistica=Tk()
                        ventana_Estadistica.geometry("400x400+100+100")
                        ventana_Estadistica.title("Estadistica_de_Viaje")
                        ventana_Estadistica.configure(background="aqua")
                        archivo=open("Gestion de viaje.txt")
                        viajes=archivo.readlines()
                        lista=tkinter.Listbox(ventana_Estadistica,
                                              font=("Times New Roman",15),bg="gray",fg="black")
                        lista.pack()
                        cont=0
                        for linea in viajes:
                            lista.insert(cont,f"linea {cont}: {linea}")
                            cont+=1
                        etiqueta=tkinter.Label(ventana_Estadistica,text="Escriba un numero de viaje disponible",
                                                     font=("Times New Roman",15),bg="gray",fg="black")

                        
                        etiqueta.pack()
                        entry=tkinter.Entry(ventana_Estadistica,text="",
                                                     font=("Times New Roman",15),bg="gray",fg="black")
                        entry.pack()
                        def mostrarEstadistica():
                            numero=entry.get()
                            datos=[]
                            if(numero+"\n") in viajes:
                                lista.destroy()
                                etiqueta.destroy()
                                entry.destroy()
                                boton.destroy()
                                linea=viajes.index(numero+"\n")
                                datos+=["Número de viaje:"+viajes[linea]]
                                datos+=["Empresa:"+viajes[linea+9]]
                                datos+=["Transporte:"+viajes[linea+10]]
                                datos+=["Provincia de salida:"+viajes[linea+1]]
                                datos+=["Ciudad de salida:"+viajes[linea+2]]
                                datos+=["Fecha de salida:"+viajes[linea+3]]
                                datos+=["Hora de salida:"+viajes[linea+4]]
                                datos+=["Provincia de llegada:"+viajes[linea+5]]
                                datos+=["Ciudad de llegada:"+viajes[linea+6]]
                                datos+=["Fecha de llegada:"+viajes[linea+7]]
                                datos+=["Hora de llegada:"+viajes[linea+8]]
                                archivo2=open("Reservacion.txt")
                                reservaciones=archivo2.readlines()
                                if(viajes[linea])in reservaciones:
                                        archivo3=open("Gestion de Transporte.txt")
                                        Transporte=archivo3.readlines()
                                        linea3=Transporte.index(viajes[linea+10])
                                        linea2=reservaciones.index(viajes[linea])
                                        datos+=["Asiento VIP reservado:"+reservaciones[linea2+15]]
                                        disponibleVip=Transporte[linea3+6][:-1]
                                        datos+=["Asiento VIP disponible:"+str(int(disponibleVip)-int(reservaciones[linea2+15]))]
                                        datos+=["Asiento Normal reservado:"+reservaciones[linea2+16]]
                                        disponibleNormal=Transporte[linea3+7][:-1]
                                        datos+=["Asiento Normal disponible:"+str(int(disponibleNormal)-int(reservaciones[linea2+16]))]
                                        datos+=["Asiento Economico reservado:"+reservaciones[linea2+17]]
                                        disponibleEconomico=Transporte[linea3+8][:-1]
                                        datos+=["Asiento Economico  disponible:"+str(int(disponibleEconomico)-int(reservaciones[linea2+17]))]
                                        datos+=["monto recaudado por el viaje:"+reservaciones[linea2+18]]                                            
                                        cont=0
                                        lista1=tkinter.Listbox(ventana_Estadistica,
                                                             font=("Times New Roman",15),bg="gray",fg="black")
                                        lista1.pack()
                                        etiqueta1=tkinter.Label(ventana_Estadistica,text="Esta son las estadisticas del viaje seleccionado",font=("Times New Roman",15),bg="gray",fg="black")
                                        etiqueta1.pack()
                                        for linea in datos:
                                            lista1.insert(cont,f"{linea}")
                                            cont+=1
                                        def continuar7():
                                            ventana_Estadistica.destroy()
                                            return menu()
                                else:
                                    archivo3=open("Gestion de Transporte.txt")
                                    Transporte=archivo3.readlines()
                                    linea3=Transporte.index(viajes[linea+10])
                                    datos+=["Asiento VIP reservado:"+"0"]
                                    disponibleVip=Transporte[linea3+6][:-1]
                                    datos+=["Asiento VIP disponible:"+str(int(disponibleVip))]
                                    datos+=["Asiento Normal reservado:"+"0"]
                                    disponibleNormal=Transporte[linea3+7][:-1]
                                    datos+=["Asiento Normal disponible:"+str(int(disponibleNormal))]
                                    datos+=["Asiento Economico reservado:"+"0"]
                                    disponibleEconomico=Transporte[linea3+8][:-1]
                                    datos+=["Asiento Economico  disponible:"+str(int(disponibleEconomico))]
                                    datos+=["monto recaudado por el viaje:"+"0"]                                            
                                    cont=0
                                    lista1=tkinter.Listbox(ventana_Estadistica,
                                                           font=("Times New Roman",15),bg="gray",fg="black")
                                    lista1.pack()
                                    etiqueta1=tkinter.Label(ventana_Estadistica,text="Esta son las estadisticas del viaje seleccionado",font=("Times New Roman",15),bg="gray",fg="black")
                                    etiqueta1.pack()
                                    for linea in datos:
                                        lista1.insert(cont,f"{linea}")
                                        cont+=1
                                    def continuar7():
                                        ventana_Estadistica.destroy()
                                        return menu()
                            
                                
                                               
                                boton1=tkinter.Button(ventana_Estadistica,text="continuar",
                                                     font=("Times New Roman",15),bg="gray",fg="black",command=continuar7)
                                boton1.pack()      
                            else:
                                messagebox.showerror("Error","El numero de viaje no existe")
                                
                            
                        boton=tkinter.Button(ventana_Estadistica,text="Continuar",
                                                     font=("Times New Roman",15),bg="gray",fg="black",command=mostrarEstadistica)
                        boton.pack()

                        ventana_Estadistica.mainloop()
                
                mnuEdicion.add_command(label="Gestión de empresas",font=("Times New Roman",14),command=Gestion_de_empresa)
                mnuEdicion.add_command(label="Gestión de transporte por empresa",font=("Times New Roman",14),command=transporte)
                
                        
                mnuEdicion.add_command(label="Gestión de viaje", font=("Times New Roman",14),command=gestion_De_viaje)
                mnuEdicion.add_command(label="Consultar historial de reservaciones",font=("Times New Roman",14),command=historial_De_reservaciones)
                mnuEdicion.add_command(label=" Estadísticas de viaje" , font=("Times New Roman",14),command=Estadistica_de_Viaje)
                
                mnuEdicion.add_separator()
                mnuEdicion.add_command(label="Salir de mantenimiento",font=("Times New Roman",14),command=mensaje1)
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
            etiqueta1.destroy()
            ventana_consulta=Tk()
            ventana_consulta.geometry("400x200+100+100")
            ventana_consulta.title("consulta_Viajes")
            ventana_consulta.configure(background="aqua")
            barra_Consulta=Menu(ventana_consulta)
            menu_Consulta=Menu(barra_Consulta,background="lime")
            """
            nombre:buscar_empresa
            entrada: caracteres
            salida: se retorna una funcion que buscara el dato ingresado por el usuario.
            restricciones: no hay una definida.
            """
            def buscar_empresa():
                ventana_Avanzada.destroy()
                menu_Consulta.destroy()
                etiqueta=tkinter.Label(ventana_consulta,text="Ingrese la cedula juridica a buscar: ", font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.pack()
                entry=tkinter.Entry(ventana_consulta, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.pack()
                archivo=open("Gestion de viaje.txt")
                lista=archivo.readlines()
                def Buscar1():
                    empresa=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    lista=archivo.readlines()
                    if(empresa+"\n")in lista:
                        boton.destroy()
                        etiqueta.destroy()
                        ventana_consulta.destroy()
                        return buscar_por_filtro(lista,empresa,9,False,9)
                    else:
                        messagebox.showerror("Error", "La cedula juridica que ingreso no existe")
                        
                archivo.close()
                boton=tkinter.Button(ventana_consulta,text="Buscar",font=("Times New Roman",14), bg="white", fg="Black",command=Buscar1)
                boton.pack()
                ventana_consulta.mainloop()

            def Buscar_LSalida():
                ventana_Avanzada.destroy()
                menu_Consulta.destroy()
                etiqueta=tkinter.Label(ventana_consulta,text="Ingrese el lugar de salida a buscar: ",font=("Times New Roman",14))
                etiqueta.pack()
                entry=tkinter.Entry(ventana_consulta, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.pack()
                archivo=open("Gestion de viaje.txt")
                lista=archivo.readlines()
                def Buscar2():
                    empresa=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    lista=archivo.readlines()
                    if(empresa+"\n")in lista:
                        boton.destroy()
                        etiqueta.destroy()
                        ventana_consulta.destroy()
                    
                        return buscar_por_filtro(lista,empresa,1,False,1)
                    else:
                        messagebox.showerror("Error", "no hay ningun viaje del lugar ingresado")

                archivo.close()
                boton=tkinter.Button(ventana_consulta,text="Buscar",font=("Times New Roman",14), bg="white", fg="Black",command=Buscar2)
                boton.pack()
                ventana_consulta.mainloop()
            def Buscar_LuLLegada():
                ventana_Avanzada.destroy()
                menu_Consulta.destroy()
                etiqueta=tkinter.Label(ventana_consulta,text="Ingrese el lugar de llegada a buscar: ",font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.pack()
                entry=tkinter.Entry(ventana_consulta, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.pack()
                archivo=open("Gestion de viaje.txt")
                lista=archivo.readlines()
                def Buscar3():
                    empresa=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    lista=archivo.readlines()
                    if(empresa+"\n")in lista:
                        boton.destroy()
                        etiqueta.destroy()
                        ventana_consulta.destroy()
                        return buscar_por_filtro(lista,empresa,5,False,5)
                    else:
                        messagebox.showerror("Error", "no hay ningun viaje del lugar ingresado")

                archivo.close()
                boton=tkinter.Button(ventana_consulta,text="Buscar",font=("Times New Roman",14), bg="white", fg="Black",command=Buscar3)
                boton.pack()
                ventana_consulta.mainloop()
                
            def rango_Fecha_Salida():
                ventana_Avanzada.destroy()
                menu_Consulta.destroy()
                etiqueta=tkinter.Label(ventana_consulta,text="Ingrese la fecha de salida a buscar ",font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.pack()
                entry=tkinter.Entry(ventana_consulta, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.pack()
                archivo=open("Gestion de viaje.txt")
                lista=archivo.readlines()
                def Buscar4():
                    empresa=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    lista=archivo.readlines()
                    if(empresa+"\n")in lista:
                        boton.destroy()
                        etiqueta.destroy()
                        ventana_consulta.destroy()
                        return buscar_por_filtro(lista,empresa,3,False,3)
                    else:
                        messagebox.askyesno("Error", "no hay ningu viaje con la fecha ingresado")

                archivo.close()
                boton=tkinter.Button(ventana_consulta,text="Buscar",font=("Times New Roman",14), bg="white", fg="Black",command=Buscar4)
                boton.pack()
                ventana_consulta.mainloop()
            def rango_Fecha_LLEgada():
                ventana_Avanzada.destroy()
                menu_Consulta.destroy()
                etiqueta=tkinter.Label(ventana_consulta,text="Ingrese la fecha de llegada a buscar: ",font=("Times New Roman",14), bg="white", fg="Black")
                etiqueta.pack()
                entry=tkinter.Entry(ventana_consulta, text="", font=("Times New Roman",14), bg="white", fg="Black")
                entry.pack()
                archivo=open("Gestion de viaje.txt")
                lista=archivo.readlines()
                def Buscar5():
                    empresa=entry.get()
                    archivo=open("Gestion de viaje.txt")
                    lista=archivo.readlines()
                    if(empresa+"\n")in lista:
                        boton.destroy()
                        etiqueta.destroy()
                        ventana_consulta.destroy()
                        return buscar_por_filtro(lista,empresa,7,False,7)
                    else:
                        messagebox.askyesno("Error", "no hay ningu viaje con la fecha ingresado")

                archivo.close()
                boton=tkinter.Button(ventana_consulta,text="Buscar",font=("Times New Roman",14), bg="white", fg="Black",command=Buscar5)
                boton.pack()
                ventana_consulta.mainloop()

            menu_Consulta.add_command(label="Empresa", font=("Times New Roman",14),command=buscar_empresa)
            menu_Consulta.add_command(label="Lugar de salida", font=("Times New Roman",14),comman=Buscar_LSalida)
            menu_Consulta.add_command(label="Lugar de llegada", font=("Times New Roman",14),command=Buscar_LuLLegada)
            menu_Consulta.add_command(label="Rango de fecha de salida.",font=("Times New Roman",14),command=rango_Fecha_Salida)
            menu_Consulta.add_command(label="Rango de fecha de llegada.", font=("Times New Roman",14),command=rango_Fecha_LLEgada)
                    
                    
            menu_Consulta.add_separator()
            menu_Consulta.add_command(label="Salir de consulta de viajes",font=("Times New Roman",14),command=mensaje_consulta_Viajes)
            barra_Consulta.add_cascade(label="consulta_Viajes",menu=menu_Consulta)
            ventana_consulta.config(menu=barra_Consulta)
            ventana_consulta.mainloop()
        
        def reservacion_de_viajes():
            ventana_reservacion = Tk()
            ventana_reservacion.geometry("600x500")
            ventana_reservacion.title("Reservación de Viaje")
            ventana_reservacion.configure(background="aqua")

            

            Archivo = open("Gestion de viaje.txt")
            datos = Archivo.readlines()
            lista = tkinter.Listbox(ventana_reservacion,width=40)
            lista.place(x=40,y=170)
            
            cont = 0
            for linea in datos:
                lista.insert(cont,f"linea {cont}: {linea}")
                cont += 1
            
            etiquetaNumero = tkinter.Label(ventana_reservacion,text="Digite el numero del viaje:",
                                            font=("Times new roman","12"),bg="white", fg="Black").place(x=10,y=20)
            Numero = tkinter.Entry(ventana_reservacion,text = "",font=("Times new roman","12"),bg="white", fg="Black")
            Numero.place(x=300,y=20)

            etiquetaNombre = tkinter.Label(ventana_reservacion,text="Escriba su nombre:",
                                            font=("Times new roman","12"),bg="white", fg="Black").place(x=10,y=50)
            Nombre = tkinter.Entry(ventana_reservacion,text= "",font=("Times new roman","12"),bg="white", fg="Black")
            Nombre.place(x=300,y=50)

            etiquetaCantidadVIP = tkinter.Label(ventana_reservacion,text="Cantidad de espacios a reservar VIP:",
                                        font=("Times new roman","12"),bg="white", fg="Black").place(x=10,y=80)
            CantidadVIP = tkinter.Entry(ventana_reservacion,text="",font=("Times new roman","12"),bg="white", fg="Black")
            CantidadVIP.place(x=300,y=80)

            etiquetaCantidadNor = tkinter.Label(ventana_reservacion,text="Cantidad de espacios a reservar economicos:",
                                            font=("Times new roman","12"),bg="white", fg="Black").place(x=10,y=110)
            CantidadNor = tkinter.Entry(ventana_reservacion,text = "",font=("Times new roman","12"),bg="white", fg="Black")
            CantidadNor.place(x=300,y=110)

            etiquetaCantidadEco = tkinter.Label(ventana_reservacion,text="Cantidad de espacios a reservar economicos:",
                                        font=("Times new roman","12"),bg="white", fg="Black").place(x=10,y=140)
            CantidadEco = tkinter.Entry(ventana_reservacion,text = "",font=("Times new roman","12"),bg="white", fg="Black")
            CantidadEco.place(x=300,y=140)

            def reservacion_de_viajes1():
                
            
                reservacion_de_viajes_aux(Numero.get(),Nombre.get(),CantidadVIP.get(),CantidadNor.get(),CantidadEco.get())
                ventana_reservacion.destroy()
            boton = tkinter.Button(ventana_reservacion, text = "Reservar",font=("Times new roman","12"),bg="white", fg="Black",
                            command= reservacion_de_viajes1).place(x=270,y=380)
            

        
        def cancelacion_aux():
            barraMenu2.destroy()
            etiqueta1.destroy()
            ventana_Avanzada.geometry("400x400")
            ventana_Avanzada.title("Cancelar reservacion")
            ventana_Avanzada.configure(background="aqua")
            etiqueta=tkinter.Label(ventana_Avanzada,text="Ingrese el numero de reservacion",font="bold")
            etiqueta.place(x=10,y=10)
            entry=tkinter.Entry(ventana_Avanzada, font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=80,y=40)
            def cancelarReservacion_aux():
                
                archivo=open("Reservacion.txt")
                reservaciones=archivo.readlines()
                numero=entry.get()
                if((numero+"\n")in reservaciones):
                    linea = reservaciones.index(numero+"\n")
                    eliminar=cancelar_Reservacion_aux(reservaciones,linea,0)
                    archivo.close()
                    archivo=open("Reservacion.txt","w")
                    archivo.write(eliminar)
                    archivo.close()
                    ventana_Avanzada.destroy()
                else:
                    mensaje=messagebox.showinfo("Error","El numero de reservacion ingresado no exixte.")
              
                                                
            boton=tkinter.Button(ventana_Avanzada,text="Cancelar reservacion",font=("Times New Roman",14), bg="white", fg="Black",
                                 command=cancelarReservacion_aux)
            boton.place(x=100,y=70)

            

                    
        ventana_Avanzada=Tk()
        ventana_Avanzada.geometry("500x200+100+100")
        ventana_Avanzada.title("Busquedas Avanzadas")
        ventana_Avanzada.configure(background="aqua")
        barraMenu2=Menu(ventana_Avanzada)
        menu_avanzado=Menu(barraMenu2,background="lime")
        etiqueta1=tkinter.Label(ventana_Avanzada,text="Seleccione la opcion que necesita en la parte superior izquierda.",font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=0,y=50)
        

        menu_avanzado.add_command(label="Consulta de viajes",font=("Times New Roman",14),command=consulta_Viajes)
        menu_avanzado.add_command(label=" Reservación de viaje", font=("Times New Roman",14),command=reservacion_de_viajes)
        menu_avanzado.add_command(label=" Cancelación de reservación", font=("Times New Roman",14),command=cancelacion_aux)

        menu_avanzado.add_separator()
        menu_avanzado.add_command(label="Salir de Busqueda Avanzadas",font=("Times New Roman",14),command=mensaje2)
        barraMenu2.add_cascade(label="Busquedas Avanzadas",menu=menu_avanzado)
        ventana_Avanzada.config(menu=barraMenu2)

        
        
        

        ventana_Avanzada.mainloop()




    mnuArchivo.add_command(label="Opciones administrativas",font=("Times New Roman",14),command=Mantenimiento)
    mnuArchivo.add_command(label="Opciones de usuario normal",font=("Times New Roman",14),command=busquedas_avanzadas)
    mnuArchivo.add_separator()
    mnuArchivo.add_command(label="Salir",font=("Times New Roman",14), command=mensaje)
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
        print(empresas)
        empresas.pop(int(linea))
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


def Modificar_Empresa_Aux(agenda,linea, contador):
    ventModificar=Tk()
    ventModificar.geometry("400x200+100+100")
    ventModificar.title("Modificar Empresa")
    ventModificar.config(width=300, height=200)
    ventModificar.configure(background="aqua")
    etiqueta=tkinter.Label(ventModificar,text="Ingrese el nuevo nombre de la empresa.",font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.place(x=70,y=10)
    entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
    entry.place(x=100,y=50)
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
                return Modificar_Empresa_Aux(agenda,linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarSegundoDato)
            boton.place(x=140,y=80)
        elif(contador==1):
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la nueva provincia de la empresa.",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=30,y=10)
            def modificarTercerDato():
                Empresa_Modificado=entry.get()
                agenda[linea]=Empresa_Modificado+"\n"
                boton.destroy()
                ventModificar.destroy()
                return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarTercerDato)
            boton.place(x=140,y=80)
        else:
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la nueva ubicacion exacta de la empresa.",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=30,y=10)
            def modificarCuartoDato():
                Empresa_Modificado=entry.get()
                agenda[linea]=Empresa_Modificado+"\n"
                boton.destroy()
                ventModificar.destroy()
                return Modificar_Empresa_Aux(agenda, linea+1, contador+1)
            boton=tkinter.Button(ventModificar,text="Modificar",bg="gray",fg="black",command=modificarCuartoDato)
            boton.place(x=140,y=80)
            

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
"""
def Eliminar_transporte_aux(transporte,linea,cont):
    eliminado=""
    eliminado+=transporte[linea]+"\n"
    while cont <=9:
        transporte.pop(linea)
        transporte
        linea
        cont+=1
    return Convertir_A_String(transporte)
"""



def Eliminar_transporte_aux(transporte,linea,cont):      
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
    ventanaEliminado.configure(background="aqua")
    etiqueta=tkinter.Label(ventanaEliminado,text=f"Transportes eliminado.",font="italic")
    etiqueta.pack()
    etiqueta1=tkinter.Label(ventanaEliminado,text=f"{result}",font="italic")
    etiqueta1.pack()
    def continuarAUX():
        ventanaEliminado.destroy()
        archivo=open("Gestion de transporte.txt","w")
        eliminar=Convertir_A_String(transporte)
        archivo.write(eliminar)
        archivo.close()
        return menu()
        

    boton=tkinter.Button(ventanaEliminado,text="Continuar",font="bold",command=continuarAUX)
    boton.pack()
#--------------------------------------------------------------------------------------------------------
            #############Modificar transporte auxiliar###########

def Modificar_transporte_Aux(transporte, linea , cont):
    ventModificar=Tk()
    ventModificar.geometry("400x200+100+100")
    ventModificar.title("Modificar Transporte")
    ventModificar.configure(background="aqua")
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
         
    else:
        if cont == 0:
            etiqueta =tkinter.Label(ventModificar,text="Eliga el tipo de transporte. ",font="italic")
            etiqueta.pack()
            def Buseta_AUX():
                transporte[linea] ="Buseta"+ "\n"
            
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            def Limosina_AUX():
               transporte[linea] ="Limosina"+ "\n"
              
               ventModificar.destroy()
               return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Buseta", font=("Times New Roman",14), bg="white", fg="Black",command=Buseta_AUX)
            boton.pack()
            boton2=tkinter.Button(ventModificar,text="Limosina",font=("Times New Roman",14), bg="white", fg="Black",command=Limosina_AUX)
            boton2.pack()
        elif(cont==1):
        
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la nueva marca del transporte.",font="bold")
            etiqueta1.pack()
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.pack()
            def marcaAUX():
                marca=entry.get()
                transporte[linea]=marca+"\n"
                etiqueta1.destroy()
                boton.destroy()
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command= marcaAUX)
            boton.place(x=80,y=60)
        elif(cont==2):
            etiqueta=tkinter.Label(ventModificar,text="Ingrese el nuevo modelo del transporte: ",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=70,y=50)
            def modeloAUX():
                modelo=entry.get()
                transporte[linea]=modelo+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command=modeloAUX)
            boton.place(x=80,y=80)
        elif(cont==3):
            #etiqueta.destroy()
            #boton.destroy()
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese el nuevo año del transporte: ", font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta1.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=70,y=50)
            def AñoAUX():
                año=entry.get()
                transporte[linea]=año+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=AñoAUX)
            boton1.place(x=80,y=80)
        elif(cont==4):
            lista=tkinter.Listbox(ventModificar,font=("Times New Roman",14), bg="white", fg="Black")
            lista.pack()
            etiqueta=tkinter.Label(ventModificar,text="Ingrese la cedula de la empresa del transporte: ",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.pack()
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.pack()
            cont=0
            archivo=open("gestion de empresa.txt")
            almacenar=archivo.readlines()
            for datos in almacenar:
                lista.insert(cont,f"Linea {cont}: {datos}")
                cont+=1
            def EmpresaAUX():
                empresa=entry.get()
                transporte[linea]=empresa+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command=EmpresaAUX)
            boton.pack()
        elif(cont==5):
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=80,y=50)
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la cantidad de asiento de clase Vip. ",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta1.place(x=10,y=10)
            def VipAUX():
                VIP=entry.get()
                transporte[linea]=VIP+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command=VipAUX)
            boton1.place(x=100,y=80)
           
        elif(cont==6):
            etiqueta=tkinter.Label(ventModificar,text=" Ingrese la cantidad de asiento de clase normal. ", font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=80,y=50)
            def NORMAL_AUX():
                normal=entry.get()
                transporte[linea]=normal+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=NORMAL_AUX)
            boton.place(x=80,y=80)

        else:
            etiqueta1=tkinter.Label(ventModificar,text="Ingrese la cantidad de asiento de clase económica. ",font=("Times New Roman",14), bg="white", fg="Black")
            etiqueta1.place(x=10,y=10)
            entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
            entry.place(x=80,y=50)
            def EconomicoAUX():
                economico=entry.get()
                transporte[linea]=economico+"\n"
                ventModificar.destroy()
                return Modificar_transporte_Aux(transporte, linea+1, cont+1)
            boton1=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command=EconomicoAUX)
            boton1.place(x=100,y=80)
           
              
def numeroDeViaje_aux():
    archivo="Gestion de viaje.txt"
    crear=open (archivo,'a')
    agenda= open (archivo,'r')#Se abre el archivo en el modo que deseamos.
    """
    En la función *f. = open (nombreArchivo,'r')* donde f. corresponde a file que es un dato o información
    que se guarda en el dispositivo de almacenamiento de la computadora. A nuestra variable file le dimos el
    nombre de agenda para que fuera de mejor entendimiento.
    """
    contador=0
    for linea in agenda:
        contador+=1
    agenda.close()
    return str(contador//12+1)
#-----------------------------------------------------------------------------------------------------------------------------

                     #################AUXILIAR DE ELIMINAER VIAJE###################



def Eliminar_Viaje_aux(Viajes,linea,cont):
    eliminado=""
    while cont <=14:
        eliminado+=Viajes[linea].rstrip()+"\n"
        Viajes.pop(linea)
        Viajes
        linea
        cont+=1
    mostrarViaje_Eliminado(eliminado)
    return Convertir_A_String(Viajes)
 
def mostrarViaje_Eliminado(viaje):      
    ventanaEliminado=Tk()
    ventanaEliminado.title("transporte eliminado")
    ventanaEliminado.geometry("300x450")
    ventanaEliminado.configure(background="aqua")
    etiqueta=tkinter.Label(ventanaEliminado,text=f"Viaje eliminado.",font="italic")
    etiqueta.pack()
    etiqueta1=tkinter.Label(ventanaEliminado,text=f"{viaje}",font="italic")
    etiqueta1.pack()
    def continuarAUX():
        ventanaEliminado.destroy()
        return menu()

    boton=tkinter.Button(ventanaEliminado,text="Continuar",font="bold",command=continuarAUX)
    boton.pack()
#-------------------------------------------------------------------------------------------------------


                #########################AUXILIAR DE MODIFICAR VIAJE##########################


def Modificar_Viajes_Aux(viajes, linea , cont):
    ventModificar=Tk()
    ventModificar.geometry("400x200+100+100")
    ventModificar.title("Modificar Viaje")
    ventModificar.configure(background="aqua")
    ventModificar.config(width=300, height=200)
    if(cont==13): 
        Gestion = open("Gestion de viaje.txt", "w")#Se abre el archivo en el modo que deseamos.
        Gestion.write(Convertir_A_String(viajes))#Se escribe la modificación de la empresa en el archivo.
        Gestion.close()#Importante cerrar el archivo.
        """
        En la función *f.close()* donde f. corresponde a file y a nuestra variable file le dimos el
        nombre de Gestion para que fuera de mejor entendimiento.
        """
        ventModificar.destroy()
        return menu()
            
        
    elif cont == 0:
        etiqueta =tkinter.Label(ventModificar,text="Ingresar la provincia de salida. ",font="italic")
        etiqueta.place(x=20,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=40,y=50)
        def ProvinciaModificar():
            provincia=entry.get()
            viajes[linea]=provincia+"\n"
            etiqueta.destroy()
            boton.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea+1 , cont+1)
        boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=ProvinciaModificar)
        boton.place(x=70,y=100)
        
    elif(cont==1):
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese la ciudad de salida.",font="bold")
        etiqueta1.place(x=10,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=40,y=50)
        def modificarCiudad():
            ciudad=entry.get()
            viajes[linea]=ciudad+"\n"
            etiqueta1.destroy()
            boton.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea+1, cont+1)
        boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarCiudad)
        boton.place(x=80,y=80)
    elif(cont==2):
        etiqueta=tkinter.Label(ventModificar,text="Ingrese la fecha de salida " , font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta.place(x=70,y=20)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=80,y=60)
        def modificarfecha():
            fecha=entry.get()
            viajes[linea]=fecha+"\n"
            etiqueta.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
        boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarfecha)
        boton.place(x=110,y=90)
    elif(cont==3):
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese la hora de salida.", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=65,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=70,y=60)
        def modificarhora():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            etiqueta1.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
        
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarhora)
        boton1.place(x=110,y=100)
    elif(cont==4):       
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=60,y=50)
        etiqueta=tkinter.Label(ventModificar,text="Ingrese la provincia de llegada. " , font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta.place(x=40,y=10)
        def modificarLLegadaP():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            etiqueta.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
        boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaP)
        boton.place(x=80,y=80)
        
    elif(cont==5):
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=50,y=50)
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese la ciudad de llegada. ",font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=30,y=10)
        def modificarLLegadaC():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
        
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaC)
        boton1.place(x=80,y=80)
        
    elif(cont==6):
        etiqueta=tkinter.Label(ventModificar,text=" Ingrese la fecha de llegada. ", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta.place(x=45,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=50,y=40)
        def modificarLLegadaF():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaF)
        boton.place(x=90,y=70)
        
    elif(cont==7):
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese la hora de llegada", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=50,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=55,y=40)
        def modificarLLegadaH():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaH)
        boton1.place(x=80,y=70)
        
    elif(cont==8):
        archivo=open("Gestion de Transporte.txt")
        datos=archivo.readlines()
        ventModificar.geometry("300x400")  
        lista=Listbox(ventModificar, font=("Times New Roman",14), bg="white", fg="Black")
        lista.pack()
        contador=0
        for indice in datos:
            lista.insert(cont,f"linea {contador}: {indice}")
            contador+=1
        etiqueta1=tkinter.Label(ventModificar,text=f"Ingrese la cedula juridica de la empresa.", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.pack()
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.pack()
        def modificarLLegadaE():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
          
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaE)
        boton1.pack()
    elif(cont==9):
        archivo=open("Gestion de Transporte.txt")
        datos=archivo.readlines()
        ventModificar.geometry("300x400")
        lista=Listbox(ventModificar, font=("Times New Roman",14), bg="white", fg="Black")
        lista.pack()
        contador=0
        for indices in datos:
            lista.insert(contador,f"linea {contador} : {indices}")
            contador+=1
        etiqueta1=tkinter.Label(ventModificar,text=f"Ingrese la placa del transporte." , font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.pack()
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.pack()
        def modificarLLegadaT():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton1=tkinter.Button(ventModificar,text="Modificar",font=("Times New Roman",14), bg="white", fg="Black",command=modificarLLegadaT)
        boton1.pack()
    elif(cont==10):
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese el valor del voleto VIP", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=30,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=70,y=40)
        def modificarVIP():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton1=tkinter.Button(ventModificar,text="Modificar" , font=("Times New Roman",14), bg="white", fg="Black",command=modificarVIP)
        boton1.place(x=80,y=70)

    elif(cont==11):
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese el valor del voleto Normal", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=30,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=80,y=40)
        def modificarNormal():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            etiqueta1.destroy()
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarNormal)
        boton1.place(x=100,y=70)
    else:
        etiqueta1=tkinter.Label(ventModificar,text="Ingrese el valor del voleto Economico", font=("Times New Roman",14), bg="white", fg="Black")
        etiqueta1.place(x=30,y=10)
        entry=tkinter.Entry(ventModificar, text="", font=("Times New Roman",14), bg="white", fg="Black")
        entry.place(x=70,y=40)
        def modificarEconomico():
            datosModificado=entry.get()
            viajes[linea]=datosModificado+"\n"
            ventModificar.destroy()
            return Modificar_Viajes_Aux(viajes, linea +1, cont+1)
            
        boton1=tkinter.Button(ventModificar,text="Modificar", font=("Times New Roman",14), bg="white", fg="Black",command=modificarEconomico)
        boton1.place(x=100,y=70)
        
        
                
        
        
#---------------------------------------------------------------------------------------------------

    
def buscar_por_filtro(lista,buscar,linea,Existe,linea2):
    ventana7=Tk()
    ventana7.geometry("600x400")
    ventana7.configure(background="aqua")
    mostrar=[]
    while linea< len(lista):
        if buscar in lista[linea]:
            linea3=linea-linea2
            cont=0
            while cont!=15:
                mostrar+=[lista[linea3]]
                linea3+=1
                
                cont+=1
            #Mostrar_viaje(lista,linea -linea2, 0)
            lista
            buscar
            linea += 15
            linea2
        else:
            lista
            buscar
            linea +=15
            linea2
    lista=Listbox(ventana7, font=("Times New Roman",14), bg="white", fg="Black")
    lista.pack()
    cont=0
    for datos in mostrar:
        lista.insert(cont,f"linea {cont} : {datos}")
        cont+=1
    etiqueta=tkinter.Label(ventana7,text=f"Estos son los viajes encontrados según el dato que ingreso. ", font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.pack()
    def salir5():
        aceptar=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(aceptar):
            ventana7.destroy()
            return menu()
    boton=tkinter.Button(ventana7,text="salir" , font=("Times New Roman",14), bg="white", fg="Black",command=salir5)
    boton.pack()
    
        
"""
nombre:Mostrar_informacion
entrada:datos = un conjunto de lista.
linea= un indice.
cont= un contador.
salida: se imprime las lista solicitadas.
restricciones: el contador debe ser igual a 16 para que termine la recursion.
"""
def Mostrar_viaje(datos,linea,cont):
    ventana=Tk()
    ventana.geometry("400x400")
    ventana.configure(background="aqua")
    lista=Listbox(ventana, font=("Times New Roman",14), bg="white", fg="Black")
    lista.pack()
    while cont !=15:
        lista.insert(cont,f"linea {cont} : {datos[linea]}")
        linea+=1
        cont+=1
    def Salir_Aux():
        aceptar=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(aceptar):
            boton.destroy()
            def principal():
                ventana.destroy()
                return menu()
            boton1=tkinter.Button(ventana,text="continuar", font=("Times New Roman",14), bg="white", fg="Black",command=principal)
            boton1.pack()
            
    boton=tkinter.Button(ventana,text="continuar", font=("Times New Roman",14), bg="white", fg="Black",command=Salir_Aux)
    boton.pack() 
                                                

#---------------------------------------------------------------------------------------------------------------------------------------------

    
def cancelar_Reservacion_aux(reservaciones,linea,cont):
    eliminado=[]
    while cont <=16:
        eliminado+=[reservaciones[linea]]
        reservaciones.pop(linea)
        reservaciones
        linea
        cont+=1
    mostrarReservacion_Cancelada(eliminado)
    return Convertir_A_String(reservaciones)
 
def mostrarReservacion_Cancelada(reservacion):      
    ventanaEliminado=Tk()
    ventanaEliminado.title("Reservacion cancelada")
    ventanaEliminado.geometry("300x400")
    ventanaEliminado.configure(background="aqua")
    etiqueta=tkinter.Label(ventanaEliminado,text=f"Reservacion cancelada.",font="italic")
    etiqueta.pack()
    lista=Listbox(ventanaEliminado,font=("Times New Roman",14), bg="white", fg="Black")
    lista.pack()
    cont=0
    for linea in reservacion:
        lista.insert(cont,f"linea {cont}:{linea}")
        cont+=1
    def continuarAUX():
        ventanaEliminado.destroy()
        return menu()

    boton=tkinter.Button(ventanaEliminado,text="Continuar",font="bold",command=continuarAUX)
    boton.pack()
#----------------------------------------------------------------------------------------------------------


                            ############ AUXILIARES DE BUSQUEDA DE RESERVACION###############

"""
nombre: filtar_por_informacion.
entrada: lista= varible que contiene los datos del archivo de reservacion
buscar= dato a buscar.
linea= indice de donde se podria ubicar el dato a buscar.
Existe= varible para comprobar si existe la informacion a buscar.
linea2=indice de donde debe iniciar la impresion del dato a buscar.
salida: muestra los datos que se encontro.
restriciones: la linea debe ser menor que la cantidad de listas que contenga la variable lista 
"""
def filtrar_por_informacion(lista,buscar,linea,Existe,linea2):
    ventanaReservacion=Tk()
    ventanaReservacion.geometry("600x400")
    ventanaReservacion.configure(background="aqua")
    mostrar=[]
    while linea < len(lista):
        if buscar in lista[linea]:
            cont=0
            linea3=linea-linea2
            while cont!=20:
                mostrar+=[lista[linea3]]
                linea3+=1
                cont+=1
                
            lista
            buscar
            linea+=20
            linea2
        else:
            lista
            buscar
            linea+=20
            linea2
    lista=Listbox(ventanaReservacion, font=("Times New Roman",14), bg="white", fg="Black")
    lista.pack()
    cont=0
    for datos in mostrar:
        lista.insert(cont,f"linea {cont} : {datos}")
        cont+=1
    etiqueta=tkinter.Label(ventanaReservacion,text=f"Estos son las reservaciones encontrados según el dato que ingreso. ",font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.pack()
    def salirR():
        mensaje=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(mensaje):
            ventanaReservacion.destroy()
            return menu()
    
    boton=tkinter.Button(ventanaReservacion,text="continuar",font=("Times New Roman",14), bg="white", fg="Black",command=salirR)
    boton.pack()



    
def filtrar_por_informacion1(lista,buscar,linea,Existe,linea2):
    ventanaReservacion=Tk()
    ventanaReservacion.geometry("500x400")
    ventanaReservacion.configure(background="aqua")
    mostrar=[]
    while linea < len(lista):
        if buscar in lista[linea] or buscar in lista[linea+1]:
            cont=0
            linea3=linea-linea2
            while cont!=20:
                mostrar+=[lista[linea3]]
                linea3+=1
                cont+=1
                
            lista
            buscar
            linea+=20
            linea2
        else:
            lista
            buscar
            linea+=20
            linea2
    lista=Listbox(ventanaReservacion, font=("Times New Roman",14), bg="white", fg="Black")
    lista.pack()
    cont=0
    for datos in mostrar:
        lista.insert(cont,f"linea {cont} : {datos}")
        cont+=1
    etiqueta=tkinter.Label(ventanaReservacion,text=f"Estos son los viajes encontrados según el dato que ingreso. ",font=("Times New Roman",14), bg="white", fg="Black")
    etiqueta.pack()
    def salirR():
        mensaje=messagebox.askyesno("Salir", "¿Desea Salir?, Confirme...")
        if(mensaje):
            ventanaReservacion.destroy()
            return menu()
    
    boton=tkinter.Button(ventanaReservacion,text="continuar",font=("Times New Roman",14), bg="white", fg="Black",command=salirR)
    boton.pack()

def seEncuentra_Aux(placa,viajes):
    for datos in viajes:
        if(placa+"\n")==datos:
            return True
        else:
            continue
    return False
#------------------------------------------------------------------------------


def reservacion_de_viajes_aux(Numero,Nombre,CantidadVIP,CantidadNor,CantidadEco):
    from datetime import datetime
    archivo = open("Reservacion.txt","a")
    archivo.close()
    archivo2 = open("Gestion de viaje.txt")
    viajes = archivo2.readlines()
    linea = viajes.index(Numero+"\n")
    FechaHora = datetime.now()
    Empresa = viajes[linea+9]
    Transporte = viajes[linea+10]
    ciudaSalida = viajes[linea+2]
    ProvinciaSalida = viajes[linea+1]
    FechaSalida = viajes[linea+3]
    HoraSalida = viajes[linea+4]
    ciudadLlegada = viajes[linea+6]
    ProvinciaLlegada = viajes[linea+5]
    FechaLlegada = viajes[linea+7]
    HoraLlegada = viajes[linea+8]
    Placa = viajes[linea+10]
    archivo3 = open("Gestion de Transporte.txt")
    transporte= archivo3.readlines()
    lineaT = transporte.index(Placa)
    VIPdisponible = transporte[lineaT+6]
    if int(VIPdisponible) - int(CantidadVIP)>= 0:
        NormalDisponible = transporte[lineaT+7]
        if int(NormalDisponible) - int(CantidadNor)>= 0:
            EconomicoDisponible = transporte[lineaT+8]
            if int(EconomicoDisponible) - int(CantidadEco)>= 0:
                Monto = int(CantidadVIP)*(int(viajes[linea+11]))
                Monto2 = int(CantidadNor)*(int(viajes[linea+12]))
                Monto3 = int(CantidadEco)*(int(viajes[linea+13]))
                Archivo = open("Reservacion.txt")
                reservaciones = Archivo.readlines()
                cont=1
                for n in reservaciones:
                    cont+=1
                cont=cont//20+1
                Archivo = open("Reservacion.txt","a")
                FechaHora = datetime.now()
                
                Archivo.write(str(cont)+"\n")
                Archivo.write(Nombre+"\n")
                Archivo.write(str(Numero)+"\n")
                Archivo.write(str(FechaHora)[:10]+"\n")
                Archivo.write(str(FechaHora)[10:18]+"\n")
                Archivo.write(Empresa)
                Archivo.write(Transporte)
                Archivo.write(ProvinciaSalida)
                Archivo.write(ciudaSalida)                
                Archivo.write(FechaSalida)
                Archivo.write(HoraSalida)
                Archivo.write(ProvinciaLlegada)
                Archivo.write(ciudadLlegada)
                
                Archivo.write(FechaLlegada)
                Archivo.write(HoraLlegada)
                Archivo.write(CantidadVIP+"\n")
                Archivo.write(CantidadNor+"\n")
                Archivo.write(CantidadEco+"\n")
                Archivo.write(str(Monto+Monto2+Monto3)+"\n")
                Archivo.write("......................................................."+"\n")


    
menu()
