import tkinter as tk
from tkinter import *
from tkinter import StringVar, ttk, messagebox, filedialog
from PIL import ImageTk, Image
from tkcalendar import *
from tkcalendar import DateEntry
from  datetime import date
import sqlite3
import os
import shutil
import threading
import pyperclip
import random

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.title("PawSystem")
ventana.iconbitmap('paw-icon.ico')
ventana.configure(bg='#0a4369') 

conexion = sqlite3.connect("dbomeyocan.db")
cursor = conexion.cursor()

##### PERROS ##### ----------------===============------------------===============------------------================--------------

#Variables Perros ----------------------------------------------------------------------------------
idP = StringVar()
nombreP = StringVar()
fechanacimientoP = StringVar()
sexoP = StringVar()
razaP = StringVar()
colorP = StringVar()
peloP = StringVar()
tallaP = StringVar()
temperamentoP = StringVar()
esterilizacionP = StringVar()
discapacidadP = StringVar()
adoptableP = StringVar()
fechaesterilizacionP = StringVar()
fechaingresoP = StringVar()

#CRUD Perros ---------------------------------------------------------------------------------------------
def limpiarCamposP():
    idP.set("")
    nombreP.set("")
    fechanacimientoP.set("")
    sexoP.set("")
    razaP.set("")
    colorP.set("")
    peloP.set("")
    tallaP.set("")
    temperamentoP.set("")
    esterilizacionP.set("")
    discapacidadP.set("")
    adoptableP.set("")
    fechaesterilizacionP.set("")
    fechaingresoP.set("")
    peloOtroP.set("")

def crearP(fMainframe2):
    #Conversiones 
    fechaesterilizacionP = date_fecha_esterilizacionp.get_date()
    fechaingresoP = date_fecha_ingresop.get_date()
    if(mesNacP=="01" or mesNacP=="02" or mesNacP=="03" or mesNacP=="04" or mesNacP=="05" or mesNacP=="06" or mesNacP=="07" or mesNacP=="08" or mesNacP=="09" or mesNacP=="10" or mesNacP=="11" or mesNacP=="12"):
        fechanacimientoP = anoNacP.get() + "-" + mesNacP
    elif(mesNacP=="N/A"):
        fechanacimientoP = anoNacP.get()
    else:
        fechanacimientoP = mesNacP
    sexoPerro = RBsexop.get()
    if sexoPerro == 1:
        sexoP = "Hembra"
    elif sexoPerro == 2:
        sexoP = "Macho"
    esterilizacionPerro = RBesterilizacionp.get()
    if esterilizacionPerro == 1:
        esterilizacionP = "Si"
    elif esterilizacionPerro == 2:
        esterilizacionP = "No"
        fechaesterilizacionP = "N/A"
    adoptablePerro = RBadoptablep.get()
    if adoptablePerro == 1:
        adoptableP = "Si"
    elif adoptablePerro == 2:
        adoptableP = "No"
    tallaPerro = RBtallap.get()
    if tallaPerro == 1:
        tallaP = "Chico"
    elif tallaPerro == 2:
        tallaP = "Mediano"
    elif tallaPerro == 3:
        tallaP = "Grande"
    peloPerro = RBpelop.get()
    if peloPerro == 1:
        peloP = "Corto"
    elif peloPerro == 2:
        peloP = "Largo"
    elif peloPerro == 3:
        peloP = "Duro"
    elif peloPerro == 4:
        peloP = "Alambre"
    elif peloPerro == 5:
        peloP = "Chino"
    elif peloPerro == 6:
        peloP = str(peloOtroP.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(nombreP.get())
        print(fechanacimientoP)
        print(sexoP)
        print(razaP.get())
        print(colorP.get())
        print(str(peloP))
        print(tallaP)
        print(temperamentoP.get())
        print(esterilizacionP)
        print(discapacidadP.get())
        print(adoptableP)
        print(str(fechaesterilizacionP))
        print(str(fechaingresoP))
        datosP = nombreP.get(), fechanacimientoP, sexoP, razaP.get(), colorP.get(), peloP, tallaP, temperamentoP.get(), esterilizacionP, discapacidadP.get(), adoptableP, str(fechaesterilizacionP), str(fechaingresoP)
        cursor.execute("INSERT INTO perros VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosP))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro")
        pass
    limpiarCamposP()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_perros()
    mostrarCamposP()

def editarP(fMainframe2):
    fechaesterilizacionP = date_fecha_esterilizacionp.get_date()
    fechaingresoP = date_fecha_ingresop.get_date()
    if(mesNacP=="01" or mesNacP=="02" or mesNacP=="03" or mesNacP=="04" or mesNacP=="05" or mesNacP=="06" or mesNacP=="07" or mesNacP=="08" or mesNacP=="09" or mesNacP=="10" or mesNacP=="11" or mesNacP=="12"):
        fechanacimientoP = anoNacP.get() + "-" + mesNacP
    elif(mesNacP=="N/A"):
        fechanacimientoP = anoNacP.get()
    else:
        fechanacimientoP = mesNacP
    sexoPerro = RBsexop.get()
    if sexoPerro == 1:
        sexoP = "Hembra"
    elif sexoPerro == 2:
        sexoP = "Macho"
    esterilizacionPerro = RBesterilizacionp.get()
    if esterilizacionPerro == 1:
        esterilizacionP = "Si"
    elif esterilizacionPerro == 2:
        esterilizacionP = "No"
        fechaesterilizacionP = "N/A"
    adoptablePerro = RBadoptablep.get()
    if adoptablePerro == 1:
        adoptableP = "Si"
    elif adoptablePerro == 2:
        adoptableP = "No"
    tallaPerro = RBtallap.get()
    if tallaPerro == 1:
        tallaP = "Chico"
    elif tallaPerro == 2:
        tallaP = "Mediano"
    elif tallaPerro == 3:
        tallaP = "Grande"
    peloPerro = RBpelop.get()
    if peloPerro == 1:
        peloP = "Corto"
    elif peloPerro == 2:
        peloP = "Largo"
    elif peloPerro == 3:
        peloP = "Duro"
    elif peloPerro == 4:
        peloP = "Alambre"
    elif peloPerro == 5:
        peloP = "Chino"
    elif peloPerro == 6:
        peloP = str(peloOtroP.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(nombreP.get())
        print(fechanacimientoP)
        print(sexoP)
        print(razaP.get())
        print(colorP.get())
        print(str(peloP))
        print(tallaP)
        print(temperamentoP.get())
        print(esterilizacionP)
        print(discapacidadP.get())
        print(adoptableP)
        print(str(fechaesterilizacionP))
        print(str(fechaingresoP))
        datosP = nombreP.get(), fechanacimientoP, sexoP, razaP.get(), colorP.get(), peloP, tallaP, temperamentoP.get(), esterilizacionP, discapacidadP.get(), adoptableP, str(fechaesterilizacionP), str(fechaingresoP)
        cursor.execute("UPDATE perros SET NOMBRE=?, FECHANACIMIENTO=?, SEXO=?, RAZA=?, COLOR=?, PELO=?, TALLA=?, TEMPERAMENTO=?, ESTERILIZACION=?, DISCAPACIDAD=?, ADOPTABLE=?, FECHAESTERILIZACION=?, FECHAINGRESO=? WHERE ID="+selectedp, (datosP))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al editar el registro")
        pass
    limpiarCamposP()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_perros()
    mostrarCamposP()

def mostrarCamposP():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosP = treeVP.get_children()
    for elemento in registrosP:
        treeVP.delete(elemento)
    try:
        cursor.execute("SELECT * FROM perros")
        for row in cursor:
            treeVP.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
    except:
        pass

def seleccionarUsandoClickP(treeVP):
    global selectedp
    global valuesp
    selectedp = None
    valuesp = None
    selectedp = treeVP.focus()
    valuesp = treeVP.item(selectedp,'values')
    print(selectedp)
    print(valuesp)

def borrarRegistroP():
    try:
        valuesp
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un perro por favor")
        ventana_perros.deiconify()
        return
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    if messagebox.askyesno(message="¿Realmente desea eliminar el registro? Se borrarán los datos y las imágenes", title="ADVERTENCIA"):
        try:
            try:
                path_2erase_p = os.getcwd() + "\\pimg\\" + selectedp
                shutil.rmtree(path_2erase_p)
            except OSError:
                pass
            cursor.execute("DELETE FROM perros WHERE ID="+selectedp)
            conexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass
    mostrarCamposP()

def mostrarCamposPa():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosP = treeVPa.get_children()
    for elemento in registrosP:
        treeVPa.delete(elemento)
    try:
        cursor.execute("SELECT * FROM perrosarchivados")
        for row in cursor:
            treeVPa.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
    except:
        pass

def archivarP():
    try:
        valuesp
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un perro por favor")
        ventana_perros.deiconify()
        return
    if messagebox.askyesno(message="¿Realmente desea archivar el registro?", title="ADVERTENCIA"):
        global estadoPa
        estadoPa = ""
        ventana_archivar_estadoP()
        ventana_perros.wait_window(ventana_archivar_estado_perros)
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM perros WHERE ID="+selectedp)
            conexion.commit()
            print("Archivando perro")
            datosPa = [selectedp]
            for i in range(len(valuesp)):
                datosPa.append(valuesp[i])
            datosPa.append(estadoPa)
            cursor.execute("INSERT INTO perrosarchivados VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosPa))
            conexion.commit()
            mostrarCamposP()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al archivar el perro")
            pass

def desarchivarP():
    if messagebox.askyesno(message="¿Realmente desea desarchivar el registro?", title="ADVERTENCIA"):
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM perrosarchivados WHERE ID="+selectedp)
            conexion.commit()
            print("Desarchivando perro")
            datosPa = [selectedp]
            for i in range(len(valuesp)):
                datosPa.append(valuesp[i])
            datosPa.pop()
            cursor.execute("INSERT INTO perros VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosPa))
            conexion.commit()
            mostrarCamposPa()
            mostrarCamposP()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al desarchivar el perro")
            pass

def buscarPa():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_perro_arch = busqueda_entryPa.get()
    #print(lookup_perro_arch)
    #print(selCbpa)
    for record in treeVPa.get_children():
        treeVPa.delete(record)
    try:
        cursor.execute("SELECT * FROM perrosarchivados WHERE "+selCbpa+" like ?",(lookup_perro_arch,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposPa()
        else:
            for record in records:
                treeVPa.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposPa()
    ventana_buscar_perros_arch.destroy()

def buscarP():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_perro = busqueda_entryP.get()
    #print(lookup_perro)
    #print(selCbp)
    for record in treeVP.get_children():
        treeVP.delete(record)
    try:
        cursor.execute("SELECT * FROM perros WHERE "+selCbp+" like ?",(lookup_perro,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposP()
        else:
            for record in records:
                treeVP.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposP()
    ventana_buscar_perros.destroy()

def clear_entradas_perros():
    e_nombrep.delete(0,END)
    e_anoNacP.delete(0,END)
    e_razap.delete(0,END)
    e_colorp.delete(0,END)
    e_pelop.delete(0,END)
    e_temperamentop.delete(0,END)
    e_discapacidadp.delete(0,END)

def insertar_editables_perros():
    global mesNacP
    #0 nombre
    e_nombrep.insert(0,valuesp[0])
    #1 fecha nacimiento
    if(valuesp[1]=="Cachorro" or valuesp[1]=="Joven" or valuesp[1]=="Adulto" or valuesp[1]=="Viejito"):
        comboP.set(valuesp[1])
        mesNacP = valuesp[1]
    else:
        try:
            split_fnp = valuesp[1].split('-')
            e_anoNacP.insert(0,split_fnp[0])
            comboP.current(newindex=int(split_fnp[1])-1)
            mesNacP = split_fnp[1]
        except:
            comboP.current(newindex=12)
            mesNacP = "N/A"
    #2 sexo
    if valuesp[2] == 'Hembra':
        RBsexop.set(1)
    elif valuesp[2] == 'Macho':
        RBsexop.set(2)
    #3 raza
    e_razap.insert(0,valuesp[3])
    #4 color
    e_colorp.insert(0,valuesp[4])
    #5 pelo
    if valuesp[5] == 'Corto':
        RBpelop.set(1)
    elif valuesp[5] == 'Largo':
        RBpelop.set(2)
    elif valuesp[5] == 'Duro':
        RBpelop.set(3)
    elif valuesp[5] == 'Alambre':
        RBpelop.set(4)
    elif valuesp[5] == 'Chino':
        RBpelop.set(5)
    else:
        RBpelop.set(6)
        e_pelop.insert(0,valuesp[5])
    #6 talla
    if valuesp[6] == 'Chico':
        RBtallap.set(1)
    elif valuesp[6] == 'Mediano':
        RBtallap.set(2)
    elif valuesp[6] == 'Grande':
        RBtallap.set(3)
    #7 temperamento
    e_temperamentop.insert(0,valuesp[7])
    #8 esterilizacion
    if valuesp[8] == 'Si':
        RBesterilizacionp.set(1)
    elif valuesp[8] == 'No':
        RBesterilizacionp.set(2)
    #9 discapacidad
    e_discapacidadp.insert(0,valuesp[9])
    #10 adoptable
    if valuesp[10] == 'Si':
        RBadoptablep.set(1)
    elif valuesp[10] == 'No':
        RBadoptablep.set(2)
    #11 fecha esterilizacion
    if not valuesp[11] == "N/A":
        split_fep = valuesp[11].split('-')
        fep_date = date(int(split_fep[0]),int(split_fep[1]),int(split_fep[2]))
        date_fecha_esterilizacionp.set_date(fep_date)
    #12 fecha ingreso
    split_fip = valuesp[12].split('-')
    fip_date = date(int(split_fip[0]),int(split_fip[1]),int(split_fip[2]))
    date_fecha_ingresop.set_date(fip_date)

#Ventanas Perros -------------------------------------------------------------------------------------------
def ventana_archivar_estadoP():
    global ventana_archivar_estado_perros
    ventana_archivar_estado_perros = tk.Toplevel()
    ventana_archivar_estado_perros.geometry("380x230")
    ventana_archivar_estado_perros.title("PawSystem Perros Archivar Motivo")
    ventana_archivar_estado_perros.iconbitmap('paw-icon.ico')
    ventana_archivar_estado_perros.configure(bg='#0a4369')
    ventana_archivar_estado_perros.resizable(False, False)
    lbl_vaep = Label(ventana_archivar_estado_perros, text="Motivo:", bg='#0a4369', fg="white",font='Helvetica 20')
    lbl_vaep.pack(pady=10)
    RBestadop = IntVar()
    RBestadop.set(1)
    rb_ep1 = tk.Radiobutton(ventana_archivar_estado_perros, text="Adoptado", padx = 5, variable=RBestadop, value=1,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
    rb_ep1.pack(pady=10)
    rb_ep2 = tk.Radiobutton(ventana_archivar_estado_perros, text="Fallecido", padx = 5, variable=RBestadop, value=2,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
    rb_ep2.pack(pady=10)
    btn_aceptar = Button(ventana_archivar_estado_perros, text="Aceptar", width=7, font='Helvetica 13 bold', bg='#33ff6d',command=lambda: aceptar(RBestadop))
    btn_aceptar.pack(pady=10)

    def aceptar(RBestadop):
        global estadoPa
        if RBestadop.get() == 1:
            estadoPa = "Adoptado"
        else:
            estadoPa = "Fallecido"
        ventana_archivar_estado_perros.destroy()

def ventana_buscarPa():
    global ventana_buscar_perros_arch
    ventana_buscar_perros_arch = tk.Toplevel()
    ventana_buscar_perros_arch.geometry("700x300")
    ventana_buscar_perros_arch.title("PawSystem Perros Búsqueda")
    ventana_buscar_perros_arch.iconbitmap('paw-icon.ico')
    ventana_buscar_perros_arch.configure(bg='#0a4369')
    ventana_buscar_perros_arch.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_perros_arch, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_perros_arch,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso","Estado"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_perros_arch, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryPa
    busqueda_entryPa = ttk.Entry(ventana_buscar_perros_arch,font=('Helvetica 10'))
    busqueda_entryPa.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_perros_arch, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBP = Button(ventana_buscar_perros_arch, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_perros_arch.destroy())
    btn_cancelarBP.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbpa
        selCbpa = None
        selCbpa = combo.get()
        #print(selCbpa)
        match selCbpa:
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del perro")
                selCbpa = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbpa = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbpa = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba la raza del perro")
                selCbpa = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del perro")
                selCbpa = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del perro")
                selCbpa = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del perro")
                selCbpa = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del perro")
                selCbpa = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbpa = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbpa = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbpa = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbpa = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbpa = "FECHAINGRESO"
            case "Estado":
                lbl_busqueda_formato.config(text="escriba Adoptado o Fallecido")
                selCbpa = "STATUS"
        #print(selCbpa)
        
    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarP = Button(ventana_buscar_perros_arch, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarPa)
    btn_buscarP.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def ventana_buscarP():
    global ventana_buscar_perros
    ventana_buscar_perros = tk.Toplevel()
    ventana_buscar_perros.geometry("700x300")
    ventana_buscar_perros.title("PawSystem Perros Búsqueda")
    ventana_buscar_perros.iconbitmap('paw-icon.ico')
    ventana_buscar_perros.configure(bg='#0a4369')
    ventana_buscar_perros.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_perros, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_perros,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_perros, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryP
    busqueda_entryP = ttk.Entry(ventana_buscar_perros,font=('Helvetica 10'))
    busqueda_entryP.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_perros, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBP = Button(ventana_buscar_perros, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_perros.destroy())
    btn_cancelarBP.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbp
        selCbp = None
        selCbp = combo.get()
        #print(selCbp)
        match selCbp:
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del perro")
                selCbp = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbp = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbp = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba la raza del perro")
                selCbp = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del perro")
                selCbp = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del perro")
                selCbp = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del perro")
                selCbp = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del perro")
                selCbp = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbp = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbp = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbp = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbp = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbp = "FECHAINGRESO"
        #print(selCbp)
        
    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarP = Button(ventana_buscar_perros, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarP)
    btn_buscarP.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def crear_ventana_perros():
    global ventana_perros
    ventana_perros = tk.Toplevel()
    ventana_perros.geometry("1280x860")
    ventana_perros.title("PawSystem Perros")
    ventana_perros.iconbitmap('paw-icon.ico')
    ventana_perros.configure(bg='#0a4369')
    ventana_perros.state('zoomed')
    
    if not os.path.exists(os.path.join(os.getcwd(), "pimg")):
        os.makedirs(os.path.join(os.getcwd(), "pimg"))

def crear_ventana_perros_archivados():
    global ventana_perros_archivados
    ventana_perros_archivados = tk.Toplevel()
    ventana_perros_archivados.geometry("1280x860")
    ventana_perros_archivados.title("PawSystem Perros Archivados")
    ventana_perros_archivados.iconbitmap('paw-icon.ico')
    ventana_perros_archivados.configure(bg='#0a4369')
    ventana_perros_archivados.state('zoomed')

def abrir_ventana_perros_archivados():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_perros_archivados, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)
    
    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vpa = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vpa.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vpa_Perros = tk.Label(fHeader_vpa, text="Perros archivados", font='Helvetica 36 bold', bg='#0a4369', fg='pink').pack(side='left', padx=10)
    btn_vp_Buscar = tk.Button(fHeader_vpa, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarPa).pack(side='right', padx=10)
    btn_vp_LimpiarBusqueda = tk.Button(fHeader_vpa, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposPa).pack(side='right', padx=10, pady=(30,0))

    #CONTENTS =============================================================================================================================
    fContents_vpa= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vpa.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso","estado")
    global treeVPa
    treeVPa = ttk.Treeview(fContents_vpa)
    columnas_perros(column_names, treeVPa)
    headings_perros(treeVPa)
    treeVPa.heading("estado", text="Estado")
    treeVPa.column("estado",width=40, minwidth=10)
    treeVPa.place(relwidth=0.98, relheight=0.96)
    scrollbar_perros(fContents_vpa, treeVPa)
    mostrarCamposPa()
    treeVPa.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickP(treeVPa))

    #FOOTER =============================================================================================================================
    fFooter_vpa= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vpa.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vpa_Regresar = tk.Button(fFooter_vpa, text="Regresar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_perros_archivados.destroy(), ventana_perros.deiconify(),seleccionarUsandoClickP(treeVP)]).pack(side='right', padx=10)
    btn_vpa_Desarchivar = tk.Button(fFooter_vpa, text="Desarchivar", font='Helvetica 20 bold', bg='#aaf76a', command=lambda:[desarchivarP()]).pack(side='left', padx=10)
    btn_vpa_VerFotos = tk.Button(fFooter_vpa, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[crear_ventana_ver_fotos(True),ventana_perros_archivados.iconify()]).pack(side='left', padx=10)

def abrir_ventana_perros():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_perros, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)
    
    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vp = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vp.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vp_Perros = tk.Label(fHeader_vp, text="Perros", font='Helvetica 36 bold', bg='#0a4369', fg='pink').pack(side='left', padx=10)
    btn_vp_Agregar = tk.Button(fHeader_vp, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: agregar_perritos(True)).pack(side='right', padx=10)
    btn_vp_Buscar = tk.Button(fHeader_vp, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarP).pack(side='right', padx=10)
    btn_vp_LimpiarBusqueda = tk.Button(fHeader_vp, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposP).pack(side='right', padx=10, pady=(30,0))
    
    #CONTENTS =============================================================================================================================
    fContents_vp= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vp.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)
    
    column_names = ("nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso")
    global treeVP
    treeVP = ttk.Treeview(fContents_vp)
    columnas_perros(column_names, treeVP)
    headings_perros(treeVP)
    treeVP.place(relwidth=0.98, relheight=0.96)
    
    mostrarCamposP()
    treeVP.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickP(treeVP))

    scrollbar_perros(fContents_vp, treeVP)
    
    #FOOTER =============================================================================================================================
    fFooter_vp= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vp.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vp_MenuPrincipal = tk.Button(fFooter_vp, text="Menú principal", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_perros.destroy(), ventana.deiconify()]).pack(side='right', padx=10)
    btn_vp_VerArchivados = tk.Button(fFooter_vp, text="Ver archivados", font='Helvetica 20 bold', bg='#bd95fc', command=lambda:[crear_ventana_perros_archivados(), abrir_ventana_perros_archivados(), ventana_perros.iconify()]).pack(side='right', padx=10)
    btn_vp_VerFotos = tk.Button(fFooter_vp, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[ventana_perros.iconify(),crear_ventana_ver_fotos(False)]).pack(side='left', padx=10)
    btn_vp_Publicar = tk.Button(fFooter_vp, text="Publicar", font='Helvetica 20 bold', bg='#f2925e',command=lambda: [ventana_perros.iconify(),ventanaPublicarP()]).pack(side='left', padx=10)
    btn_vp_Editar = tk.Button(fFooter_vp, text="Editar", font='Helvetica 20 bold', bg='#34ebc3', command=lambda: agregar_perritos(False)).pack(side='left', padx=10)
    btn_vp_Archivar = tk.Button(fFooter_vp, text="Archivar", font='Helvetica 20 bold', bg='pink', command=lambda:archivarP()).pack(side='left', padx=10)
    btn_vp_Borrar = tk.Button(fFooter_vp, text="Borrar", font='Helvetica 20 bold', bg='#f03932',command=lambda: borrarRegistroP()).pack(side='left', padx=10)

    #Ventana para agregar perritos
    def agregar_perritos(add):
        if add == False:
            try:
                valuesp
            except NameError:
                messagebox.showwarning("Advertencia","Seleccione un perro por favor")
                return

        fMainFrame1.destroy()
        fMainFrame2 = tk.Frame(ventana_perros, bg='#0a4369')
        fMainFrame2.pack(fill="both", expand=True)

        fagregar_p_header = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_p_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
        lbl_Vagregar_Perros = tk.Label(fagregar_p_header, text="Perros", font='Helvetica 30 bold', bg='#0a4369', fg='pink').pack(side='left', padx=10)

        fagregar_p = tk.Frame(fMainFrame2, bg = '#0a4369')
        fagregar_p.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.77)

        fagregar_p_footer = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_p_footer.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
        btn_Vagregar_cancelar = tk.Button(fagregar_p_footer, text="Cancelar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: [fMainFrame2.destroy(), abrir_ventana_perros()]).pack(side='right', padx=10)

        #Labels de categorias
        labels_formulario_perros(fagregar_p)

        #Calendarios de las categorias
        calendarios_formulario_perros(fagregar_p)

        #Entradas de las categorias
        entradas_formulario_perros(fagregar_p)

        #Radio Buttons de las categorias
        radiobtns_formulario_perros(fagregar_p)

        def selectionComboP(event):
            global mesNacP
            mesNacP = StringVar()
            mesNacP = comboP.get()
            match mesNacP:
                case "Enero":
                    mesNacP = "01"
                case "Febrero":
                    mesNacP = "02"
                case "Marzo":
                    mesNacP = "03"
                case "Abril":
                    mesNacP = "04"
                case "Mayo":
                    mesNacP = "05"
                case "Junio":
                    mesNacP = "06"
                case "Julio":
                    mesNacP = "07"
                case "Agosto":
                    mesNacP = "08"
                case "Septiembre":
                    mesNacP = "09"
                case "Octubre":
                    mesNacP = "10"
                case "Noviembre":
                    mesNacP = "11"
                case "Diciembre":
                    mesNacP = "12"
                case "No aplica":
                    mesNacP = "N/A"
                case "Cachorro":
                    mesNacP = "Cachorro"
                case "Joven":
                    mesNacP = "Joven"
                case "Adulto":
                    mesNacP = "Adulto"
                case "Viejito":
                    mesNacP = "Viejito"

        global comboP
        comboP = ttk.Combobox(fagregar_p,state="readonly", font='Helvetica 10', values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre","No aplica","Cachorro", "Joven", "Adulto", "Viejito"])
        comboP.grid(row=1,column=1,padx=70,sticky=W)
        comboP.bind("<<ComboboxSelected>>", selectionComboP)

        if add == True:
            btn_Vagregar_Agregar = tk.Button(fagregar_p_header, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[crearP(fMainFrame2)]).pack(side='right', padx=10)
        elif add == False:
            btn_Vagregar_Editar = tk.Button(fagregar_p_header, text="Guardar cambios", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[editarP(fMainFrame2)]).pack(side='right', padx=10)
            clear_entradas_perros()
            insertar_editables_perros()

    def radiobtns_formulario_perros(fagregar_p):
        global RBsexop
        RBsexop = IntVar()
        RBsexop.set(1)
        rb_sp1 = tk.Radiobutton(fagregar_p, text="Hembra", padx = 5, variable=RBsexop, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_sp1.grid(row=3,column=1,sticky=W)
        rb_sp2 = tk.Radiobutton(fagregar_p, text="Macho", padx = 5, variable=RBsexop, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_sp2.grid(row=3,column=1,sticky=W,padx=120)

        global RBesterilizacionp
        RBesterilizacionp = IntVar()
        RBesterilizacionp.set(1)
        rb_ep1 = tk.Radiobutton(fagregar_p, text="Sí", padx = 10, variable=RBesterilizacionp, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_ep1.grid(row=9,column=1,sticky=W)
        rb_ep2 = tk.Radiobutton(fagregar_p, text="No", padx = 10, variable=RBesterilizacionp, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_ep2.grid(row=9,column=1,sticky=W,padx=90)

        global RBadoptablep
        RBadoptablep = IntVar()
        RBadoptablep.set(1)
        rb_ap1 = tk.Radiobutton(fagregar_p, text="Sí", padx = 10, variable=RBadoptablep, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_ap1.grid(row=11,column=1,sticky=W)
        rb_ap2 = tk.Radiobutton(fagregar_p, text="No", padx = 10, variable=RBadoptablep, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_ap2.grid(row=11,column=1,sticky=W,padx=90)

        global RBpelop
        RBpelop = IntVar()
        RBpelop.set(1)
        rb_pp1 = tk.Radiobutton(fagregar_p, text="Corto", padx = 10, variable=RBpelop, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp1.grid(row=6,column=1,sticky=W)
        rb_pp2 = tk.Radiobutton(fagregar_p, text="Largo", padx = 10, variable=RBpelop, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp2.grid(row=6,column=1,sticky=W,padx=(90,0))
        rb_pp3 = tk.Radiobutton(fagregar_p, text="Duro", padx = 10, variable=RBpelop, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp3.grid(row=6,column=1,sticky=W,padx=(182,0))
        rb_pp4 = tk.Radiobutton(fagregar_p, text="Alambre", padx = 10, variable=RBpelop, value=4,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp4.grid(row=6,column=1,sticky=W,padx=(267,0))
        rb_pp5 = tk.Radiobutton(fagregar_p, text="Chino", padx = 10, variable=RBpelop, value=5,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp5.grid(row=6,column=1,sticky=W,padx=(377,0))
        rb_pp6 = tk.Radiobutton(fagregar_p, text="Otro:", padx = 10, variable=RBpelop, value=6,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_pp6.grid(row=6,column=1,sticky=W,padx=(469,0))

        global RBtallap
        RBtallap = IntVar()
        RBtallap.set(1)
        rb_tp1 = tk.Radiobutton(fagregar_p, text="Chico", padx = 5, variable=RBtallap, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_tp1.grid(row=7,column=1,sticky=W)
        rb_tp2 = tk.Radiobutton(fagregar_p, text="Mediano", padx = 5, variable=RBtallap, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_tp2.grid(row=7,column=1,sticky=W,padx=100)
        rb_tp3 = tk.Radiobutton(fagregar_p, text="Grande", padx = 5, variable=RBtallap, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='pink')
        rb_tp3.grid(row=7,column=1,sticky=W,padx=220)

    def entradas_formulario_perros(fagregar_p):
        global e_razap
        e_razap=tk.Entry(fagregar_p, textvariable=razaP,font=('Helvetica 14'))
        e_razap.grid(row=4,column=1,sticky=W)
        global e_colorp
        e_colorp=tk.Entry(fagregar_p, textvariable=colorP,font=('Helvetica 14'))
        e_colorp.grid(row=5,column=1,sticky=W)
        global peloOtroP
        peloOtroP = StringVar()
        global e_pelop
        e_pelop=tk.Entry(fagregar_p, textvariable=peloOtroP,font=('Helvetica 14'))
        e_pelop.grid(row=6,column=1,sticky=W,padx=(560,0))
        global e_temperamentop
        e_temperamentop=tk.Entry(fagregar_p, textvariable=temperamentoP,font=('Helvetica 14'))
        e_temperamentop.grid(row=8,column=1,sticky=W)
        global e_nombrep
        e_nombrep=tk.Entry(fagregar_p, textvariable=nombreP,font=('Helvetica 14'))
        e_nombrep.grid(row=0,column=1,sticky=W)
        global e_discapacidadp
        e_discapacidadp=tk.Entry(fagregar_p, textvariable=discapacidadP,font=('Helvetica 14'))
        e_discapacidadp.grid(row=10,column=1,sticky=W)
        global anoNacP
        anoNacP = StringVar()
        global e_anoNacP
        e_anoNacP=tk.Entry(fagregar_p, textvariable=anoNacP,font=('Helvetica 14'))
        e_anoNacP.grid(row=1,column=1,sticky=W,padx=(425,0))

    def calendarios_formulario_perros(fagregar_p):
        global date_fecha_esterilizacionp
        date_fecha_esterilizacionp = DateEntry(fagregar_p,selectmode ='day')
        date_fecha_esterilizacionp.grid(row=9,column=1, sticky=W,padx=(510,0))
        global date_fecha_ingresop
        date_fecha_ingresop = DateEntry(fagregar_p,selectmode ='day')
        date_fecha_ingresop.grid(row=2,column=1, sticky=W)

    def labels_formulario_perros(fagregar_p):
        lbl_nombre=tk.Label(fagregar_p,text="Nombre",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_nombre.grid(row=0,column=0,sticky=W,padx=20)
        lbl_fecha_nacimiento=tk.Label(fagregar_p,text="Fecha de nacimiento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento.grid(row=1,column=0,sticky=W,padx=(20,45),pady=7)
        lbl_fecha_nacimiento_mes=tk.Label(fagregar_p,text="mes:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_mes.grid(row=1, column=1,sticky=W,pady=7)
        lbl_fecha_nacimiento_year=tk.Label(fagregar_p,text="año:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_year.grid(row=1, column=1,sticky=W,pady=7,padx=(360,0))
        lbl_sexo=tk.Label(fagregar_p,text="Sexo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_sexo.grid(row=3,column=0,sticky=W,padx=20,pady=7)
        lbl_raza=tk.Label(fagregar_p,text="Raza",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_raza.grid(row=4,column=0,sticky=W,padx=20,pady=7)
        lbl_color=tk.Label(fagregar_p,text="Color",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_color.grid(row=5,column=0,sticky=W,padx=20,pady=7)
        lbl_pelo=tk.Label(fagregar_p,text="Pelo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_pelo.grid(row=6,column=0,sticky=W,padx=20,pady=7)
        lbl_talla=tk.Label(fagregar_p,text="Talla",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_talla.grid(row=7,column=0,sticky=W,padx=20,pady=7)
        lbl_temperamento=tk.Label(fagregar_p,text="Temperamento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_temperamento.grid(row=8,column=0,sticky=W,padx=20,pady=7)
        lbl_esterilizacion=tk.Label(fagregar_p,text="Esterilización",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_esterilizacion.grid(row=9,column=0,sticky=W,padx=20,pady=7)
        lbl_discapacidad=tk.Label(fagregar_p,text="Notas",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_discapacidad.grid(row=10,column=0,sticky=W,padx=20,pady=7)
        lbl_adoptable=tk.Label(fagregar_p,text="Adoptable",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_adoptable.grid(row=11,column=0,sticky=W,padx=20,pady=7)
        lbl_fecha_esterilizacion=tk.Label(fagregar_p,text="Fecha de esterilización:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_esterilizacion.grid(row=9,column=1,sticky=W,padx=(267,0),pady=7)
        lbl_fecha_ingreso=tk.Label(fagregar_p,text="Fecha de ingreso",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_ingreso.grid(row=2,column=0,sticky=W,padx=20,pady=7)

def scrollbar_perros(fContents_vp, treeVP):
    scrollbar1 = ttk.Scrollbar(fContents_vp, orient=tk.VERTICAL, command=treeVP.yview)
    treeVP.configure(yscroll=scrollbar1.set)
    scrollbar1.place(relx=0.98, relwidth=0.02, relheight=1)
    
    scrollbar2 = ttk.Scrollbar(fContents_vp, orient=tk.HORIZONTAL, command=treeVP.xview)
    treeVP.configure(xscroll=scrollbar2.set)
    scrollbar2.place(rely=0.96, relwidth=0.98, relheight=0.04)

def headings_perros(treeVP):
    treeVP.heading("nombre", text="Nombre")
    treeVP.heading("fechanacimiento", text="Fecha de nacimiento")
    treeVP.heading("sexo", text="Sexo")
    treeVP.heading("raza", text="Raza")
    treeVP.heading("color", text="Color")
    treeVP.heading("pelo", text="Pelo")
    treeVP.heading("talla", text="Talla")
    treeVP.heading("temperamento", text="Temperamento")
    treeVP.heading("esterilizacion", text="Esterilización")
    treeVP.heading("discapacidad", text="Notas")
    treeVP.heading("adoptable", text="Adoptable")
    treeVP.heading("fechaesterilizacion", text="Fecha de esterilización")
    treeVP.heading("fechaingreso", text="Fecha de ingreso")

def columnas_perros(column_names, treeVP):
    treeVP.configure(columns=column_names, show='headings')
    treeVP.column("#0",width=10, minwidth=10)
    treeVP.column("nombre",width=40, minwidth=10)
    treeVP.column("fechanacimiento",width=40, minwidth=10)
    treeVP.column("sexo",width=10, minwidth=10)
    treeVP.column("raza",width=40, minwidth=10)
    treeVP.column("color",width=15, minwidth=10)
    treeVP.column("pelo",width=40, minwidth=10)
    treeVP.column("talla",width=40, minwidth=10)
    treeVP.column("temperamento",width=40, minwidth=10)
    treeVP.column("esterilizacion",width=40, minwidth=10)
    treeVP.column("discapacidad",width=40, minwidth=10)
    treeVP.column("adoptable",width=40, minwidth=10)
    treeVP.column("fechaesterilizacion",width=40, minwidth=10)
    treeVP.column("fechaingreso",width=40, minwidth=10)

#Ventanas Fotos Perros ------------------------------------------------------------------------------------
def crear_ventana_ver_fotos(archivado):
    try:
        valuesp
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un perro por favor")
        ventana_perros.deiconify()
        return
    global ver_fotos_ven
    ver_fotos_ven = tk.Toplevel(ventana)
    ver_fotos_ven.geometry("1280x720")
    ver_fotos_ven.title("PawSystem Perros")
    ver_fotos_ven.iconbitmap('paw-icon.ico')
    ver_fotos_ven.configure(bg='#0a4369')
    ver_fotos_ven.state('zoomed')
    ver_fotos_ven.update_idletasks()
    folder_path = os.path.join(os.getcwd(), "pimg")
    # Verificar si la carpeta existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
 
    abrir_ventana_ver_fotos(archivado)

def abrir_ventana_ver_fotos(archivado):
    fMainFrame3 = tk.Frame(ver_fotos_ven, bg='#0a4369')
    fMainFrame3.pack(fill="both", expand=True)
    fVerfotos_p_header = tk.Frame(fMainFrame3, bg='#0a4369')
    fVerfotos_p_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    fverFotos_p_footer = tk.Frame(fMainFrame3, bg = '#0a4369')
    fverFotos_p_footer.place(relx=0.01, rely=0.81, relwidth=0.98, relheight=0.15)
   
   
    
    btn_regresar_p = tk.Button(fVerfotos_p_header, text = "Regresar", font='Helvetica 18 bold', bg='#33ff6d')
    btn_regresar_p.pack(side = 'left')

    lbl_vfp_n_Perros = Label(fVerfotos_p_header, text="", font='Helvetica 30 bold', bg='#0a4369', fg='pink')
    lbl_vfp_n_Perros.pack(side='left', padx=50)
    lbl_vfp_n_Perros.config(text=valuesp[0])
    lbl_vfp_fi_Perros = Label(fVerfotos_p_header, text = "",font='Helvetica 15 bold', bg='#0a4369', fg='pink')
    lbl_vfp_fi_Perros.pack(side = 'right',padx=5)
    lbl_vfp_fi_Perros.config(text = valuesp[12])
    lbl_vfp_fit_Perros = Label(fVerfotos_p_header, text = "Fecha de ingreso: ",font='Helvetica 15 bold', bg='#0a4369', fg='pink')
    lbl_vfp_fit_Perros.pack(side = 'right',padx=5)
    
    btn_agregarfoto_p = tk.Button(fverFotos_p_footer, text = "Agregar Foto", font='Helvetica 18 bold', bg='#33ff6d')
    btn_agregarfoto_p.pack(side= 'left', padx=45)
    btn_eliminarfotos_p = tk.Button(fverFotos_p_footer, text = "Eliminar foto", font='Helvetica 18 bold', bg='#db5142')
    btn_eliminarfotos_p.pack(side= 'right', padx=45)

    canvas_ver_foto_p = tk.Canvas(fverFotos_p_footer,height =70,width =500, bg = '#C1CDCD')
    canvas_ver_foto_p.pack(side = tk.BOTTOM,fill = tk.X)

    canvas_ver_foto_p.bind('<Configure>', lambda e:canvas_ver_foto_p.bbox('all'))
    slider = tk.Frame(canvas_ver_foto_p)
    canvas_ver_foto_p.create_window((0,0),window = slider, anchor = tk.NW)
    progbarFP = ttk.Progressbar(fVerfotos_p_header, orient='horizontal',mode='determinate',length=500)
    progbarFP.update_idletasks()
    progbarFP.pack(side=TOP,expand=YES)

    threading.Thread(target = lambda:contenido_ver_fotos(canvas_ver_foto_p,fverFotos_p_footer,fMainFrame3,archivado,slider,btn_agregarfoto_p,btn_regresar_p,btn_eliminarfotos_p,progbarFP)).start()

def contenido_ver_fotos(canvas_ver_foto_p,fverFotos_p_footer,fMainFrame3,archivado,slider,btn_agregarfoto_p,btn_regresar_p,btn_eliminarfotos_p,progbarFP):    
    #Frames de contenidos para fotos
    fVerFotos_p_contents = tk.Frame(fMainFrame3, bg = '#0a4369')
    fVerFotos_p_contents.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.71)

    #Botones ver fotos, regresar y eliminar COMMAND
    if archivado == False:
        btn_regresar_p.config(command = lambda: [ver_fotos_ven.destroy(),ventana_perros.deiconify()])
        btn_agregarfoto_p.config(command = lambda: [agregar_fotos_p(ver_fotos_ven),abrir_ventana_ver_fotos(False)])
    else:
        btn_regresar_p.config(command = lambda: [ver_fotos_ven.destroy(),ventana_perros_archivados.deiconify()])
        btn_agregarfoto_p.config(command = lambda: [agregar_fotos_p(ver_fotos_ven),abrir_ventana_ver_fotos(True)])
    btn_eliminarfotos_p.config(command = lambda:[eliminar_foto_p(dir_path_p_fotos, aux_index)])

    #Lbl desplegar imagenes
    lbl_desplegar_img_p = tk.Label(fVerFotos_p_contents,bg = '#0a4369')
    lbl_desplegar_img_p.pack(anchor = tk.CENTER)

    images_list_p = []
    images_vars_p = []

    global dir_path_p_fotos
    images_files = None
    dir_path_p_fotos = os.getcwd() + "/pimg/" + selectedp
    if not os.path.exists(dir_path_p_fotos):
        os.makedirs(dir_path_p_fotos)

    images_files = os.listdir(dir_path_p_fotos)
  
    for r in range(0, len(images_files)):
        original_image = Image.open(dir_path_p_fotos + '/' + images_files[r])
        width_img_p, height_img_p = original_image.size
        aspect_ratio_P = width_img_p/height_img_p
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_p = 500
        max_height_img_p = 500
        new_width_img_p = min(width_img_p, max_width_img_p)
        new_height_img_P = min(height_img_p, max_height_img_p)
        
        if aspect_ratio_P > 1:
            #Imagen más ancha que alta
            new_height_img_P = int(new_width_img_p / aspect_ratio_P)
        else:
            #Imagen más alta que ancha
            new_width_img_p = int(new_height_img_P * aspect_ratio_P)

        images_list_p.append([
                ImageTk.PhotoImage(original_image.resize((int(new_width_img_p/7),int(new_height_img_P/7) ), Image.Resampling.LANCZOS)),
                ImageTk.PhotoImage(resized_image.resize((new_width_img_p, new_height_img_P)), Image.Resampling.LANCZOS)
                             ])   
        images_vars_p.append(f'img_{r}')
        

        progbarFP['value'] += (100/len(images_files))
    progbarFP.pack_forget()
    
    
    def desplegar_img_p(index_p):
        global aux_index
        aux_index = index_p
        lbl_desplegar_img_p.config(image = images_list_p[index_p][1])
        lbl_desplegar_img_p.pack(side='left', anchor='center', expand=True)
            
    for n in range(len(images_vars_p)):
        globals()[images_vars_p[n]] = tk.Button(slider,image=images_list_p[n][0], bd = 0, command = lambda n = n:desplegar_img_p(n))
        globals()[images_vars_p[n]].pack(side =tk.LEFT)

    canvas_ver_foto_p.configure(scrollregion=canvas_ver_foto_p.bbox('all'))
    x_scroll_bar = tk.Scrollbar(fverFotos_p_footer, orient='horizontal')
    x_scroll_bar.pack(side = tk.BOTTOM,fill = tk.X)
    x_scroll_bar.configure(command=canvas_ver_foto_p.xview)
    canvas_ver_foto_p.configure(xscrollcommand=x_scroll_bar.set)
    slider.bind('<Configure>', lambda event: canvas_ver_foto_p.configure(scrollregion=canvas_ver_foto_p.bbox('all')))
    
    def eliminar_foto_p(dir_path_p_fotos, aux_index): 
        respuesta = messagebox.askyesno("Eliminar imagen","¿Seguro quieres eliminar la imagen?")
        if respuesta ==1:
            res = []
            for path in os.listdir(dir_path_p_fotos):
                # checar si el directorio es un archivo
                if os.path.isfile(os.path.join(dir_path_p_fotos, path)):
                    res.append(path) 
            deletepath = dir_path_p_fotos +"/" +str(res[aux_index])  
            os.remove(deletepath)
            fMainFrame3.destroy()
            if archivado == False:
                abrir_ventana_ver_fotos(False)
            else:
                abrir_ventana_ver_fotos(True)
        else:
            return 0
        
    def agregar_fotos_p(ventana):
        current_path_image = filedialog.askopenfilename(initialdir='Imagenes')   
        ruta_p,n_archivo_p = os.path.split(current_path_image)    
        new_path_image = dir_path_p_fotos + "/" + str(n_archivo_p)
        shutil.copyfile(current_path_image, new_path_image)
        fMainFrame3.destroy()

#Textos Perros ---------------------------------------------------------------------------------------------
def ventanaAdopcionP():
    ventana.withdraw()
    ventana_adop_p = tk.Toplevel()
    ventana_adop_p.geometry("1300x720")
    ventana_adop_p.title("Adopción")
    ventana_adop_p.iconbitmap('paw-icon.ico')
    ventana_adop_p.configure(bg='#0a4369')
    ventana_adop_p.state('zoomed')
    ventana_adop_p.update_idletasks()

    textos = [
        "SU 🎞 #HISTORIA CONTINÚA, en #ADOPCIÒN 🐾Un #rescate que aún sigue vigente"
        " 🇲🇽🐾\nNOMBRE: "+valuesp[0]+"\nNACIÓ: "+valuesp[1]+ "\nTALLA: "+valuesp[6]+"\nSEXO: "
        +valuesp[2]+" #"+valuesp[8]+"estaesterilizado\nTEMPERAMENTO: "+valuesp[7]+"#adopta"
        " #adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀"
        " #APADRINAMIENTOVIRTUAL #UnperritogatitoabandonadoenunHOGAR\nPara más información comunícate a:"
        " adopcionesvirtualesomeyocan@yahoo.com.mx #amigoperruno #amigogatuno #perritos #gatitos"
        " #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Conoce a "+valuesp[0]+ "! SU #HISTORIA CONTINUA en #ADOPCION. Nació "+valuesp[1]+" y es un #rescate"
        " que aún sigue vigente, TÚ puedes cambiar su vida\nTALLA: "+valuesp[6]+"\nSEXO:"
        +valuesp[2]+"\n#"+valuesp[8]+"estaesterilizado\nTEMPERAMENTO: "+valuesp[7]+" Con tu ayuda nuestro"
        " #Omeyocanito puede tener una vida mejor y compartir su felicidad y alegría con más personas"
        "\n#adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL"
        " #UnperritogatitoabandonadoenunHOGAR Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx" 
        "\n#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesp[0]+"!🐾 sigue aquí con nosotros. El es un #Omeyocanito "+valuesp[7]+". Estaríamos muy" 
        " felices de encontrarle una familia que le dé mucho amor.\nPara más información comunícate a:" 
        " adopcionesvirtualesomeyocan@yahoo.com.m #amigoperruno #amigogatuno #perritos"
        " #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesp[0]+", lleva un rato con nosotros, pero ya quiere conocer a las personas que serán"
        " su #familia ❤️. Es de talla"+valuesp[6]+" ¡ya es tiempo de darle la vida que merece!" 
        " Si no puedes adoptar puedes #apadrinar a"+valuesp[0]+" o #compartir para que encuentre un hogar"
        " 🐾❤️.\n#ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesp[0]+" merece una oportunidad!. Está con nosotros desde "+valuesp[12]+". Ayúdanos a encontrarle" 
        " una familia. Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx #adopta "
        "#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        ""+valuesp[0]+" 🐶es de talla "+valuesp[6]+". Es"+valuesp[7]+", y "+valuesp[2]+""  
        "Si quieres adoptar a "+valuesp[0]+" y que formen una hermosa familia juntos❤️🐾, contáctanos."
        "#ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        "adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        "🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        "Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        "#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Me llamo "+valuesp[0]+" estoy buscando una familia que me de mucho cariño🥰." 
        " Soy "+valuesp[7]+" y de tamaño "+valuesp[6]+". Ayúdame a encontrar la familia que tanto he esperado." 
        " #ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #-------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesp[0]+" ya quiere pertenece a una familia, es de talla "+valuesp[6]+"" 
        " Es "+valuesp[7]+". Estamos seguras de que le dará mucho a amor a la familia a la que vaya a pertenecer." 
        " Es muy amigable con otros perros y niños," 
        " pero necesita una familia que pueda brindarle la atención y el tiempo que necesita para mantenerse feliz y saludable."
        " #ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Soy "+valuesp[0]+" y soy de talla "+valuesp[6]+"." 
        " Soy "+valuesp[7]+" Necesito una familia que tenga tiempo y amor para dedicar a un perro activo como yo."
        " Si estás interesado en adoptarme, por favor asegúrate de que tienes el tiempo y los recursos necesarios para cuidarme adecuadamente." 
        " Estoy dispuesto a aprender y estoy ansioso por encontrar un hogar lleno de amor. ¡Gracias por considerarme!",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Hola nosotros somos #Omeyocan🖐🏼! Necesitamos tu ayuda🥹, "+valuesp[0]+" 🐶esta buscando una familia con quien compartir su felicidad y cariño ❤️"
        "\nNACIÓ: "+valuesp[1]+"\n"
        "TALLA: "+valuesp[6]+"\n"
        "SEXO: "+valuesp[2]+"\n"
        "#Esterilización "+valuesp[8]+"\n"
        "TEMPERAMENTO: "+valuesp[7]+"\n"
        " #ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_adop_p,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_adop_p.destroy)
    regresar.place(relx=0.01, rely=0.02)
    
    fotos = tk.Button(ventana_adop_p, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_p)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_adop_p, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_adop_p, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_adop_p, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_p = Label(ventana_adop_p,text="",font='Helvetica 30 bold', fg='pink', bg='#0a4369')
    lbl_nombre_p.place(relx=0.1, rely=0.02)
    lbl_nombre_p.config(text=valuesp[0])

    lbl_img_p = Label(ventana_adop_p,bg = '#0a4369')
    lbl_img_p.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_perro_pub(lbl_img_p)).start()

def ventanaNoAdopcionP():
    ventana.withdraw()
    ventana_no_adopt_p = tk.Toplevel()
    ventana_no_adopt_p.geometry("1300x720")
    ventana_no_adopt_p.title("No adopción")
    ventana_no_adopt_p.iconbitmap('paw-icon.ico')
    ventana_no_adopt_p.configure(bg='#0a4369')
    ventana_no_adopt_p.state('zoomed')
    ventana_no_adopt_p.update_idletasks()

    textos = [
        "¡Hola! Soy "+valuesp[0]+" estoy buscando apoyo para poder tener una vida digna🐾." 
        " No soy adoptable, pero puedes apadrinarme de manera virtual 🐶 en adopcionesvirtualesomeyocan@yahoo.com.mx." 
        " No todos podemos ser adoptables por distintas razones, pero siempre existen más maneras de apoyar. ❤️"
        " #APADRINA #noadoptable #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Existen muchos Omeyocanitos que no tienen la posibilidad de ser adoptados😥 ya que algunos se encuentran" 
        " en rehabilitación física y/o emocional, pero puedes apadrinar.\n" 
        ""+valuesp[0]+"🐾💞 no tiene la posibilidad y busca TU🫵 ayuda para poder tener la vida que merece." 
        " adopcionesvirtualesomeyocan@yahoo.com.mx #APADRINA #noadoptable #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesp[0]+" te necesita! Aunque 🚫NO es ADOPTABLE🚫 podrías hacer que tenga una mejor vida y pronta rehabilitación ❤‍🩹 ." 
        " En #Omeyocan hay #omeyocanitos que requieren de atención especial y rehabilitación física o emocional, sin embargo," 
        " puedes #apadrinar y contribuir y hacer el cambio 💓. Esta con nosotros desde "+valuesp[12]+". \n"
        "NACIÓ: "+valuesp[1]+"\n"
        "TALLA: "+valuesp[6]+"\n"
        "SEXO: "+valuesp[2]+"\n"
        "#Esterilizado\n"
        " TEMPERAMENTO: "+valuesp[7]+""
        " 🧚🏻‍♀ APADRINAMIENTO VIRTUAL, comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx para mas informarción."
        " #APADRINA"
        " #UnperritogatitoabandonadoenunHOGAR",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Haz la diferencia en la vida de "+valuesp[0]+"! Apadrina a uno de los adorables perros de Omeyocan, un refugio dedicado a cuidar y proteger a los animales." 
        " Tu apadrinamiento ayudará a cubrir los costos de alimentación, atención médica y cuidado diario de estos perros mientras esperan encontrar un hogar amoroso y permanente." 
        " ¡Únete a nosotros en nuestra misión de brindar una vida mejor a estos perros necesitados!"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "🚫"+valuesp[0]+" NO ES ADOPTABLE🚫\n"
        " Lleva con nosotros desde "+valuesp[12]+", necesita de tu apoyo para salir adelante,"
        " aunque 🚫NO ES ADOPTABLE🚫 puedes #Apadrinar para ayudar a su cuidado.\n"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_no_adopt_p,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_no_adopt_p.destroy)
    regresar.place(relx=0.01, rely=0.02)
    
    fotos = tk.Button(ventana_no_adopt_p, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_p)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_no_adopt_p, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_no_adopt_p, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_no_adopt_p, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_p = Label(ventana_no_adopt_p,text="",font='Helvetica 30 bold', fg='pink', bg='#0a4369')
    lbl_nombre_p.place(relx=0.1, rely=0.02)
    lbl_nombre_p.config(text=valuesp[0])

    lbl_img_p = Label(ventana_no_adopt_p,bg = '#0a4369')
    lbl_img_p.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_perro_pub(lbl_img_p)).start()

def ventanaDonarP():
    ventana.withdraw()
    donar_p = tk.Toplevel()
    donar_p.geometry("1300x720")
    donar_p.title("Donación")
    donar_p.iconbitmap('paw-icon.ico')
    donar_p.configure(bg='#0a4369')
    donar_p.state('zoomed')

    textos = [
            "¡Hola! Somos Omeyoacan un albergue de perros, gatos y conejos🐶🐱🐰 que les brinda hogar temporal y cuidado, a los omeyocanitos sin hogar y abandonados."
            " Nos dedicamos a ofrecerles un lugar seguro y amoroso ❤️mientras encontramos un hogar permanente para ellos. Sin embargo, para poder mantenernos y seguir"
            " brindando nuestros servicios, necesitamos tu ayuda🆘. Cualquier donación, por pequeña que sea, nos ayuda a alimentar, vacunar y mantener sanos a nuestros"
            " amigos caninos. Si te gustaría ayudar, dejamos la información aquí abajo. ¡Cualquier ayuda es bienvenida! ¡Gracias!🥰"
            "Si tienes la posibilidad #Échanos 🐾#Amiga dependemos al 💯 de tu ✅apoyo.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
         
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "A pesar de nuestros🐕 llamados 😢no logramos el OBJETIVO y NECESITAMOS DE TU APOYO\n"
            "🙏¿Crees poder ayudarnos para continuar con este proyecto de vida hecho realidad?🙏\n"
            " 🆘Amigos es 🚨#URGENTE!🆘\n"
            "¿Crees poder 🙏#Écharnos 🐾#Amiga 👍"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "🆘NECESITAMOS AYUDA🆘\n"
            "Los Omeyocanitos necesitan de tu apoyo\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Queremos invitarte a hacer una diferencia en la vida de los animalitos🐾❤️ necesitados en nuestro albergue." 
            " Cada día trabajamos arduamente para asegurarnos de que Omeyocanitos tengan un hogar seguro, comida y atención médica🏥🥖🏠." 
            " Pero no podemos hacerlo solos. Necesitamos de la ayuda de personas como tú para mantener nuestro albergue funcionando y poder ayudar a más animalitos." 
            "Cada donación es muy importante y apreciada. ¡Muchas gracias por considerarnos!🙏\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Omeyoacan es financiado por donaciones de personas como tú❤️🥰."
            " Sin su ayuda, no sería posible continuar nuestra labor de salvar y proteger a estos animales que tanto necesitan nuestro apoyo💪." 
            " Cada donación, por pequeña que sea, hace una gran diferencia💞." 
            "Con su ayuda, podemos proporcionar atención médica, comida nutritiva y juguetes para los perros, así como mantener el refugio en óptimas condiciones." 
            "Cada año, ayudamos a cientos de perros a encontrar un hogar amoroso y seguro❤️🏠.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Como Omeyoacan, es nuestra misión es asegurarnos de que cada animalito en nuestro cuidado tenga un hogar permanente y amoroso💞🐾." 
            " Pero para lograrlo, necesitamos de tu ayuda🫵." 
            " Cada donación que recibimos nos ayuda a proporcionar cuidado médico, alimento, agua y un lugar seguro para nuestros amigos peludos." 
            " También nos ayuda a publicitar y promocionar nuestros perros para que encuentren un hogar permanente🏠." 
            " Si te gustaría ayudar, puedes hacer una donación ¡Cualquier ayuda es apreciada y bienvenida! ¡Gracias por pensar en nosotros y en los perros necesitados!🥰"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
          ,  
            "¡Hola! Se hoy el cambio  que quieres mañana. Muchos #omeyocanitos requieren de tu donación." 
            "El refugio requiere de muchos recursos diariamente, para el alimento, cuidados, mantenimiento y muchas cosas más para cambiar la vida de muchos animalitos." 
            "Si esta en tus posibilidades ayudar, en #Omeyocan estariamos muy agradecidos."
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘🆘🆘 AYUDA🆘🆘🆘\n"
            "Necesitamos de tu apoyo, tu donación ayudará a muchos #Omeyocanitos ¿Nos podrias dar una 🐾 #amiga?\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘URGENTE🆘\n"
            "¡TE NECESITAMOS! 🐶🐱🐰\n"
            "¿Nos podrias dar una 🐾 #amiga? CUALQUIER DONATIVO HACE UNA GRAN DIFERENCIA. Todos los #Omeyocanitos te lo agradeceran.\n"
            "🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘\n"
             "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(donar_p,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=donar_p.destroy)
    regresar.place(relx=0.01, rely=0.02)
    
    fotos = tk.Button(donar_p, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_p)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(donar_p, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(donar_p, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(donar_p, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_p = Label(donar_p,text="",font='Helvetica 30 bold', fg='pink', bg='#0a4369')
    lbl_nombre_p.place(relx=0.1, rely=0.02)
    lbl_nombre_p.config(text=valuesp[0])

    lbl_img_p = Label(donar_p,bg = '#0a4369')
    lbl_img_p.place(relx= 0.8, rely=0.05, anchor=N)

def ventanaPublicarP():
    try:
        valuesp
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un perro por favor")
        ventana_perros.deiconify()
        return
    ventana_publicar_p = tk.Toplevel()
    ventana_publicar_p.geometry("1280x720")
    ventana_publicar_p.title("PawSystem")
    ventana_publicar_p.iconbitmap('paw-icon.ico')
    ventana_publicar_p.configure(bg='#0a4369') 
    ventana_publicar_p.state('zoomed')
    ventana_publicar_p.update_idletasks()

    # Crear el botón de regresar
    regresar = tk.Button(ventana_publicar_p, text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=lambda:[ventana_publicar_p.destroy(), ventana_perros.deiconify()])
    regresar.place(relx=0.01, rely=0.02)

    lbl_nombre_p = Label(ventana_publicar_p,text="",font='Helvetica 40 bold', fg='pink', bg='#0a4369')
    lbl_nombre_p.place(relx=0.12, rely=0.05)
    lbl_nombre_p.config(text=valuesp[0])

    # Crear el botón de opciones
    adopcion = tk.Button(ventana_publicar_p, text="Adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaAdopcionP(),ventana.deiconify])
    adopcion.place(relx=0.2, rely=0.85, anchor="center")

    noadop = tk.Button(ventana_publicar_p, text="No adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaNoAdopcionP(),ventana.deiconify])
    noadop.place(relx=0.5, rely=0.85, anchor="center")

    donacion = tk.Button(ventana_publicar_p, text="Donación", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaDonarP(),ventana.deiconify])
    donacion.place(relx=0.8, rely=0.85, anchor="center")

    lbl_img_p = Label(ventana_publicar_p,bg = '#0a4369')
    lbl_img_p.place(relx= 0.5, rely=0.2, anchor=N)

    get_img_perro_pub(lbl_img_p)

def get_img_perro_pub(lbl_img_p):
    try:
        dir_path_p_fotos = os.getcwd() + "/pimg/" + selectedp #Conseguir directorio de la carpeta de imagenes
        images_files = os.listdir(dir_path_p_fotos)[0]
        original_image = Image.open(dir_path_p_fotos + '/' + images_files)
        width_img_p, height_img_p = original_image.size
        aspect_ratio_P = width_img_p/height_img_p
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_p = 400
        max_height_img_p = 400
        new_width_img_p = min(width_img_p, max_width_img_p)
        new_height_img_P = min(height_img_p, max_height_img_p)
        
        if aspect_ratio_P > 1:
            #Imagen más ancha que alta
            new_height_img_P = int(new_width_img_p / aspect_ratio_P)
        else:
            #Imagen más alta que ancha
            new_width_img_p = int(new_height_img_P * aspect_ratio_P)

        new_img = ImageTk.PhotoImage(resized_image.resize((new_width_img_p, new_height_img_P)), Image.Resampling.LANCZOS)
        lbl_img_p.config(image=new_img)
        lbl_img_p.image = new_img   
    except:
        missingImg = (Image.open("noimg.jpg"))
        resized_missingImg = missingImg.resize((300,300), Image.Resampling.LANCZOS)
        new_missingImg = ImageTk.PhotoImage(resized_missingImg)
        lbl_img_p.config(image=new_missingImg)
        lbl_img_p.image = new_missingImg 
        pass

def carpeta_fotos_p():
    try:
        dir_path_p_fotos = os.getcwd() + "/pimg/" + selectedp
        os.startfile(dir_path_p_fotos)
    except:
        messagebox.showwarning("ADVERTENCIA","No hay fotos del perrito registradas")
        return

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

##### Gatos ##### ----------------===============------------------===============------------------================--------------

#Variables Gatos ----------------------------------------------------------------------------------
idG = StringVar()
nombreG = StringVar()
fechanacimientoG = StringVar()
sexoG = StringVar()
razaG = StringVar()
colorG = StringVar()
peloG = StringVar()
tallaG = StringVar()
temperamentoG = StringVar()
esterilizacionG = StringVar()
discapacidadG = StringVar()
adoptableG = StringVar()
fechaesterilizacionG = StringVar()
fechaingresoG = StringVar()

#CRUD Gatos ---------------------------------------------------------------------------------------------
def limpiarCamposG():
    idG.set("")
    nombreG.set("")
    fechanacimientoG.set("")
    sexoG.set("")
    razaG.set("")
    colorG.set("")
    peloG.set("")
    tallaG.set("")
    temperamentoG.set("")
    esterilizacionG.set("")
    discapacidadG.set("")
    adoptableG.set("")
    fechaesterilizacionG.set("")
    fechaingresoG.set("")
    peloOtroG.set("")

def crearG(fMainframe2):
    #Conversiones 
    fechaesterilizacionG = date_fecha_esterilizacionG.get_date()
    fechaingresoG = date_fecha_ingresoG.get_date()
    if(mesNacG=="01" or mesNacG=="02" or mesNacG=="03" or mesNacG=="04" or mesNacG=="05" or mesNacG=="06" or mesNacG=="07" or mesNacG=="08" or mesNacG=="09" or mesNacG=="10" or mesNacG=="11" or mesNacG=="12"):
        fechanacimientoG = anoNacG.get() + "-" + mesNacG
    elif(mesNacG=="N/A"):
        fechanacimientoG = anoNacG.get()
    else:
        fechanacimientoG = mesNacG
    sexoGato = RBsexoG.get()
    if sexoGato == 1:
        sexoG = "Hembra"
    elif sexoGato == 2:
        sexoG = "Macho"
    esterilizacionGato = RBesterilizacionG.get()
    if esterilizacionGato == 1:
        esterilizacionG = "Si"
    elif esterilizacionGato == 2:
        esterilizacionG = "No"
        fechaesterilizacionG = "N/A"
    adoptableGato = RBadoptableG.get()
    if adoptableGato == 1:
        adoptableG = "Si"
    elif adoptableGato == 2:
        adoptableG = "No"
    tallaGato = RBtallaG.get()
    if tallaGato == 1:
        tallaG = "Chico"
    elif tallaGato == 2:
        tallaG = "Mediano"
    elif tallaGato == 3:
        tallaG = "Grande"
    peloGato = RBpeloG.get()
    if peloGato == 1:
        peloG = "Corto"
    elif peloGato == 2:
        peloG = "Largo"
    elif peloGato == 3:
        peloG = "Duro"
    elif peloGato == 4:
        peloG = "Alambre"
    elif peloGato == 5:
        peloG = "Chino"
    elif peloGato == 6:
        peloG = str(peloOtroG.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(nombreG.get())
        print(fechanacimientoG)
        print(sexoG)
        print(razaG.get())
        print(colorG.get())
        print(str(peloG))
        print(tallaG)
        print(temperamentoG.get())
        print(esterilizacionG)
        print(discapacidadG.get())
        print(adoptableG)
        print(str(fechaesterilizacionG))
        print(str(fechaingresoG))
        datosG = nombreG.get(), fechanacimientoG, sexoG, razaG.get(), colorG.get(), peloG, tallaG, temperamentoG.get(), esterilizacionG, discapacidadG.get(), adoptableG, str(fechaesterilizacionG), str(fechaingresoG)
        cursor.execute("INSERT INTO gatos VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosG))
        conexion.commit()

    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro")
        pass
    limpiarCamposG()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_Gatos()
    mostrarCamposG()

def editarG(fMainframe2):
    fechaesterilizacionG = date_fecha_esterilizacionG.get_date()
    fechaingresoG = date_fecha_ingresoG.get_date()
    if(mesNacG=="01" or mesNacG=="02" or mesNacG=="03" or mesNacG=="04" or mesNacG=="05" or mesNacG=="06" or mesNacG=="07" or mesNacG=="08" or mesNacG=="09" or mesNacG=="10" or mesNacG=="11" or mesNacG=="12"):
        fechanacimientoG = anoNacG.get() + "-" + mesNacG
    elif(mesNacG=="N/A"):
        fechanacimientoG = anoNacG.get()
    else:
        fechanacimientoG = mesNacG
    sexoGato = RBsexoG.get()
    if sexoGato == 1:
        sexoG = "Hembra"
    elif sexoGato == 2:
        sexoG = "Macho"
    esterilizacionGato = RBesterilizacionG.get()
    if esterilizacionGato == 1:
        esterilizacionG = "Si"
    elif esterilizacionGato == 2:
        esterilizacionG = "No"
        fechaesterilizacionG = "N/A"
    adoptableGato = RBadoptableG.get()
    if adoptableGato == 1:
        adoptableG = "Si"
    elif adoptableGato == 2:
        adoptableG = "No"
    tallaGato = RBtallaG.get()
    if tallaGato == 1:
        tallaG = "Chico"
    elif tallaGato == 2:
        tallaG = "Mediano"
    elif tallaGato == 3:
        tallaG = "Grande"
    peloGato = RBpeloG.get()
    if peloGato == 1:
        peloG = "Corto"
    elif peloGato == 2:
        peloG = "Largo"
    elif peloGato == 3:
        peloG = "Duro"
    elif peloGato == 4:
        peloG = "Alambre"
    elif peloGato == 5:
        peloG = "Chino"
    elif peloGato == 6:
        peloG = str(peloOtroG.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(nombreG.get())
        print(fechanacimientoG)
        print(sexoG)
        print(razaG.get())
        print(colorG.get())
        print(str(peloG))
        print(tallaG)
        print(temperamentoG.get())
        print(esterilizacionG)
        print(discapacidadG.get())
        print(adoptableG)
        print(str(fechaesterilizacionG))
        print(str(fechaingresoG))
        datosG = nombreG.get(), fechanacimientoG, sexoG, razaG.get(), colorG.get(), peloG, tallaG, temperamentoG.get(), esterilizacionG, discapacidadG.get(), adoptableG, str(fechaesterilizacionG), str(fechaingresoG)
        cursor.execute("UPDATE gatos SET NOMBRE=?, FECHANACIMIENTO=?, SEXO=?, RAZA=?, COLOR=?, PELO=?, TALLA=?, TEMPERAMENTO=?, ESTERILIZACION=?, DISCAPACIDAD=?, ADOPTABLE=?, FECHAESTERILIZACION=?, FECHAINGRESO=? WHERE ID="+selectedG, (datosG))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al editar el registro")
        pass
    limpiarCamposG()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_Gatos()
    mostrarCamposG()

def mostrarCamposG():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosG = treeVG.get_children()
    for elemento in registrosG:
        treeVG.delete(elemento)
    try:
        cursor.execute("SELECT * FROM gatos")
        for row in cursor:
            treeVG.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
    except:
        pass

def seleccionarUsandoClickG(treeVG):
    global selectedG
    global valuesG
    selectedG = None
    valuesG = None
    selectedG = treeVG.focus()
    valuesG = treeVG.item(selectedG,'values')
    print(selectedG)
    print(valuesG)

def borrarRegistroG():
    try:
        valuesG
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un gato por favor")
        ventana_Gatos.deiconify()
        return
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    if messagebox.askyesno(message="¿Realmente desea eliminar el registro? Se borrarán los datos y las imágenes", title="ADVERTENCIA"):
        try:
            try:
                path_2erase_g = os.getcwd() + "\\gimg\\" + selectedG
                shutil.rmtree(path_2erase_g)
            except OSError:
                pass
            cursor.execute("DELETE FROM gatos WHERE ID="+selectedG)
            conexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass
    mostrarCamposG()

def mostrarCamposGa():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosG = treeVGa.get_children()
    for elemento in registrosG:
        treeVGa.delete(elemento)
    try:
        cursor.execute("SELECT * FROM gatosarchivados")
        for row in cursor:
            treeVGa.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
    except:
        pass

def archivarG():
    try:
        valuesG
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un gato por favor")
        ventana_Gatos.deiconify()
        return
    if messagebox.askyesno(message="¿Realmente desea archivar el registro?", title="ADVERTENCIA"):
        global estadoGa
        estadoGa = ""
        ventana_archivar_estadoG()
        ventana_Gatos.wait_window(ventana_archivar_estado_Gatos)
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM gatos WHERE ID="+selectedG)
            conexion.commit()
            print("Archivando gato")
            datosGa = [selectedG]
            for i in range(len(valuesG)):
                datosGa.append(valuesG[i])
            datosGa.append(estadoGa)
            cursor.execute("INSERT INTO gatosarchivados VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosGa))
            conexion.commit()
            mostrarCamposG()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al archivar el gato")
            pass

def desarchivarG():
    if messagebox.askyesno(message="¿Realmente desea desarchivar el registro?", title="ADVERTENCIA"):
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM gatosarchivados WHERE ID="+selectedG)
            conexion.commit()
            print("Desarchivando gato")
            datosGa = [selectedG]
            for i in range(len(valuesG)):
                datosGa.append(valuesG[i])
            datosGa.pop()
            cursor.execute("INSERT INTO gatos VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosGa))
            conexion.commit()
            mostrarCamposGa()
            mostrarCamposG()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al desarchivar el gato")
            pass

def buscarGa():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_Gato_arch = busqueda_entryGa.get()
    #print(lookup_Gato_arch)
    #print(selCbGa)
    for record in treeVGa.get_children():
        treeVGa.delete(record)
    try:
        cursor.execute("SELECT * FROM gatosarchivados WHERE "+selCbGa+" like ?",(lookup_Gato_arch,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposGa()
        else:
            for record in records:
                treeVGa.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposGa()
    ventana_buscar_Gatos_arch.destroy()

def buscarG():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_Gato = busqueda_entryG.get()
    #print(lookup_Gato)
    #print(selCbG)
    for record in treeVG.get_children():
        treeVG.delete(record)
    try:
        cursor.execute("SELECT * FROM gatos WHERE "+selCbG+" like ?",(lookup_Gato,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposG()
        else:
            for record in records:
                treeVG.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposG()
    ventana_buscar_Gatos.destroy()

def clear_entradas_Gatos():
    e_nombreG.delete(0,END)
    e_anoNacG.delete(0,END)
    e_razaG.delete(0,END)
    e_colorG.delete(0,END)
    e_peloG.delete(0,END)
    e_temperamentoG.delete(0,END)
    e_discapacidadG.delete(0,END)

def insertar_editables_Gatos():
    global mesNacG
    #0 nombre
    e_nombreG.insert(0,valuesG[0])
    #1 fecha nacimiento
    if(valuesG[1]=="Cachorro" or valuesG[1]=="Joven" or valuesG[1]=="Adulto" or valuesG[1]=="Viejito"):
        comboG.set(valuesG[1])
        mesNacG = valuesG[1]
    else:
        try:
            split_fng = valuesG[1].split('-')
            e_anoNacG.insert(0,split_fng[0])
            comboG.current(newindex=int(split_fng[1])-1)
            mesNacG = split_fng[1]
        except:
            comboG.current(newindex=12)
            mesNacG = "N/A"
    #2 sexo
    if valuesG[2] == 'Hembra':
        RBsexoG.set(1)
    elif valuesG[2] == 'Macho':
        RBsexoG.set(2)
    #3 raza
    e_razaG.insert(0,valuesG[3])
    #4 color
    e_colorG.insert(0,valuesG[4])
    #5 pelo
    if valuesG[5] == 'Corto':
        RBpeloG.set(1)
    elif valuesG[5] == 'Largo':
        RBpeloG.set(2)
    elif valuesG[5] == 'Duro':
        RBpeloG.set(3)
    elif valuesG[5] == 'Alambre':
        RBpeloG.set(4)
    elif valuesG[5] == 'Chino':
        RBpeloG.set(5)
    else:
        RBpeloG.set(6)
        e_peloG.insert(0,valuesG[5])
    #6 talla
    if valuesG[6] == 'Chico':
        RBtallaG.set(1)
    elif valuesG[6] == 'Mediano':
        RBtallaG.set(2)
    elif valuesG[6] == 'Grande':
        RBtallaG.set(3)
    #7 temperamento
    e_temperamentoG.insert(0,valuesG[7])
    #8 esterilizacion
    if valuesG[8] == 'Si':
        RBesterilizacionG.set(1)
    elif valuesG[8] == 'No':
        RBesterilizacionG.set(2)
    #9 discapacidad
    e_discapacidadG.insert(0,valuesG[9])
    #10 adoptable
    if valuesG[10] == 'Si':
        RBadoptableG.set(1)
    elif valuesG[10] == 'No':
        RBadoptableG.set(2)
    #11 fecha esterilizacion
    if not valuesG[11] == "N/A":
        split_feg = valuesG[11].split('-')
        feg_date = date(int(split_feg[0]),int(split_feg[1]),int(split_feg[2]))
        date_fecha_esterilizacionG.set_date(feg_date)
    #12 fecha ingreso
    split_fig = valuesG[12].split('-')
    fig_date = date(int(split_fig[0]),int(split_fig[1]),int(split_fig[2]))
    date_fecha_ingresoG.set_date(fig_date)

#Ventanas Gatos -------------------------------------------------------------------------------------------
def ventana_archivar_estadoG():
    global ventana_archivar_estado_Gatos
    ventana_archivar_estado_Gatos = tk.Toplevel()
    ventana_archivar_estado_Gatos.geometry("380x230")
    ventana_archivar_estado_Gatos.title("PawSystem Gatos Archivar Motivo")
    ventana_archivar_estado_Gatos.iconbitmap('paw-icon.ico')
    ventana_archivar_estado_Gatos.configure(bg='#0a4369')
    ventana_archivar_estado_Gatos.resizable(False, False)
    lbl_vaeg = Label(ventana_archivar_estado_Gatos, text="Motivo:", bg='#0a4369', fg="white",font='Helvetica 20')
    lbl_vaeg.pack(pady=10)
    RBestadog = IntVar()
    RBestadog.set(1)
    rb_eg1 = tk.Radiobutton(ventana_archivar_estado_Gatos, text="Adoptado", padx = 5, variable=RBestadog, value=1,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
    rb_eg1.pack(pady=10)
    rb_eg2 = tk.Radiobutton(ventana_archivar_estado_Gatos, text="Fallecido", padx = 5, variable=RBestadog, value=2,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
    rb_eg2.pack(pady=10)
    btn_aceptar = Button(ventana_archivar_estado_Gatos, text="Aceptar", width=7, font='Helvetica 13 bold', bg='#33ff6d',command=lambda: aceptar(RBestadog))
    btn_aceptar.pack(pady=10)

    def aceptar(RBestadog):
        global estadoGa
        if RBestadog.get() == 1:
            estadoGa = "Adoptado"
        else:
            estadoGa = "Fallecido"
        ventana_archivar_estado_Gatos.destroy()

def ventana_buscarGa():
    global ventana_buscar_Gatos_arch
    ventana_buscar_Gatos_arch = tk.Toplevel()
    ventana_buscar_Gatos_arch.geometry("700x300")
    ventana_buscar_Gatos_arch.title("PawSystem Gatos Búsqueda")
    ventana_buscar_Gatos_arch.iconbitmap('paw-icon.ico')
    ventana_buscar_Gatos_arch.configure(bg='#0a4369')
    ventana_buscar_Gatos_arch.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_Gatos_arch, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_Gatos_arch,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso","Estado"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_Gatos_arch, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryGa
    busqueda_entryGa = ttk.Entry(ventana_buscar_Gatos_arch,font=('Helvetica 10'))
    busqueda_entryGa.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_Gatos_arch, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBG = Button(ventana_buscar_Gatos_arch, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_Gatos_arch.destroy())
    btn_cancelarBG.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbGa
        selCbGa = None
        selCbGa = combo.get()
        #print(selCbGa)
        match selCbGa:
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del gato")
                selCbGa = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbGa = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbGa = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba la raza del gato")
                selCbGa = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del gato")
                selCbGa = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del gato")
                selCbGa = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del gato")
                selCbGa = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del gato")
                selCbGa = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbGa = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbGa = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbGa = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbGa = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbGa = "FECHAINGRESO"
            case "Estado":
                lbl_busqueda_formato.config(text="escriba Adoptado o Fallecido")
                selCbGa = "STATUS"
        #print(selCbGa)

    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarG = Button(ventana_buscar_Gatos_arch, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarGa)
    btn_buscarG.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def ventana_buscarG():
    global ventana_buscar_Gatos
    ventana_buscar_Gatos = tk.Toplevel()
    ventana_buscar_Gatos.geometry("700x300")
    ventana_buscar_Gatos.title("PawSystem Gatos Búsqueda")
    ventana_buscar_Gatos.iconbitmap('paw-icon.ico')
    ventana_buscar_Gatos.configure(bg='#0a4369')
    ventana_buscar_Gatos.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_Gatos, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_Gatos,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_Gatos, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryG
    busqueda_entryG = ttk.Entry(ventana_buscar_Gatos,font=('Helvetica 10'))
    busqueda_entryG.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_Gatos, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBG = Button(ventana_buscar_Gatos, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_Gatos.destroy())
    btn_cancelarBG.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbG
        selCbG = None
        selCbG = combo.get()
        #print(selCbG)
        match selCbG:
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del gato")
                selCbG = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbG = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbG = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba la raza del gato")
                selCbG = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del gato")
                selCbG = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del gato")
                selCbG = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del gato")
                selCbG = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del gato")
                selCbG = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbG = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbG = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbG = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbG = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbG = "FECHAINGRESO"
        #print(selCbG)

    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarG = Button(ventana_buscar_Gatos, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarG)
    btn_buscarG.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def crear_ventana_Gatos():
    global ventana_Gatos
    ventana_Gatos = tk.Toplevel()
    ventana_Gatos.geometry("1280x860")
    ventana_Gatos.title("PawSystem Gatos")
    ventana_Gatos.iconbitmap('paw-icon.ico')
    ventana_Gatos.configure(bg='#0a4369')
    ventana_Gatos.state('zoomed')

    if not os.path.exists(os.path.join(os.getcwd(), "gimg")):
        os.makedirs(os.path.join(os.getcwd(), "gimg"))

def crear_ventana_Gatos_archivados():
    global ventana_Gatos_archivados
    ventana_Gatos_archivados = tk.Toplevel()
    ventana_Gatos_archivados.geometry("1280x860")
    ventana_Gatos_archivados.title("PawSystem Gatos Archivados")
    ventana_Gatos_archivados.iconbitmap('paw-icon.ico')
    ventana_Gatos_archivados.configure(bg='#0a4369')
    ventana_Gatos_archivados.state('zoomed')

def abrir_ventana_Gatos_archivados():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_Gatos_archivados, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)

    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vga = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vga.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vga_Gatos = tk.Label(fHeader_vga, text="Gatos archivados", font='Helvetica 36 bold', bg='#0a4369', fg='#f7a13e').pack(side='left', padx=10)
    btn_vg_Buscar = tk.Button(fHeader_vga, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarGa).pack(side='right', padx=10)
    btn_vg_LimpiarBusqueda = tk.Button(fHeader_vga, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposGa).pack(side='right', padx=10, pady=(30,0))

    #CONTENTS =============================================================================================================================
    fContents_vGa= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vGa.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso","estado")
    global treeVGa
    treeVGa = ttk.Treeview(fContents_vGa)
    columnas_Gatos(column_names, treeVGa)
    headings_Gatos(treeVGa)
    treeVGa.heading("estado", text="Estado")
    treeVGa.column("estado",width=40, minwidth=10)
    treeVGa.place(relwidth=0.98, relheight=0.96)
    scrollbar_Gatos(fContents_vGa, treeVGa)
    mostrarCamposGa()
    treeVGa.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickG(treeVGa))

    #FOOTER =============================================================================================================================
    fFooter_vGa= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vGa.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vga_Regresar = tk.Button(fFooter_vGa, text="Regresar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_Gatos_archivados.destroy(), ventana_Gatos.deiconify(),seleccionarUsandoClickG(treeVG)]).pack(side='right', padx=10)
    btn_vga_Desarchivar = tk.Button(fFooter_vGa, text="Desarchivar", font='Helvetica 20 bold', bg='#aaf76a', command=lambda:[desarchivarG()]).pack(side='left', padx=10)
    btn_vga_VerFotos = tk.Button(fFooter_vGa, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[crear_ventana_ver_fotos_G(True),ventana_Gatos_archivados.iconify()]).pack(side='left', padx=10)

def abrir_ventana_Gatos():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_Gatos, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)

    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vg = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vg.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vp_Gatos = tk.Label(fHeader_vg, text="Gatos", font='Helvetica 36 bold', bg='#0a4369', fg='#f7a13e').pack(side='left', padx=10)
    btn_vp_Agregar = tk.Button(fHeader_vg, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: agregar_Gatitos(True)).pack(side='right', padx=10)
    btn_vp_Buscar = tk.Button(fHeader_vg, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarG).pack(side='right', padx=10)
    btn_vp_LimpiarBusqueda = tk.Button(fHeader_vg, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposG).pack(side='right', padx=10, pady=(30,0))

    #CONTENTS =============================================================================================================================
    fContents_vG= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vG.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso")
    global treeVG
    treeVG = ttk.Treeview(fContents_vG)
    columnas_Gatos(column_names, treeVG)
    headings_Gatos(treeVG)
    treeVG.place(relwidth=0.98, relheight=0.96)

    mostrarCamposG()
    treeVG.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickG(treeVG))

    scrollbar_Gatos(fContents_vG, treeVG)

    #FOOTER =============================================================================================================================
    fFooter_vG= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vG.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vG_MenuPrincipal = tk.Button(fFooter_vG, text="Menú principal", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_Gatos.destroy(), ventana.deiconify()]).pack(side='right', padx=10)
    btn_vG_VerArchivados = tk.Button(fFooter_vG, text="Ver archivados", font='Helvetica 20 bold', bg='#bd95fc', command=lambda:[crear_ventana_Gatos_archivados(), abrir_ventana_Gatos_archivados(), ventana_Gatos.iconify()]).pack(side='right', padx=10)
    btn_vG_VerFotos = tk.Button(fFooter_vG, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[ventana_Gatos.iconify(),crear_ventana_ver_fotos_G(False)]).pack(side='left', padx=10)
    btn_vG_Publicar = tk.Button(fFooter_vG, text="Publicar", font='Helvetica 20 bold', bg='#f2925e',command=lambda: [ventana_Gatos.iconify(),ventanaPublicarG()]).pack(side='left', padx=10)
    btn_vG_Editar = tk.Button(fFooter_vG, text="Editar", font='Helvetica 20 bold', bg='#34ebc3', command=lambda: agregar_Gatitos(False)).pack(side='left', padx=10)
    btn_vG_Archivar = tk.Button(fFooter_vG, text="Archivar", font='Helvetica 20 bold', bg='pink', command=lambda:archivarG()).pack(side='left', padx=10)
    btn_vG_Borrar = tk.Button(fFooter_vG, text="Borrar", font='Helvetica 20 bold', bg='#f03932',command=lambda: borrarRegistroG()).pack(side='left', padx=10)

    #Ventana para agregar gatitos
    def agregar_Gatitos(add):
        if add == False:
            try:
                valuesG
            except NameError:
                messagebox.showwarning("Advertencia","Seleccione un gato por favor")
                return

        fMainFrame1.destroy()
        fMainFrame2 = tk.Frame(ventana_Gatos, bg='#0a4369')
        fMainFrame2.pack(fill="both", expand=True)

        fagregar_G_header = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_G_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
        lbl_Vagregar_Gatos = tk.Label(fagregar_G_header, text="Gatos", font='Helvetica 30 bold', bg='#0a4369', fg='#f7a13e').pack(side='left', padx=10)

        fagregar_G = tk.Frame(fMainFrame2, bg = '#0a4369')
        fagregar_G.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.77)

        fagregar_G_footer = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_G_footer.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
        btn_Vagregar_cancelar = tk.Button(fagregar_G_footer, text="Cancelar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: [fMainFrame2.destroy(), abrir_ventana_Gatos()]).pack(side='right', padx=10)

        #Labels de categorias
        labels_formulario_Gatos(fagregar_G)

        #Calendarios de las categorias
        calendarios_formulario_Gatos(fagregar_G)

        #Entradas de las categorias
        entradas_formulario_Gatos(fagregar_G)

        #Radio Buttons de las categorias
        radiobtns_formulario_Gatos(fagregar_G)

        def selectionComboG(event):
            global mesNacG
            mesNacG = StringVar()
            mesNacG = comboG.get()
            match mesNacG:
                case "Enero":
                    mesNacG = "01"
                case "Febrero":
                    mesNacG = "02"
                case "Marzo":
                    mesNacG = "03"
                case "Abril":
                    mesNacG = "04"
                case "Mayo":
                    mesNacG = "05"
                case "Junio":
                    mesNacG = "06"
                case "Julio":
                    mesNacG = "07"
                case "Agosto":
                    mesNacG = "08"
                case "Septiembre":
                    mesNacG = "09"
                case "Octubre":
                    mesNacG = "10"
                case "Noviembre":
                    mesNacG = "11"
                case "Diciembre":
                    mesNacG = "12"
                case "No aplica":
                    mesNacG = "N/A"
                case "Cachorro":
                    mesNacG = "Cachorro"
                case "Joven":
                    mesNacG = "Joven"
                case "Adulto":
                    mesNacG = "Adulto"
                case "Viejito":
                    mesNacG = "Viejito"

        global comboG
        comboG = ttk.Combobox(fagregar_G,state="readonly", font='Helvetica 10', values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre","No aplica","Cachorro", "Joven", "Adulto", "Viejito"])
        comboG.grid(row=1,column=1,padx=70,sticky=W)
        comboG.bind("<<ComboboxSelected>>", selectionComboG)
        
        if add == True:
            btn_Vagregar_Agregar = tk.Button(fagregar_G_header, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[crearG(fMainFrame2)]).pack(side='right', padx=10)
        elif add == False:
            btn_Vagregar_Editar = tk.Button(fagregar_G_header, text="Guardar cambios", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[editarG(fMainFrame2)]).pack(side='right', padx=10)
            clear_entradas_Gatos()
            insertar_editables_Gatos()
            

    def radiobtns_formulario_Gatos(fagregar_G):
        global RBsexoG
        RBsexoG = IntVar()
        RBsexoG.set(1)
        rb_sG1 = tk.Radiobutton(fagregar_G, text="Hembra", padx = 5, variable=RBsexoG, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_sG1.grid(row=3,column=1,sticky=W)
        rb_sG2 = tk.Radiobutton(fagregar_G, text="Macho", padx = 5, variable=RBsexoG, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_sG2.grid(row=3,column=1,sticky=W,padx=120)

        global RBesterilizacionG
        RBesterilizacionG = IntVar()
        RBesterilizacionG.set(1)
        rb_eG1 = tk.Radiobutton(fagregar_G, text="Sí", padx = 10, variable=RBesterilizacionG, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_eG1.grid(row=9,column=1,sticky=W)
        rb_eG2 = tk.Radiobutton(fagregar_G, text="No", padx = 10, variable=RBesterilizacionG, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_eG2.grid(row=9,column=1,sticky=W,padx=90)

        global RBadoptableG
        RBadoptableG = IntVar()
        RBadoptableG.set(1)
        rb_aG1 = tk.Radiobutton(fagregar_G, text="Sí", padx = 10, variable=RBadoptableG, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_aG1.grid(row=11,column=1,sticky=W)
        rb_aG2 = tk.Radiobutton(fagregar_G, text="No", padx = 10, variable=RBadoptableG, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_aG2.grid(row=11,column=1,sticky=W,padx=90)

        global RBpeloG
        RBpeloG = IntVar()
        RBpeloG.set(1)
        rb_pG1 = tk.Radiobutton(fagregar_G, text="Corto", padx = 10, variable=RBpeloG, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG1.grid(row=6,column=1,sticky=W)
        rb_pG2 = tk.Radiobutton(fagregar_G, text="Largo", padx = 10, variable=RBpeloG, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG2.grid(row=6,column=1,sticky=W,padx=(90,0))
        rb_pG3 = tk.Radiobutton(fagregar_G, text="Duro", padx = 10, variable=RBpeloG, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG3.grid(row=6,column=1,sticky=W,padx=(182,0))
        rb_pG4 = tk.Radiobutton(fagregar_G, text="Alambre", padx = 10, variable=RBpeloG, value=4,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG4.grid(row=6,column=1,sticky=W,padx=(267,0))
        rb_pG5 = tk.Radiobutton(fagregar_G, text="Chino", padx = 10, variable=RBpeloG, value=5,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG5.grid(row=6,column=1,sticky=W,padx=(377,0))
        rb_pG6 = tk.Radiobutton(fagregar_G, text="Otro:", padx = 10, variable=RBpeloG, value=6,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_pG6.grid(row=6,column=1,sticky=W,padx=(469,0))

        global RBtallaG
        RBtallaG = IntVar()
        RBtallaG.set(1)
        rb_tG1 = tk.Radiobutton(fagregar_G, text="Chico", padx = 5, variable=RBtallaG, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_tG1.grid(row=7,column=1,sticky=W)
        rb_tG2 = tk.Radiobutton(fagregar_G, text="Mediano", padx = 5, variable=RBtallaG, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_tG2.grid(row=7,column=1,sticky=W,padx=100)
        rb_tG3 = tk.Radiobutton(fagregar_G, text="Grande", padx = 5, variable=RBtallaG, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#f7a13e')
        rb_tG3.grid(row=7,column=1,sticky=W,padx=220)

    def entradas_formulario_Gatos(fagregar_G):
        global e_razaG
        e_razaG=tk.Entry(fagregar_G, textvariable=razaG,font=('Helvetica 14'))
        e_razaG.grid(row=4,column=1,sticky=W)
        global e_colorG
        e_colorG=tk.Entry(fagregar_G, textvariable=colorG,font=('Helvetica 14'))
        e_colorG.grid(row=5,column=1,sticky=W)
        global peloOtroG
        peloOtroG = StringVar()
        global e_peloG
        e_peloG=tk.Entry(fagregar_G, textvariable=peloOtroG,font=('Helvetica 14'))
        e_peloG.grid(row=6,column=1,sticky=W,padx=(560,0))
        global e_temperamentoG
        e_temperamentoG=tk.Entry(fagregar_G, textvariable=temperamentoG,font=('Helvetica 14'))
        e_temperamentoG.grid(row=8,column=1,sticky=W)
        global e_nombreG
        e_nombreG=tk.Entry(fagregar_G, textvariable=nombreG,font=('Helvetica 14'))
        e_nombreG.grid(row=0,column=1,sticky=W)
        global e_discapacidadG
        e_discapacidadG=tk.Entry(fagregar_G, textvariable=discapacidadG,font=('Helvetica 14'))
        e_discapacidadG.grid(row=10,column=1,sticky=W)
        global anoNacG
        anoNacG = StringVar()
        global e_anoNacG
        e_anoNacG=tk.Entry(fagregar_G, textvariable=anoNacG,font=('Helvetica 14'))
        e_anoNacG.grid(row=1,column=1,sticky=W,padx=(425,0))

    def calendarios_formulario_Gatos(fagregar_G):
        global date_fecha_esterilizacionG
        date_fecha_esterilizacionG = DateEntry(fagregar_G,selectmode ='day')
        date_fecha_esterilizacionG.grid(row=9,column=1, sticky=W,padx=(510,0))
        global date_fecha_ingresoG
        date_fecha_ingresoG = DateEntry(fagregar_G,selectmode ='day')
        date_fecha_ingresoG.grid(row=2,column=1, sticky=W)

    def labels_formulario_Gatos(fagregar_G):
        lbl_nombre=tk.Label(fagregar_G,text="Nombre",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_nombre.grid(row=0,column=0,sticky=W,padx=20)
        lbl_fecha_nacimiento=tk.Label(fagregar_G,text="Fecha de nacimiento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento.grid(row=1,column=0,sticky=W,padx=(20,45),pady=7)
        lbl_fecha_nacimiento_mes=tk.Label(fagregar_G,text="mes:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_mes.grid(row=1, column=1,sticky=W,pady=7)
        lbl_fecha_nacimiento_year=tk.Label(fagregar_G,text="año:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_year.grid(row=1, column=1,sticky=W,pady=7,padx=(360,0))
        lbl_sexo=tk.Label(fagregar_G,text="Sexo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_sexo.grid(row=3,column=0,sticky=W,padx=20,pady=7)
        lbl_raza=tk.Label(fagregar_G,text="Raza",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_raza.grid(row=4,column=0,sticky=W,padx=20,pady=7)
        lbl_color=tk.Label(fagregar_G,text="Color",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_color.grid(row=5,column=0,sticky=W,padx=20,pady=7)
        lbl_pelo=tk.Label(fagregar_G,text="Pelo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_pelo.grid(row=6,column=0,sticky=W,padx=20,pady=7)
        lbl_talla=tk.Label(fagregar_G,text="Talla",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_talla.grid(row=7,column=0,sticky=W,padx=20,pady=7)
        lbl_temperamento=tk.Label(fagregar_G,text="Temperamento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_temperamento.grid(row=8,column=0,sticky=W,padx=20,pady=7)
        lbl_esterilizacion=tk.Label(fagregar_G,text="Esterilización",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_esterilizacion.grid(row=9,column=0,sticky=W,padx=20,pady=7)
        lbl_discapacidad=tk.Label(fagregar_G,text="Notas",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_discapacidad.grid(row=10,column=0,sticky=W,padx=20,pady=7)
        lbl_adoptable=tk.Label(fagregar_G,text="Adoptable",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_adoptable.grid(row=11,column=0,sticky=W,padx=20,pady=7)
        lbl_fecha_esterilizacion=tk.Label(fagregar_G,text="Fecha de esterilización:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_esterilizacion.grid(row=9,column=1,sticky=W,padx=(267,0),pady=7)
        lbl_fecha_ingreso=tk.Label(fagregar_G,text="Fecha de ingreso",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_ingreso.grid(row=2,column=0,sticky=W,padx=20,pady=7)

def scrollbar_Gatos(fContents_vG, treeVG):
    scrollbar1 = ttk.Scrollbar(fContents_vG, orient=tk.VERTICAL, command=treeVG.yview)
    treeVG.configure(yscroll=scrollbar1.set)
    scrollbar1.place(relx=0.98, relwidth=0.02, relheight=1)

    scrollbar2 = ttk.Scrollbar(fContents_vG, orient=tk.HORIZONTAL, command=treeVG.xview)
    treeVG.configure(xscroll=scrollbar2.set)
    scrollbar2.place(rely=0.96, relwidth=0.98, relheight=0.04)

def headings_Gatos(treeVG):
    treeVG.heading("nombre", text="Nombre")
    treeVG.heading("fechanacimiento", text="Fecha de nacimiento")
    treeVG.heading("sexo", text="Sexo")
    treeVG.heading("raza", text="Raza")
    treeVG.heading("color", text="Color")
    treeVG.heading("pelo", text="Pelo")
    treeVG.heading("talla", text="Talla")
    treeVG.heading("temperamento", text="Temperamento")
    treeVG.heading("esterilizacion", text="Esterilización")
    treeVG.heading("discapacidad", text="Notas")
    treeVG.heading("adoptable", text="Adoptable")
    treeVG.heading("fechaesterilizacion", text="Fecha de esterilización")
    treeVG.heading("fechaingreso", text="Fecha de ingreso")

def columnas_Gatos(column_names, treeVG):
    treeVG.configure(columns=column_names, show='headings')
    treeVG.column("#0",width=10, minwidth=10)
    treeVG.column("nombre",width=40, minwidth=10)
    treeVG.column("fechanacimiento",width=40, minwidth=10)
    treeVG.column("sexo",width=10, minwidth=10)
    treeVG.column("raza",width=40, minwidth=10)
    treeVG.column("color",width=15, minwidth=10)
    treeVG.column("pelo",width=40, minwidth=10)
    treeVG.column("talla",width=40, minwidth=10)
    treeVG.column("temperamento",width=40, minwidth=10)
    treeVG.column("esterilizacion",width=40, minwidth=10)
    treeVG.column("discapacidad",width=40, minwidth=10)
    treeVG.column("adoptable",width=40, minwidth=10)
    treeVG.column("fechaesterilizacion",width=40, minwidth=10)
    treeVG.column("fechaingreso",width=40, minwidth=10)

#Ventanas Fotos Gatos ------------------------------------------------------------------------------------
def crear_ventana_ver_fotos_G(archivado):
    try:
        valuesG
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un gato por favor")
        ventana_Gatos.deiconify()
        return
    global ver_fotos_ven_G
    ver_fotos_ven_G = tk.Toplevel(ventana)
    ver_fotos_ven_G.geometry("1280x720")
    ver_fotos_ven_G.title("PawSystem Gatos")
    ver_fotos_ven_G.iconbitmap('paw-icon.ico')
    ver_fotos_ven_G.configure(bg='#0a4369')
    ver_fotos_ven_G.state('zoomed')
    ver_fotos_ven_G.update_idletasks()

    abrir_ventana_ver_fotos_G(archivado)

def abrir_ventana_ver_fotos_G(archivado):
    fMainFrame3 = tk.Frame(ver_fotos_ven_G, bg='#0a4369')
    fMainFrame3.pack(fill="both", expand=True)
    fVerfotos_G_header = tk.Frame(fMainFrame3, bg='#0a4369')
    fVerfotos_G_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    fverFotos_G_footer = tk.Frame(fMainFrame3, bg = '#0a4369')
    fverFotos_G_footer.place(relx=0.01, rely=0.81, relwidth=0.98, relheight=0.15)

    btn_regresar_G = tk.Button(fVerfotos_G_header, text = "Regresar", font='Helvetica 18 bold', bg='#33ff6d')
    btn_regresar_G.pack(side = 'left')

    lbl_vfg_n_Gatos = Label(fVerfotos_G_header, text="", font='Helvetica 30 bold', bg='#0a4369', fg='#f7a13e')
    lbl_vfg_n_Gatos.pack(side='left', padx=50)
    lbl_vfg_n_Gatos.config(text=valuesG[0])
    lbl_vfg_fi_Gatos = Label(fVerfotos_G_header, text = "",font='Helvetica 15 bold', bg='#0a4369', fg='#f7a13e')
    lbl_vfg_fi_Gatos.pack(side = 'right',padx=5)
    lbl_vfg_fi_Gatos.config(text = valuesG[12])
    lbl_vfg_fit_Gatos = Label(fVerfotos_G_header, text = "Fecha de ingreso: ",font='Helvetica 15 bold', bg='#0a4369', fg='#f7a13e')
    lbl_vfg_fit_Gatos.pack(side = 'right',padx=5)

    btn_agregarfoto_G = tk.Button(fverFotos_G_footer, text = "Agregar Foto", font='Helvetica 18 bold', bg='#33ff6d')
    btn_agregarfoto_G.pack(side= 'left', padx=45)
    btn_eliminarfotos_G = tk.Button(fverFotos_G_footer, text = "Eliminar foto", font='Helvetica 18 bold', bg='#db5142')
    btn_eliminarfotos_G.pack(side= 'right', padx=45)

    canvas_ver_foto_G = tk.Canvas(fverFotos_G_footer,height =70,width =500, bg = '#C1CDCD')
    canvas_ver_foto_G.pack(side = tk.BOTTOM,fill = tk.X)

    canvas_ver_foto_G.bind('<Configure>', lambda e:canvas_ver_foto_G.bbox('all'))
    slider = tk.Frame(canvas_ver_foto_G)
    canvas_ver_foto_G.create_window((0,0),window = slider, anchor = tk.NW)
    progbarFG = ttk.Progressbar(fVerfotos_G_header, orient='horizontal',mode='determinate',length=500)
    progbarFG.update_idletasks()
    progbarFG.pack(side=TOP,expand=YES)

    threading.Thread(target = lambda:contenido_ver_fotos_G(canvas_ver_foto_G,fverFotos_G_footer,fMainFrame3,archivado,slider,btn_agregarfoto_G,btn_regresar_G,btn_eliminarfotos_G,progbarFG)).start()

def contenido_ver_fotos_G(canvas_ver_foto_G,fverFotos_G_footer,fMainFrame3,archivado,slider,btn_agregarfoto_G,btn_regresar_G,btn_eliminarfotos_G,progbarFG):    
    #Frames de contenidos para fotos
    fVerFotos_G_contents = tk.Frame(fMainFrame3, bg = '#0a4369')
    fVerFotos_G_contents.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.71)

    #Botones ver fotos, regresar y eliminar COMMAND
    if archivado == False:
        btn_regresar_G.config(command = lambda: [ver_fotos_ven_G.destroy(),ventana_Gatos.deiconify()])
        btn_agregarfoto_G.config(command = lambda: [agregar_fotos_G(ver_fotos_ven_G),abrir_ventana_ver_fotos_G(False)])
    else:
        btn_regresar_G.config(command = lambda: [ver_fotos_ven_G.destroy(),ventana_Gatos_archivados.deiconify()])
        btn_agregarfoto_G.config(command = lambda: [agregar_fotos_G(ver_fotos_ven_G),abrir_ventana_ver_fotos_G(True)])
    btn_eliminarfotos_G.config(command = lambda:[eliminar_foto_G(dir_path_G_fotos, aux_index)])

    #Lbl desplegar imagenes
    lbl_desplegar_img_G = tk.Label(fVerFotos_G_contents,bg = '#0a4369')
    lbl_desplegar_img_G.pack(anchor = tk.CENTER)

    images_list_G = []
    images_vars_G = []

    global dir_path_G_fotos
    images_files = None
    dir_path_G_fotos = os.getcwd() + "/gimg/" + selectedG
    if not os.path.exists(dir_path_G_fotos):
        os.makedirs(dir_path_G_fotos)
    images_files = os.listdir(dir_path_G_fotos)      
        

    for r in range(0, len(images_files)):
        original_image = Image.open(dir_path_G_fotos + '/' + images_files[r])
        width_img_G, height_img_G = original_image.size
        aspect_ratio_G = width_img_G/height_img_G
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_G = 500
        max_height_img_G = 500
        new_width_img_G = min(width_img_G, max_width_img_G)
        new_height_img_G = min(height_img_G, max_height_img_G)

        if aspect_ratio_G > 1:
            #Imagen más ancha que alta
            new_height_img_G = int(new_width_img_G / aspect_ratio_G)
        else:
            #Imagen más alta que ancha
            new_width_img_G = int(new_height_img_G * aspect_ratio_G)

        images_list_G.append([
                ImageTk.PhotoImage(original_image.resize((int(new_width_img_G/7),int(new_height_img_G/7) ), Image.Resampling.LANCZOS)),
                ImageTk.PhotoImage(resized_image.resize((new_width_img_G, new_height_img_G)), Image.Resampling.LANCZOS)
                             ])   
        images_vars_G.append(f'img_{r}')


        progbarFG['value'] += (100/len(images_files))
    progbarFG.pack_forget()


    def desplegar_img_G(index_G):
        global aux_index
        aux_index = index_G
        lbl_desplegar_img_G.config(image = images_list_G[index_G][1])
        lbl_desplegar_img_G.pack(side='left', anchor='center', expand=True)

    for n in range(len(images_vars_G)):
        globals()[images_vars_G[n]] = tk.Button(slider,image=images_list_G[n][0], bd = 0, command = lambda n = n:desplegar_img_G(n))
        globals()[images_vars_G[n]].pack(side =tk.LEFT)

    canvas_ver_foto_G.configure(scrollregion=canvas_ver_foto_G.bbox('all'))
    x_scroll_bar = tk.Scrollbar(fverFotos_G_footer, orient='horizontal')
    x_scroll_bar.pack(side = tk.BOTTOM,fill = tk.X)
    x_scroll_bar.configure(command=canvas_ver_foto_G.xview)
    canvas_ver_foto_G.configure(xscrollcommand=x_scroll_bar.set)
    slider.bind('<Configure>', lambda event: canvas_ver_foto_G.configure(scrollregion=canvas_ver_foto_G.bbox('all')))

    def eliminar_foto_G(dir_path_G_fotos, aux_index): 
        respuesta = messagebox.askyesno("Eliminar imagen","¿Seguro quieres eliminar la imagen?")
        if respuesta ==1:
            res = []
            for path in os.listdir(dir_path_G_fotos):
                # checar si el directorio es un archivo
                if os.path.isfile(os.path.join(dir_path_G_fotos, path)):
                    res.append(path) 
            deletepath = dir_path_G_fotos +"/" +str(res[aux_index])  
            os.remove(deletepath)
            fMainFrame3.destroy()
            if archivado == False:
                abrir_ventana_ver_fotos_G(False)
            else:
                abrir_ventana_ver_fotos_G(True)
        else:
            return 0

    def agregar_fotos_G(ventana):
        current_path_image = filedialog.askopenfilename(initialdir='Imagenes')   
        ruta_G,n_archivo_G = os.path.split(current_path_image)    
        new_path_image = dir_path_G_fotos + "/" + str(n_archivo_G)
        shutil.copyfile(current_path_image, new_path_image)
        fMainFrame3.destroy()

#Textos Gatos ---------------------------------------------------------------------------------------------
def ventanaAdopcionG():
    ventana.withdraw()
    ventana_adop_G = tk.Toplevel()
    ventana_adop_G.geometry("1300x720")
    ventana_adop_G.title("Adopción")
    ventana_adop_G.iconbitmap('paw-icon.ico')
    ventana_adop_G.configure(bg='#0a4369')
    ventana_adop_G.state('zoomed')
    ventana_adop_G.update_idletasks()

    textos = [
        "SU 🎞 #HISTORIA CONTINÚA, en #ADOPCIÒN 🐾Un #rescate que aún sigue vigente"
        " 🇲🇽🐾\nNOMBRE: "+valuesG[0]+"\nNACIÓ: "+valuesG[1]+ "\nTALLA: "+valuesG[6]+"\nSEXO: "
        +valuesG[2]+" #"+valuesG[8]+"estaesterilizado\nTEMPERAMENTO: "+valuesG[7]+"#adopta"
        " #adopta #adoptanocompres #amigoperruno ❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀"
        " #APADRINAMIENTOVIRTUAL #UnperritogatitoabandonadoenunHOGAR\nPara más información comunícate a:"
        " adopcionesvirtualesomeyocan@yahoo.com.mx #amigoperruno #amigogatuno #perritos #gatitos"
        " #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Conoce a "+valuesG[0]+ "! SU #HISTORIA CONTINUA en #ADOPCION. Nació "+valuesG[1]+" y es un #rescate"
        " que aún sigue vigente, TÚ puedes cambiar su vida\nTALLA: "+valuesG[6]+"\nSEXO:"
        +valuesG[2]+"\n#"+valuesG[8]+"estaesterilizado\nTEMPERAMENTO: "+valuesG[7]+" Con tu ayuda nuestro"
        " #Omeyocanito puede tener una vida mejor y compartir su felicidad y alegría con más personas"
        "\n#adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL"
        " #UnperritogatitoabandonadoenunHOGAR Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx" 
        "\n#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesG[0]+"!🐾 sigue aquí con nosotros. El es un #Omeyocanito "+valuesG[7]+". Estaríamos muy" 
        " felices de encontrarle una familia que le dé mucho amor.\nPara más información comunícate a:" 
        " adopcionesvirtualesomeyocan@yahoo.com.m #amigoperruno #amigogatuno #perritos"
        " #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesG[0]+", lleva un rato con nosotros, pero ya quiere conocer a las personas que serán"
        " su #familia ❤️. Es de talla"+valuesG[6]+" ¡ya es tiempo de darle la vida que merece!" 
        " Si no puedes adoptar puedes #apadrinar a"+valuesG[0]+" o #compartir para que encuentre un hogar"
        " 🐾❤️.\n#ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesG[0]+" merece una oportunidad!. Está con nosotros desde "+valuesG[12]+". Ayúdanos a encontrarle" 
        " una familia. Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx #adopta "
        "#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        ""+valuesG[0]+" 🐱 es de talla "+valuesG[6]+". Es"+valuesG[7]+", y "+valuesG[2]+""  
        "Si quieres adoptar a "+valuesG[0]+" y que formen una hermosa familia juntos❤️🐾, contáctanos."
        "#ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        "adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        "🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        "\nPara más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Me llamo "+valuesG[0]+" estoy buscando una familia que me de mucho cariño🥰." 
        " Soy "+valuesG[7]+" y de tamaño "+valuesG[6]+". Ayúdame a encontrar la familia que tanto he esperado." 
        " #ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #-------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesG[0]+" ya quiere pertenece a una familia, es de talla "+valuesG[6]+"" 
        " Es "+valuesG[7]+". Estamos seguras de que le dará mucho a amor a la familia a la que vaya a pertenecer." 
        " Es muy amigable con otros perros y niños," 
        " pero necesita una familia que pueda brindarle la atención y el tiempo que necesita para mantenerse feliz y saludable."
        " #ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Soy "+valuesG[0]+" y soy de talla "+valuesG[6]+"." 
        " Soy "+valuesG[7]+" Necesito una familia que tenga tiempo y amor para dedicar a un perro activo como yo."
        " Si estás interesado en adoptarme, por favor asegúrate de que tienes el tiempo y los recursos necesarios para cuidarme adecuadamente." 
        " Estoy dispuesto a aprender y estoy ansioso por encontrar un hogar lleno de amor. ¡Gracias por considerarme!",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Hola nosotros somos #Omeyocan🖐🏼! Necesitamos tu ayuda🥹, "+valuesG[0]+" 🐱 esta buscando una familia con quien compartir su felicidad y cariño ❤️"
        "\nNACIÓ: "+valuesG[1]+"\n"
        "TALLA: "+valuesG[6]+"\n"
        "SEXO: "+valuesG[2]+"\n"
        "#Esterilización "+valuesG[8]+"\n"
        "TEMPERAMENTO: "+valuesG[7]+"\n"
        " #ADOPTA #adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_adop_G,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_adop_G.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(ventana_adop_G, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_G)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_adop_G, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_adop_G, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_adop_G, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_G = Label(ventana_adop_G,text="",font='Helvetica 30 bold', fg='#f7a13e', bg='#0a4369')
    lbl_nombre_G.place(relx=0.1, rely=0.02)
    lbl_nombre_G.config(text=valuesG[0])

    lbl_img_G = Label(ventana_adop_G,bg = '#0a4369')
    lbl_img_G.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_Gato_pub(lbl_img_G)).start()

def ventanaNoAdopcionG():
    ventana.withdraw()
    ventana_no_adopt_G = tk.Toplevel()
    ventana_no_adopt_G.geometry("1300x720")
    ventana_no_adopt_G.title("No adopción")
    ventana_no_adopt_G.iconbitmap('paw-icon.ico')
    ventana_no_adopt_G.configure(bg='#0a4369')
    ventana_no_adopt_G.state('zoomed')
    ventana_no_adopt_G.update_idletasks()

    textos = [
        "¡Hola! Soy "+valuesG[0]+" estoy buscando apoyo para poder tener una vida digna🐾." 
        " No soy adoptable, pero puedes apadrinarme de manera virtual 🐱 en adopcionesvirtualesomeyocan@yahoo.com.mx." 
        " No todos podemos ser adoptables por distintas razones, pero siempre existen más maneras de apoyar. ❤️"
        " #APADRINA #noadoptable #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Existen muchos Omeyocanitos que no tienen la posibilidad de ser adoptados😥 ya que algunos se encuentran" 
        " en rehabilitación física y/o emocional, pero puedes apadrinar.\n" 
        ""+valuesG[0]+"🐾💞 no tiene la posibilidad y busca TU ayuda para poder tener la vida que merece." 
        " adopcionesvirtualesomeyocan@yahoo.com.mx #APADRINA #noadoptable #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesG[0]+" te necesita! Aunque 🚫NO es ADOPTABLE🚫 podrías hacer que tenga una mejor vida y pronta rehabilitación ❤‍🩹 ." 
        " En #Omeyocan hay #omeyocanitos que requieren de atención especial y rehabilitación física o emocional, sin embargo," 
        " puedes #apadrinar y contribuir y hacer el cambio 💓. Esta con nosotros desde "+valuesG[12]+". \n"
        "NACIÓ: "+valuesG[1]+"\n"
        "TALLA: "+valuesG[6]+"\n"
        "SEXO: "+valuesG[2]+"\n"
        "#Esterilizado\n"
        " TEMPERAMENTO: "+valuesG[7]+""
        " 🧚🏻‍♀ APADRINAMIENTO VIRTUAL, comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx para mas informarción."
        " \n#APADRINA #UnperritogatitoabandonadoenunHOGAR",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Haz la diferencia en la vida de "+valuesG[0]+"! Apadrina a uno de los adorables gatitos de Omeyocan, un refugio dedicado a cuidar y proteger a los animales." 
        " Tu apadrinamiento ayudará a cubrir los costos de alimentación, atención médica y cuidado diario de estos gatitos mientras esperan encontrar un hogar amoroso y permanente." 
        " ¡Únete a nosotros en nuestra misión de brindar una vida mejor a estos gatitos necesitados!"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "🚫"+valuesG[0]+" NO ES ADOPTABLE🚫\n"
        " Lleva con nosotros desde "+valuesG[12]+", necesita de tu apoyo para salir adelante,"
        " aunque 🚫NO ES ADOPTABLE🚫 puedes #Apadrinar para ayudar a su cuidado.\n"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_no_adopt_G,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_no_adopt_G.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(ventana_no_adopt_G, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_G)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_no_adopt_G, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_no_adopt_G, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_no_adopt_G, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_G = Label(ventana_no_adopt_G,text="",font='Helvetica 30 bold', fg='#f7a13e', bg='#0a4369')
    lbl_nombre_G.place(relx=0.1, rely=0.02)
    lbl_nombre_G.config(text=valuesG[0])

    lbl_img_G = Label(ventana_no_adopt_G,bg = '#0a4369')
    lbl_img_G.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_Gato_pub(lbl_img_G)).start()

def ventanaDonarG():
    ventana.withdraw()
    donar_G = tk.Toplevel()
    donar_G.geometry("1300x720")
    donar_G.title("Donación")
    donar_G.iconbitmap('paw-icon.ico')
    donar_G.configure(bg='#0a4369')
    donar_G.state('zoomed')

    textos = [
            "¡Hola! Somos Omeyoacan un albergue de perros, gatos y conejos🐶🐱🐰 que les brinda hogar temporal y cuidado, a los omeyocanitos sin hogar y abandonados."
            " Nos dedicamos a ofrecerles un lugar seguro y amoroso ❤️mientras encontramos un hogar permanente para ellos. Sin embargo, para poder mantenernos y seguir"
            " brindando nuestros servicios, necesitamos tu ayuda🆘. Cualquier donación, por pequeña que sea, nos ayuda a alimentar, vacunar y mantener sanos a nuestros"
            " amigos caninos. Si te gustaría ayudar, dejamos la información aquí abajo. ¡Cualquier ayuda es bienvenida! ¡Gracias!🥰"
            "Si tienes la posibilidad #Échanos 🐾#Amiga dependemos al 💯 de tu ✅apoyo.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,

            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "A pesar de nuestros🐕 llamados 😢no logramos el OBJETIVO y NECESITAMOS DE TU APOYO\n"
            "🙏¿Crees poder ayudarnos para continuar con este proyecto de vida hecho realidad?🙏\n"
            " 🆘Amigos es 🚨#URGENTE!🆘\n"
            "¿Crees poder 🙏#Écharnos 🐾#Amiga 👍"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "🆘NECESITAMOS AYUDA🆘\n"
            "Los Omeyocanitos necesitan de tu apoyo\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Queremos invitarte a hacer una diferencia en la vida de los animalitos🐾❤️ necesitados en nuestro albergue." 
            " Cada día trabajamos arduamente para asegurarnos de que Omeyocanitos tengan un hogar seguro, comida y atención médica🏥🥖🏠." 
            " Pero no podemos hacerlo solos. Necesitamos de la ayuda de personas como tú para mantener nuestro albergue funcionando y poder ayudar a más animalitos." 
            "Cada donación es muy importante y apreciada. ¡Muchas gracias por considerarnos!🙏\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Omeyoacan es financiado por donaciones de personas como tú❤️🥰."
            " Sin su ayuda, no sería posible continuar nuestra labor de salvar y proteger a estos animales que tanto necesitan nuestro apoyo💪." 
            " Cada donación, por pequeña que sea, hace una gran diferencia💞." 
            "Con su ayuda, podemos proporcionar atención médica, comida nutritiva y juguetes para los perros, así como mantener el refugio en óptimas condiciones." 
            "Cada año, ayudamos a cientos de perros a encontrar un hogar amoroso y seguro❤️🏠.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Como Omeyoacan, es nuestra misión es asegurarnos de que cada animalito en nuestro cuidado tenga un hogar permanente y amoroso💞🐾." 
            " Pero para lograrlo, necesitamos de tu ayuda🫵." 
            " Cada donación que recibimos nos ayuda a proporcionar cuidado médico, alimento, agua y un lugar seguro para nuestros amigos peludos." 
            " También nos ayuda a publicitar y promocionar nuestros perros para que encuentren un hogar permanente🏠." 
            " Si te gustaría ayudar, puedes hacer una donación ¡Cualquier ayuda es apreciada y bienvenida! ¡Gracias por pensar en nosotros y en los perros necesitados!🥰"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
          ,  
            "¡Hola! Se hoy el cambio  que quieres mañana. Muchos #omeyocanitos requieren de tu donación." 
            "El refugio requiere de muchos recursos diariamente, para el alimento, cuidados, mantenimiento y muchas cosas más para cambiar la vida de muchos animalitos." 
            "Si esta en tus posibilidades ayudar, en #Omeyocan estariamos muy agradecidos."
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘🆘🆘 AYUDA🆘🆘🆘\n"
            "Necesitamos de tu apoyo, tu donación ayudará a muchos #Omeyocanitos ¿Nos podrias dar una 🐾 #amiga?\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘URGENTE🆘\n"
            "¡TE NECESITAMOS! 🐶🐱🐰\n"
            "¿Nos podrias dar una 🐾 #amiga? CUALQUIER DONATIVO HACE UNA GRAN DIFERENCIA. Todos los #Omeyocanitos te lo agradeceran.\n"
            "🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘\n"
             "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(donar_G,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=donar_G.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(donar_G, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_G)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(donar_G, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(donar_G, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(donar_G, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_G = Label(donar_G,text="",font='Helvetica 30 bold', fg='#f7a13e', bg='#0a4369')
    lbl_nombre_G.place(relx=0.1, rely=0.02)
    lbl_nombre_G.config(text=valuesG[0])

    lbl_img_G = Label(donar_G,bg = '#0a4369')
    lbl_img_G.place(relx= 0.8, rely=0.05, anchor=N)

def ventanaPublicarG():
    try:
        valuesG
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un gato por favor")
        ventana_Gatos.deiconify()
        return
    ventana_publicar_G = tk.Toplevel()
    ventana_publicar_G.geometry("1280x720")
    ventana_publicar_G.title("PawSystem Gatos")
    ventana_publicar_G.iconbitmap('paw-icon.ico')
    ventana_publicar_G.configure(bg='#0a4369') 
    ventana_publicar_G.state('zoomed')
    ventana_publicar_G.update_idletasks()

    # Crear el botón de regresar
    regresar = tk.Button(ventana_publicar_G, text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=lambda:[ventana_publicar_G.destroy(), ventana_Gatos.deiconify()])
    regresar.place(relx=0.01, rely=0.02)

    lbl_nombre_G = Label(ventana_publicar_G,text="",font='Helvetica 40 bold', fg='#f7a13e', bg='#0a4369')
    lbl_nombre_G.place(relx=0.12, rely=0.05)
    lbl_nombre_G.config(text=valuesG[0])

    # Crear el botón de opciones
    adopcion = tk.Button(ventana_publicar_G, text="Adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaAdopcionG(),ventana.deiconify])
    adopcion.place(relx=0.2, rely=0.85, anchor="center")

    noadop = tk.Button(ventana_publicar_G, text="No adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaNoAdopcionG(),ventana.deiconify])
    noadop.place(relx=0.5, rely=0.85, anchor="center")

    donacion = tk.Button(ventana_publicar_G, text="Donación", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaDonarG(),ventana.deiconify])
    donacion.place(relx=0.8, rely=0.85, anchor="center")

    lbl_img_G = Label(ventana_publicar_G,bg = '#0a4369')
    lbl_img_G.place(relx= 0.5, rely=0.2, anchor=N)

    get_img_Gato_pub(lbl_img_G)

def get_img_Gato_pub(lbl_img_G):
    try:
        dir_path_G_fotos = os.getcwd() + "/gimg/" + selectedG #Conseguir directorio de la carpeta de imagenes
        images_files = os.listdir(dir_path_G_fotos)[0]
        original_image = Image.open(dir_path_G_fotos + '/' + images_files)
        width_img_G, height_img_G = original_image.size
        aspect_ratio_G = width_img_G/height_img_G
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_G = 400
        max_height_img_G = 400
        new_width_img_G = min(width_img_G, max_width_img_G)
        new_height_img_G = min(height_img_G, max_height_img_G)

        if aspect_ratio_G > 1:
            #Imagen más ancha que alta
            new_height_img_G = int(new_width_img_G / aspect_ratio_G)
        else:
            #Imagen más alta que ancha
            new_width_img_G = int(new_height_img_G * aspect_ratio_G)

        new_img = ImageTk.PhotoImage(resized_image.resize((new_width_img_G, new_height_img_G)), Image.Resampling.LANCZOS)
        lbl_img_G.config(image=new_img)
        lbl_img_G.image = new_img   
    except:
        missingImg = (Image.open("noimg.jpg"))
        resized_missingImg = missingImg.resize((300,300), Image.Resampling.LANCZOS)
        new_missingImg = ImageTk.PhotoImage(resized_missingImg)
        lbl_img_G.config(image=new_missingImg)
        lbl_img_G.image = new_missingImg 
        pass

def carpeta_fotos_G():
    try:
        dir_path_G_fotos = os.getcwd() + "/gimg/" + selectedG
        os.startfile(dir_path_G_fotos)
    except:
        messagebox.showwarning("ADVERTENCIA","No hay fotos del gatito registradas")
        return

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

##### OTROS ##### ----------------===============------------------===============------------------================--------------
#Variables Otros ----------------------------------------------------------------------------------
idO = StringVar()
nombreO = StringVar()
fechanacimientoO = StringVar()
sexoO = StringVar()
razaO = StringVar()
colorO = StringVar()
peloO = StringVar()
tallaO = StringVar()
temperamentoO = StringVar()
esterilizacionO = StringVar()
discapacidadO = StringVar()
adoptableO = StringVar()
fechaesterilizacionO = StringVar()
fechaingresoO = StringVar()
tipoO = StringVar()

#CRUD Otros ---------------------------------------------------------------------------------------------
def limpiarCamposO():
    idO.set("")
    nombreO.set("")
    fechanacimientoO.set("")
    sexoO.set("")
    razaO.set("")
    colorO.set("")
    peloO.set("")
    tallaO.set("")
    temperamentoO.set("")
    esterilizacionO.set("")
    discapacidadO.set("")
    adoptableO.set("")
    fechaesterilizacionO.set("")
    fechaingresoO.set("")
    peloOtroO.set("")

def crearO(fMainframe2):
    #Conversiones 
    fechaesterilizacionO = date_fecha_esterilizacionO.get_date()
    fechaingresoO = date_fecha_ingresoO.get_date()
    if(mesNacO=="01" or mesNacO=="02" or mesNacO=="03" or mesNacO=="04" or mesNacO=="05" or mesNacO=="06" or mesNacO=="07" or mesNacO=="08" or mesNacO=="09" or mesNacO=="10" or mesNacO=="11" or mesNacO=="12"):
        fechanacimientoO = anoNacO.get() + "-" + mesNacO
    elif(mesNacO=="N/A"):
        fechanacimientoO = anoNacO.get()
    else:
        fechanacimientoO = mesNacO
    sexoOtro = RBsexoO.get()
    if sexoOtro == 1:
        sexoO = "Hembra"
    elif sexoOtro == 2:
        sexoO = "Macho"
    esterilizacionOtro = RBesterilizacionO.get()
    if esterilizacionOtro == 1:
        esterilizacionO = "Si"
    elif esterilizacionOtro == 2:
        esterilizacionO = "No"
        fechaesterilizacionO = "N/A"
    adoptableOtro = RBadoptableO.get()
    if adoptableOtro == 1:
        adoptableO = "Si"
    elif adoptableOtro == 2:
        adoptableO = "No"
    tallaOtro = RBtallaO.get()
    if tallaOtro == 1:
        tallaO = "Chico"
    elif tallaOtro == 2:
        tallaO = "Mediano"
    elif tallaOtro == 3:
        tallaO = "Grande"
    peloOtro = RBpeloO.get()
    if peloOtro == 1:
        peloO = "Corto"
    elif peloOtro == 2:
        peloO = "Largo"
    elif peloOtro == 3:
        peloO = "Duro"
    elif peloOtro == 4:
        peloO = "Alambre"
    elif peloOtro == 5:
        peloO = "Chino"
    elif peloOtro == 6:
        peloO = str(peloOtroO.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(tipoO.get())
        print(nombreO.get())
        print(fechanacimientoO)
        print(sexoO)
        print(razaO.get())
        print(colorO.get())
        print(str(peloO))
        print(tallaO)
        print(temperamentoO.get())
        print(esterilizacionO)
        print(discapacidadO.get())
        print(adoptableO)
        print(str(fechaesterilizacionO))
        print(str(fechaingresoO))
        (datosO) = tipoO.get(), nombreO.get(), fechanacimientoO, sexoO, razaO.get(), colorO.get(), peloO, tallaO, temperamentoO.get(), esterilizacionO, discapacidadO.get(), adoptableO, str(fechaesterilizacionO), str(fechaingresoO)
        cursor.execute("INSERT INTO otros VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosO))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro")
        pass
    limpiarCamposO()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_Otros()
    mostrarCamposO()

def editarO(fMainframe2):
    fechaesterilizacionO = date_fecha_esterilizacionO.get_date()
    fechaingresoO = date_fecha_ingresoO.get_date()
    if(mesNacO=="01" or mesNacO=="02" or mesNacO=="03" or mesNacO=="04" or mesNacO=="05" or mesNacO=="06" or mesNacO=="07" or mesNacO=="08" or mesNacO=="09" or mesNacO=="10" or mesNacO=="11" or mesNacO=="12"):
        fechanacimientoO = anoNacO.get() + "-" + mesNacO
    elif(mesNacO=="N/A"):
        fechanacimientoO = anoNacO.get()
    else:
        fechanacimientoO = mesNacO
    sexoOtro = RBsexoO.get()
    if sexoOtro == 1:
        sexoO = "Hembra"
    elif sexoOtro == 2:
        sexoO = "Macho"
    esterilizacionOtro = RBesterilizacionO.get()
    if esterilizacionOtro == 1:
        esterilizacionO = "Si"
    elif esterilizacionOtro == 2:
        esterilizacionO = "No"
        fechaesterilizacionO = "N/A"
    adoptableOtro = RBadoptableO.get()
    if adoptableOtro == 1:
        adoptableO = "Si"
    elif adoptableOtro == 2:
        adoptableO = "No"
    tallaOtro = RBtallaO.get()
    if tallaOtro == 1:
        tallaO = "Chico"
    elif tallaOtro == 2:
        tallaO = "Mediano"
    elif tallaOtro == 3:
        tallaO = "Grande"
    peloOtro = RBpeloO.get()
    if peloOtro == 1:
        peloO = "Corto"
    elif peloOtro == 2:
        peloO = "Largo"
    elif peloOtro == 3:
        peloO = "Duro"
    elif peloOtro == 4:
        peloO = "Alambre"
    elif peloOtro == 5:
        peloO = "Chino"
    elif peloOtro == 6:
        peloO = str(peloOtroO.get())
    #Conexión
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    try:
        print(tipoO.get())
        print(nombreO.get())
        print(fechanacimientoO)
        print(sexoO)
        print(razaO.get())
        print(colorO.get())
        print(str(peloO))
        print(tallaO)
        print(temperamentoO.get())
        print(esterilizacionO)
        print(discapacidadO.get())
        print(adoptableO)
        print(str(fechaesterilizacionO))
        print(str(fechaingresoO))
        datosO = tipoO.get(),nombreO.get(), fechanacimientoO, sexoO, razaO.get(), colorO.get(), peloO, tallaO, temperamentoO.get(), esterilizacionO, discapacidadO.get(), adoptableO, str(fechaesterilizacionO), str(fechaingresoO)
        cursor.execute("UPDATE otros SET TIPO=?, NOMBRE=?, FECHANACIMIENTO=?, SEXO=?, RAZA=?, COLOR=?, PELO=?, TALLA=?, TEMPERAMENTO=?, ESTERILIZACION=?, DISCAPACIDAD=?, ADOPTABLE=?, FECHAESTERILIZACION=?, FECHAINGRESO=? WHERE ID="+selectedO, (datosO))
        conexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al editar el registro")
        pass
    limpiarCamposO()
    fMainframe2.destroy()
    ventana.iconify()
    abrir_ventana_Otros()
    mostrarCamposO()

def mostrarCamposO():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosO = treeVO.get_children()
    for elemento in registrosO:
        treeVO.delete(elemento)
    try:
        cursor.execute("SELECT * FROM otros")
        for row in cursor:
            treeVO.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
    except:
        pass

def seleccionarUsandoClickO(treeVO):
    global selectedO
    global valuesO
    selectedO = None
    valuesO = None
    selectedO = treeVO.focus()
    valuesO = treeVO.item(selectedO,'values')
    print(selectedO)
    print(valuesO)

def borrarRegistroO():
    try:
        valuesO
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un animal por favor")
        ventana_Otros.deiconify()
        return
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    if messagebox.askyesno(message="¿Realmente desea eliminar el registro? Se borrarán los datos y las imágenes", title="ADVERTENCIA"):
        try:
            try:
                path_2erase_o = os.getcwd() + "\\oimg\\" + selectedO
                shutil.rmtree(path_2erase_o)
            except OSError:
                pass
            cursor.execute("DELETE FROM otros WHERE ID="+selectedO)
            conexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass
    mostrarCamposO()

def mostrarCamposOt():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    registrosO = treeVOt.get_children()
    for elemento in registrosO:
        treeVOt.delete(elemento)
    try:
        cursor.execute("SELECT * FROM otrosarchivados")
        for row in cursor:
            treeVOt.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))
    except:
        pass

def archivarO():
    try:
        valuesO
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un animal por favor")
        ventana_Otros.deiconify()
        return
    if messagebox.askyesno(message="¿Realmente desea archivar el registro?", title="ADVERTENCIA"):
        global estadoOt
        estadoOt = ""
        ventana_archivar_estadoO()
        ventana_Otros.wait_window(ventana_archivar_estado_Otros)
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM otros WHERE ID="+selectedO)
            conexion.commit()
            print("Archivando otro")
            datosOt = [selectedO]
            for i in range(len(valuesO)):
                datosOt.append(valuesO[i])
            datosOt.append(estadoOt)
            cursor.execute("INSERT INTO otrosarchivados VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datosOt)
            conexion.commit()
            mostrarCamposO()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al archivar el animal")
            pass

def desarchivarO():
    if messagebox.askyesno(message="¿Realmente desea desarchivar el registro?", title="ADVERTENCIA"):
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM otrosarchivados WHERE ID="+selectedO)
            conexion.commit()
            print("Desarchivando otro")
            datosOt = [selectedO]
            for i in range(len(valuesO)):
                datosOt.append(valuesO[i])
            datosOt.pop()
            cursor.execute("INSERT INTO otros VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", datosOt)
            conexion.commit()
            mostrarCamposOt()
            mostrarCamposO()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al desarchivar el animal")
            pass

def buscarOt():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_Otro_arch = busqueda_entryOt.get()
    #print(lookup_Otro_arch)
    #print(selCbOt)
    for record in treeVOt.get_children():
        treeVOt.delete(record)
    try:
        cursor.execute("SELECT * FROM otrosarchivados WHERE "+selCbOt+" like ?",(lookup_Otro_arch,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposOt()
        else:
            for record in records:
                treeVOt.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposOt()
    ventana_buscar_Otros_arch.destroy()

def buscarO():
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    lookup_Otro = busqueda_entryO.get()
    #print(lookup_Otro)
    #print(selCbO)
    for record in treeVO.get_children():
        treeVO.delete(record)
    try:
        cursor.execute("SELECT * FROM otros WHERE "+selCbO+" like ?",(lookup_Otro,))
        records = cursor.fetchall()
        #print(records)
        if not records: #empty list
            messagebox.showwarning("ADVERTENCIA","No se encontraron resultados")
            mostrarCamposO()
        else:
            for record in records:
                treeVO.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposO()
    ventana_buscar_Otros.destroy()

def clear_entradas_Otros():
    e_tipoO.delete(0,END)
    e_nombreO.delete(0,END)
    e_anoNacO.delete(0,END)
    e_razaO.delete(0,END)
    e_colorO.delete(0,END)
    e_peloO.delete(0,END)
    e_temperamentoO.delete(0,END)
    e_discapacidadO.delete(0,END)

def insertar_editables_Otros():
    global mesNacO
    #0 tipo
    e_tipoO.insert(0,valuesO[0])
    #1 nombre
    e_nombreO.insert(0,valuesO[1])
    #2 fecha nacimiento
    if(valuesO[2]=="Cachorro" or valuesO[2]=="Joven" or valuesO[2]=="Adulto" or valuesO[2]=="Viejito"):
        comboO.set(valuesO[2])
        mesNacO = valuesO[1]
    else:
        try:
            split_fno = valuesO[2].split('-')
            e_anoNacO.insert(0,split_fno[0])
            comboO.current(newindex=int(split_fno[1])-1)
            mesNacO = split_fno[1]
        except:
            comboO.current(newindex=12)
            mesNacO = "N/A"
    #3 sexo
    if valuesO[3] == 'Hembra':
        RBsexoO.set(1)
    elif valuesO[3] == 'Macho':
        RBsexoO.set(2)
    #4 raza
    e_razaO.insert(0,valuesO[4])
    #5 color
    e_colorO.insert(0,valuesO[5])
    #6 pelo
    if valuesO[6] == 'Corto':
        RBpeloO.set(1)
    elif valuesO[6] == 'Largo':
        RBpeloO.set(2)
    elif valuesO[6] == 'Duro':
        RBpeloO.set(3)
    elif valuesO[6] == 'Alambre':
        RBpeloO.set(4)
    elif valuesO[6] == 'Chino':
        RBpeloO.set(5)
    else:
        RBpeloO.set(6)
        e_peloO.insert(0,valuesO[6])
    #7 talla
    if valuesO[7] == 'Chico':
        RBtallaO.set(1)
    elif valuesO[7] == 'Mediano':
        RBtallaO.set(2)
    elif valuesO[7] == 'Grande':
        RBtallaO.set(3)
    #8 temperamento
    e_temperamentoO.insert(0,valuesO[8])
    #9 esterilizacion
    if valuesO[9] == 'Si':
        RBesterilizacionO.set(1)
    elif valuesO[9] == 'No':
        RBesterilizacionO.set(2)
    #10 discapacidad
    e_discapacidadO.insert(0,valuesO[10])
    #11 adoptable
    if valuesO[11] == 'Si':
        RBadoptableO.set(1)
    elif valuesO[11] == 'No':
        RBadoptableO.set(2)
    #12 fecha esterilizacion
    if not valuesO[12] == "N/A":
        split_feo = valuesO[12].split('-')
        feo_date = date(int(split_feo[0]),int(split_feo[1]),int(split_feo[2]))
        date_fecha_esterilizacionO.set_date(feo_date)
    #13 fecha ingreso
    split_fio = valuesO[13].split('-')
    fio_date = date(int(split_fio[0]),int(split_fio[1]),int(split_fio[2]))
    date_fecha_ingresoO.set_date(fio_date)

#Ventanas Otros -------------------------------------------------------------------------------------------
def ventana_archivar_estadoO():
    global ventana_archivar_estado_Otros
    ventana_archivar_estado_Otros = tk.Toplevel()
    ventana_archivar_estado_Otros.geometry("380x230")
    ventana_archivar_estado_Otros.title("PawSystem Otros Archivar Motivo")
    ventana_archivar_estado_Otros.iconbitmap('paw-icon.ico')
    ventana_archivar_estado_Otros.configure(bg='#0a4369')
    ventana_archivar_estado_Otros.resizable(False, False)
    lbl_vaeo = Label(ventana_archivar_estado_Otros, text="Motivo:", bg='#0a4369', fg="white",font='Helvetica 20')
    lbl_vaeo.pack(pady=10)
    RBestadoo = IntVar()
    RBestadoo.set(1)
    rb_eo1 = tk.Radiobutton(ventana_archivar_estado_Otros, text="Adoptado", padx = 5, variable=RBestadoo, value=1,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
    rb_eo1.pack(pady=10)
    rb_eo2 = tk.Radiobutton(ventana_archivar_estado_Otros, text="Fallecido", padx = 5, variable=RBestadoo, value=2,font=('Helvetica 14'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
    rb_eo2.pack(pady=10)
    btn_aceptar = Button(ventana_archivar_estado_Otros, text="Aceptar", width=7, font='Helvetica 13 bold', bg='#33ff6d',command=lambda: aceptar(RBestadoo))
    btn_aceptar.pack(pady=10)

    def aceptar(RBestadoo):
        global estadoOt
        if RBestadoo.get() == 1:
            estadoOt = "Adoptado"
        else:
            estadoOt = "Fallecido"
        ventana_archivar_estado_Otros.destroy()

def ventana_buscarOt():
    global ventana_buscar_Otros_arch
    ventana_buscar_Otros_arch = tk.Toplevel()
    ventana_buscar_Otros_arch.geometry("700x300")
    ventana_buscar_Otros_arch.title("PawSystem Otros Búsqueda")
    ventana_buscar_Otros_arch.iconbitmap('paw-icon.ico')
    ventana_buscar_Otros_arch.configure(bg='#0a4369')
    ventana_buscar_Otros_arch.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_Otros_arch, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_Otros_arch,state="readonly", font='Helvetica 10', values=["Tipo","Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso","Estado"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_Otros_arch, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryOt
    busqueda_entryOt = ttk.Entry(ventana_buscar_Otros_arch,font=('Helvetica 10'))
    busqueda_entryOt.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_Otros_arch, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBO = Button(ventana_buscar_Otros_arch, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_Otros_arch.destroy())
    btn_cancelarBO.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbOt
        selCbOt = None
        selCbOt = combo.get()
        #print(selCbOt)
        match selCbOt:
            case "Tipo":
                lbl_busqueda_formato.config(text="escriba el tipo de animal")
                selCbOt = "TIPO"
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del animal")
                selCbOt = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbOt = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbOt = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba que animal es")
                selCbOt = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del animal")
                selCbOt = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del animal")
                selCbOt = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del animal")
                selCbOt = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del animal")
                selCbOt = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbOt = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbOt = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbOt = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbOt = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbOt = "FECHAINGRESO"
            case "Estado":
                lbl_busqueda_formato.config(text="escriba Adoptado o Fallecido")
                selCbOt = "STATUS"
        #print(selCbOt)

    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarO = Button(ventana_buscar_Otros_arch, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarOt)
    btn_buscarO.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def ventana_buscarO():
    global ventana_buscar_Otros
    ventana_buscar_Otros = tk.Toplevel()
    ventana_buscar_Otros.geometry("700x300")
    ventana_buscar_Otros.title("PawSystem Otros Búsqueda")
    ventana_buscar_Otros.iconbitmap('paw-icon.ico')
    ventana_buscar_Otros.configure(bg='#0a4369')
    ventana_buscar_Otros.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_Otros, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_Otros,state="readonly", font='Helvetica 10', values=["Tipo","Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Notas","Adoptable","Fecha de esterilización","Fecha de ingreso"])
    combo.grid(column=1, row=0, sticky=W, padx=10, pady=(10,5))
    lbl_busqueda = Label(ventana_buscar_Otros, text="Búsqueda:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    global busqueda_entryO
    busqueda_entryO = ttk.Entry(ventana_buscar_Otros,font=('Helvetica 10'))
    busqueda_entryO.grid(column=1, row=1, sticky=W, padx=10, pady=5)
    lbl_busqueda_formato = Label(ventana_buscar_Otros, text="", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_busqueda_formato.grid(column=1, row=2, sticky=W, padx=7, pady=2)
    btn_cancelarBO = Button(ventana_buscar_Otros, text="Cancelar", width=8, font='Helvetica 11 bold', bg='pink',command=lambda:ventana_buscar_Otros.destroy())
    btn_cancelarBO.grid(column=0, row=4, sticky=W, padx=5, pady=5)

    def selectionCombo(event):
        global selCbO
        selCbO = None
        selCbO = combo.get()
        #print(selCbO)
        match selCbO:
            case "Tipo":
                lbl_busqueda_formato.config(text="escriba el tipo de animal")
                selCbOt = "TIPO"
            case "Nombre":
                lbl_busqueda_formato.config(text="escriba el nombre del animal")
                selCbO = "NOMBRE"
            case "Fecha de nacimiento":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm\no bien escriba N/A, Cachorro, Joven, Adulto o Viejito")
                selCbO = "FECHANACIMIENTO"
            case "Sexo":
                lbl_busqueda_formato.config(text="escriba hembra o macho")
                selCbO = "SEXO"
            case "Raza":
                lbl_busqueda_formato.config(text="escriba que animal es")
                selCbO = "RAZA"
            case "Color":
                lbl_busqueda_formato.config(text="escriba el color del animal")
                selCbO = "COLOR"
            case "Pelo":
                lbl_busqueda_formato.config(text="escriba el pelo del animal")
                selCbO = "PELO"
            case "Talla":
                lbl_busqueda_formato.config(text="escriba la talla del animal")
                selCbO = "TALLA"
            case "Temperamento":
                lbl_busqueda_formato.config(text="escriba el temperamento del animal")
                selCbO = "TEMPERAMENTO"
            case "Esterilización":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbO = "ESTERILIZACION"
            case "Notas":
                lbl_busqueda_formato.config(text="escriba las notas")
                selCbO = "DISCAPACIDAD"
            case "Adoptable":
                lbl_busqueda_formato.config(text="escriba sí o no")
                selCbO = "ADOPTABLE"
            case "Fecha de esterilización":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbO = "FECHAESTERILIZACION"
            case "Fecha de ingreso":
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm-dd")
                selCbO = "FECHAINGRESO"
        #print(selCbO)

    combo.bind("<<ComboboxSelected>>", selectionCombo)
    btn_buscarO = Button(ventana_buscar_Otros, text="Buscar", width=7, font='Helvetica 13 bold', bg='#edd972',command=buscarO)
    btn_buscarO.grid(column=1, row=3, sticky=E, padx=5, pady=5)

def crear_ventana_Otros():
    global ventana_Otros
    ventana_Otros = tk.Toplevel()
    ventana_Otros.geometry("1280x860")
    ventana_Otros.title("PawSystem Otros")
    ventana_Otros.iconbitmap('paw-icon.ico')
    ventana_Otros.configure(bg='#0a4369')
    ventana_Otros.state('zoomed')
    if not os.path.exists(os.path.join(os.getcwd(), "oimg")):
        os.makedirs(os.path.join(os.getcwd(), "oimg"))

def crear_ventana_Otros_archivados():
    global ventana_Otros_archivados
    ventana_Otros_archivados = tk.Toplevel()
    ventana_Otros_archivados.geometry("1280x860")
    ventana_Otros_archivados.title("PawSystem Otros Archivados")
    ventana_Otros_archivados.iconbitmap('paw-icon.ico')
    ventana_Otros_archivados.configure(bg='#0a4369')
    ventana_Otros_archivados.state('zoomed')

def abrir_ventana_Otros_archivados():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_Otros_archivados, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)

    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vot = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vot.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vot_Otros = tk.Label(fHeader_vot, text="Otros archivados", font='Helvetica 36 bold', bg='#0a4369', fg='#2beda3').pack(side='left', padx=10)
    btn_vo_Buscar = tk.Button(fHeader_vot, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarOt).pack(side='right', padx=10)
    btn_vo_LimpiarBusqueda = tk.Button(fHeader_vot, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposOt).pack(side='right', padx=10, pady=(30,0))

    #CONTENTS =============================================================================================================================
    fContents_vOt= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vOt.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("tipo","nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso","estado")
    global treeVOt
    treeVOt = ttk.Treeview(fContents_vOt)
    columnas_Otros(column_names, treeVOt)
    headings_Otros(treeVOt)
    treeVOt.heading("estado", text="Estado")
    treeVOt.column("estado",width=40, minwidth=10)
    treeVOt.place(relwidth=0.98, relheight=0.96)
    scrollbar_Otros(fContents_vOt, treeVOt)
    mostrarCamposOt()
    treeVOt.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickO(treeVOt))

    #FOOTER =============================================================================================================================
    fFooter_vOt= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vOt.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vot_Regresar = tk.Button(fFooter_vOt, text="Regresar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_Otros_archivados.destroy(), ventana_Otros.deiconify(),seleccionarUsandoClickO(treeVO)]).pack(side='right', padx=10)
    btn_vot_Desarchivar = tk.Button(fFooter_vOt, text="Desarchivar", font='Helvetica 20 bold', bg='#aaf76a', command=lambda:[desarchivarO()]).pack(side='left', padx=10)
    btn_vot_VerFotos = tk.Button(fFooter_vOt, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[crear_ventana_ver_fotos_O(True),ventana_Otros_archivados.iconify()]).pack(side='left', padx=10)

def abrir_ventana_Otros():
    #MAIN FRAME
    fMainFrame1 = tk.Frame(ventana_Otros, bg='#0a4369')
    fMainFrame1.pack(fill="both", expand=True)

    #Crear widgets
    #HEADER =============================================================================================================================
    fHeader_vo = tk.Frame(fMainFrame1, bg='#0a4369')
    fHeader_vo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    lbl_vo_Otros = tk.Label(fHeader_vo, text="Otros", font='Helvetica 36 bold', bg='#0a4369', fg='#2beda3').pack(side='left', padx=10)
    btn_vo_Agregar = tk.Button(fHeader_vo, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: agregar_Otros(True)).pack(side='right', padx=10)
    btn_vo_Buscar = tk.Button(fHeader_vo, text="Buscar", font='Helvetica 20 bold', bg='#edd972', command=ventana_buscarO).pack(side='right', padx=10)
    btn_vo_LimpiarBusqueda = tk.Button(fHeader_vo, text="Limpiar búsqueda", font='Helvetica 10 bold', bg='#edd972',command=mostrarCamposO).pack(side='right', padx=10, pady=(30,0))

    #CONTENTS =============================================================================================================================
    fContents_vO= tk.Frame(fMainFrame1, bg='#0a4369')
    fContents_vO.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("tipo","nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso")
    global treeVO
    treeVO = ttk.Treeview(fContents_vO)
    columnas_Otros(column_names, treeVO)
    headings_Otros(treeVO)
    treeVO.place(relwidth=0.98, relheight=0.96)

    mostrarCamposO()
    treeVO.bind("<<TreeviewSelect>>", lambda eff: seleccionarUsandoClickO(treeVO))

    scrollbar_Otros(fContents_vO, treeVO)

    #FOOTER =============================================================================================================================
    fFooter_vO= tk.Frame(fMainFrame1, bg='#0a4369')
    fFooter_vO.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
    btn_vO_MenuPrincipal = tk.Button(fFooter_vO, text="Menú principal", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[ventana_Otros.destroy(), ventana.deiconify()]).pack(side='right', padx=10)
    btn_vO_VerArchivados = tk.Button(fFooter_vO, text="Ver archivados", font='Helvetica 20 bold', bg='#bd95fc', command=lambda:[crear_ventana_Otros_archivados(), abrir_ventana_Otros_archivados(), ventana_Otros.iconify()]).pack(side='right', padx=10)
    btn_vO_VerFotos = tk.Button(fFooter_vO, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[ventana_Otros.iconify(),crear_ventana_ver_fotos_O(False)]).pack(side='left', padx=10)
    btn_vO_Publicar = tk.Button(fFooter_vO, text="Publicar", font='Helvetica 20 bold', bg='#f2925e',command=lambda: [ventana_Otros.iconify(),ventanaPublicarO()]).pack(side='left', padx=10)
    btn_vO_Editar = tk.Button(fFooter_vO, text="Editar", font='Helvetica 20 bold', bg='#34ebc3', command=lambda: agregar_Otros(False)).pack(side='left', padx=10)
    btn_vO_Archivar = tk.Button(fFooter_vO, text="Archivar", font='Helvetica 20 bold', bg='pink', command=lambda:archivarO()).pack(side='left', padx=10)
    btn_vO_Borrar = tk.Button(fFooter_vO, text="Borrar", font='Helvetica 20 bold', bg='#f03932',command=lambda: borrarRegistroO()).pack(side='left', padx=10)

    #Ventana para agregar animalitos
    def agregar_Otros(add):
        if add == False:
            try:
                valuesO
            except NameError:
                messagebox.showwarning("Advertencia","Seleccione un animal por favor")
                return

        fMainFrame1.destroy()
        fMainFrame2 = tk.Frame(ventana_Otros, bg='#0a4369')
        fMainFrame2.pack(fill="both", expand=True)

        fagregar_O_header = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_O_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
        lbl_Vagregar_Otros = tk.Label(fagregar_O_header, text="Otros", font='Helvetica 30 bold', bg='#0a4369', fg='#2beda3').pack(side='left', padx=(10,0))
        lbl_arrowO = Label(fagregar_O_header, text="→", font='Helvetica 24 bold', bg='#0a4369', fg='#2beda3').pack(side='left')

        fagregar_O = tk.Frame(fMainFrame2, bg = '#0a4369')
        fagregar_O.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.77)

        fagregar_O_footer = tk.Frame(fMainFrame2, bg='#0a4369')
        fagregar_O_footer.place(relx=0.01, rely=0.89, relwidth=0.98, relheight=0.1)
        btn_Vagregar_cancelar = tk.Button(fagregar_O_footer, text="Cancelar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda: [fMainFrame2.destroy(), abrir_ventana_Otros()]).pack(side='right', padx=10)

        frameOtro = Frame(fagregar_O_header,bg='#0a4369')
        frameOtro.place(relx=0.15, rely=0.25, relwidth=0.4, relheight=0.45)

        #Labels de categorias
        labels_formulario_Otros(fagregar_O,frameOtro)

        #Calendarios de las categorias
        calendarios_formulario_Otros(fagregar_O)

        #Entradas de las categorias
        entradas_formulario_Otros(fagregar_O,frameOtro)

        #Radio Buttons de las categorias
        radiobtns_formulario_Otros(fagregar_O)

        def selectionComboO(event):
            global mesNacO
            mesNacO = StringVar()
            mesNacO = comboO.get()
            match mesNacO:
                case "Enero":
                    mesNacO = "01"
                case "Febrero":
                    mesNacO = "02"
                case "Marzo":
                    mesNacO = "03"
                case "Abril":
                    mesNacO = "04"
                case "Mayo":
                    mesNacO = "05"
                case "Junio":
                    mesNacO = "06"
                case "Julio":
                    mesNacO = "07"
                case "Agosto":
                    mesNacO = "08"
                case "Septiembre":
                    mesNacO = "09"
                case "Octubre":
                    mesNacO = "10"
                case "Noviembre":
                    mesNacO = "11"
                case "Diciembre":
                    mesNacO = "12"
                case "No aplica":
                    mesNacO = "N/A"
                case "Cachorro":
                    mesNacO = "Cachorro"
                case "Joven":
                    mesNacO = "Joven"
                case "Adulto":
                    mesNacO = "Adulto"
                case "Viejito":
                    mesNacO = "Viejito"

        global comboO
        comboO = ttk.Combobox(fagregar_O,state="readonly", font='Helvetica 10', values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre","No aplica","Cachorro", "Joven", "Adulto", "Viejito"])
        comboO.grid(row=1,column=1,padx=70,sticky=W)
        comboO.bind("<<ComboboxSelected>>", selectionComboO)

        if add == True:
            btn_Vagregar_Agregar = tk.Button(fagregar_O_header, text="Agregar", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[crearO(fMainFrame2)]).pack(side='right', padx=10)
        elif add == False:
            btn_Vagregar_Editar = tk.Button(fagregar_O_header, text="Guardar cambios", font='Helvetica 20 bold', bg='#33ff6d', command=lambda:[editarO(fMainFrame2)]).pack(side='right', padx=10)
            clear_entradas_Otros()
            insertar_editables_Otros()

    def radiobtns_formulario_Otros(fagregar_O):
        global RBsexoO
        RBsexoO = IntVar()
        RBsexoO.set(1)
        rb_sO1 = tk.Radiobutton(fagregar_O, text="Hembra", padx = 5, variable=RBsexoO, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_sO1.grid(row=3,column=1,sticky=W)
        rb_sO2 = tk.Radiobutton(fagregar_O, text="Macho", padx = 5, variable=RBsexoO, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_sO2.grid(row=3,column=1,sticky=W,padx=120)

        global RBesterilizacionO
        RBesterilizacionO = IntVar()
        RBesterilizacionO.set(1)
        rb_eO1 = tk.Radiobutton(fagregar_O, text="Sí", padx = 10, variable=RBesterilizacionO, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_eO1.grid(row=9,column=1,sticky=W)
        rb_eO2 = tk.Radiobutton(fagregar_O, text="No", padx = 10, variable=RBesterilizacionO, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_eO2.grid(row=9,column=1,sticky=W,padx=90)

        global RBadoptableO
        RBadoptableO = IntVar()
        RBadoptableO.set(1)
        rb_aO1 = tk.Radiobutton(fagregar_O, text="Sí", padx = 10, variable=RBadoptableO, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_aO1.grid(row=11,column=1,sticky=W)
        rb_aO2 = tk.Radiobutton(fagregar_O, text="No", padx = 10, variable=RBadoptableO, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_aO2.grid(row=11,column=1,sticky=W,padx=90)

        global RBpeloO
        RBpeloO = IntVar()
        RBpeloO.set(1)
        rb_pO1 = tk.Radiobutton(fagregar_O, text="Corto", padx = 10, variable=RBpeloO, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO1.grid(row=6,column=1,sticky=W)
        rb_pO2 = tk.Radiobutton(fagregar_O, text="Largo", padx = 10, variable=RBpeloO, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO2.grid(row=6,column=1,sticky=W,padx=(90,0))
        rb_pO3 = tk.Radiobutton(fagregar_O, text="Duro", padx = 10, variable=RBpeloO, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO3.grid(row=6,column=1,sticky=W,padx=(182,0))
        rb_pO4 = tk.Radiobutton(fagregar_O, text="Alambre", padx = 10, variable=RBpeloO, value=4,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO4.grid(row=6,column=1,sticky=W,padx=(267,0))
        rb_pO5 = tk.Radiobutton(fagregar_O, text="Chino", padx = 10, variable=RBpeloO, value=5,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO5.grid(row=6,column=1,sticky=W,padx=(377,0))
        rb_pO6 = tk.Radiobutton(fagregar_O, text="Otro:", padx = 10, variable=RBpeloO, value=6,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_pO6.grid(row=6,column=1,sticky=W,padx=(469,0))

        global RBtallaO
        RBtallaO = IntVar()
        RBtallaO.set(1)
        rb_tO1 = tk.Radiobutton(fagregar_O, text="Chico", padx = 5, variable=RBtallaO, value=1,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_tO1.grid(row=7,column=1,sticky=W)
        rb_tO2 = tk.Radiobutton(fagregar_O, text="Mediano", padx = 5, variable=RBtallaO, value=2,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_tO2.grid(row=7,column=1,sticky=W,padx=100)
        rb_tO3 = tk.Radiobutton(fagregar_O, text="Grande", padx = 5, variable=RBtallaO, value=3,font=('Helvetica 12'),bg='#0a4369',fg="white",selectcolor='gray25',activebackground='#0a4369',activeforeground='#2beda3')
        rb_tO3.grid(row=7,column=1,sticky=W,padx=220)

    def entradas_formulario_Otros(fagregar_O,frameOtro):
        global e_tipoO
        e_tipoO = Entry(frameOtro,textvariable=tipoO,font=('Helvetica 14'))
        e_tipoO.grid(row=0,column=1,sticky=W)
        global e_razaO
        e_razaO=tk.Entry(fagregar_O, textvariable=razaO,font=('Helvetica 14'))
        e_razaO.grid(row=4,column=1,sticky=W)
        global e_colorO
        e_colorO=tk.Entry(fagregar_O, textvariable=colorO,font=('Helvetica 14'))
        e_colorO.grid(row=5,column=1,sticky=W)
        global peloOtroO
        peloOtroO = StringVar()
        global e_peloO
        e_peloO=tk.Entry(fagregar_O, textvariable=peloOtroO,font=('Helvetica 14'))
        e_peloO.grid(row=6,column=1,sticky=W,padx=(560,0))
        global e_temperamentoO
        e_temperamentoO=tk.Entry(fagregar_O, textvariable=temperamentoO,font=('Helvetica 14'))
        e_temperamentoO.grid(row=8,column=1,sticky=W)
        global e_nombreO
        e_nombreO=tk.Entry(fagregar_O, textvariable=nombreO,font=('Helvetica 14'))
        e_nombreO.grid(row=0,column=1,sticky=W)
        global e_discapacidadO
        e_discapacidadO=tk.Entry(fagregar_O, textvariable=discapacidadO,font=('Helvetica 14'))
        e_discapacidadO.grid(row=10,column=1,sticky=W)
        global anoNacO
        anoNacO = StringVar()
        global e_anoNacO
        e_anoNacO=tk.Entry(fagregar_O, textvariable=anoNacO,font=('Helvetica 14'))
        e_anoNacO.grid(row=1,column=1,sticky=W,padx=(425,0))

    def calendarios_formulario_Otros(fagregar_O):
        global date_fecha_esterilizacionO
        date_fecha_esterilizacionO = DateEntry(fagregar_O,selectmode ='day')
        date_fecha_esterilizacionO.grid(row=9,column=1, sticky=W,padx=(510,0))
        global date_fecha_ingresoO
        date_fecha_ingresoO = DateEntry(fagregar_O,selectmode ='day')
        date_fecha_ingresoO.grid(row=2,column=1, sticky=W)

    def labels_formulario_Otros(fagregar_O,frameOtro):
        lbl_nombre=tk.Label(fagregar_O,text="Nombre",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_nombre.grid(row=0,column=0,sticky=W,padx=20)
        lbl_fecha_nacimiento=tk.Label(fagregar_O,text="Fecha de nacimiento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento.grid(row=1,column=0,sticky=W,padx=(20,45),pady=7)
        lbl_fecha_nacimiento_mes=tk.Label(fagregar_O,text="mes:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_mes.grid(row=1, column=1,sticky=W,pady=7)
        lbl_fecha_nacimiento_year=tk.Label(fagregar_O,text="año:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_nacimiento_year.grid(row=1, column=1,sticky=W,pady=7,padx=(360,0))
        lbl_sexo=tk.Label(fagregar_O,text="Sexo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_sexo.grid(row=3,column=0,sticky=W,padx=20,pady=7)
        lbl_raza=tk.Label(fagregar_O,text="Raza",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_raza.grid(row=4,column=0,sticky=W,padx=20,pady=7)
        lbl_color=tk.Label(fagregar_O,text="Color",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_color.grid(row=5,column=0,sticky=W,padx=20,pady=7)
        lbl_pelo=tk.Label(fagregar_O,text="Pelo",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_pelo.grid(row=6,column=0,sticky=W,padx=20,pady=7)
        lbl_talla=tk.Label(fagregar_O,text="Talla",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_talla.grid(row=7,column=0,sticky=W,padx=20,pady=7)
        lbl_temperamento=tk.Label(fagregar_O,text="Temperamento",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_temperamento.grid(row=8,column=0,sticky=W,padx=20,pady=7)
        lbl_esterilizacion=tk.Label(fagregar_O,text="Esterilización",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_esterilizacion.grid(row=9,column=0,sticky=W,padx=20,pady=7)
        lbl_discapacidad=tk.Label(fagregar_O,text="Notas",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_discapacidad.grid(row=10,column=0,sticky=W,padx=20,pady=7)
        lbl_adoptable=tk.Label(fagregar_O,text="Adoptable",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_adoptable.grid(row=11,column=0,sticky=W,padx=20,pady=7)
        lbl_fecha_esterilizacion=tk.Label(fagregar_O,text="Fecha de esterilización:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_esterilizacion.grid(row=9,column=1,sticky=W,padx=(267,0),pady=7)
        lbl_fecha_ingreso=tk.Label(fagregar_O,text="Fecha de ingreso",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_ingreso.grid(row=2,column=0,sticky=W,padx=20,pady=7)
        lbl_tipo = Label(frameOtro,text="Tipo de animalito: ",font='Helvetica 20 bold',bg='#0a4369',fg="white")
        lbl_tipo.grid(row=0,column=0,sticky=W)

def scrollbar_Otros(fContents_vO, treeVO):
    scrollbar1 = ttk.Scrollbar(fContents_vO, orient=tk.VERTICAL, command=treeVO.yview)
    treeVO.configure(yscroll=scrollbar1.set)
    scrollbar1.place(relx=0.98, relwidth=0.02, relheight=1)

    scrollbar2 = ttk.Scrollbar(fContents_vO, orient=tk.HORIZONTAL, command=treeVO.xview)
    treeVO.configure(xscroll=scrollbar2.set)
    scrollbar2.place(rely=0.96, relwidth=0.98, relheight=0.04)

def headings_Otros(treeVO):
    treeVO.heading("tipo", text="Tipo")
    treeVO.heading("nombre", text="Nombre")
    treeVO.heading("fechanacimiento", text="Fecha de nacimiento")
    treeVO.heading("sexo", text="Sexo")
    treeVO.heading("raza", text="Raza")
    treeVO.heading("color", text="Color")
    treeVO.heading("pelo", text="Pelo")
    treeVO.heading("talla", text="Talla")
    treeVO.heading("temperamento", text="Temperamento")
    treeVO.heading("esterilizacion", text="Esterilización")
    treeVO.heading("discapacidad", text="Notas")
    treeVO.heading("adoptable", text="Adoptable")
    treeVO.heading("fechaesterilizacion", text="Fecha de esterilización")
    treeVO.heading("fechaingreso", text="Fecha de ingreso")

def columnas_Otros(column_names, treeVO):
    treeVO.configure(columns=column_names, show='headings')
    treeVO.column("#0",width=10, minwidth=10)
    treeVO.column("tipo",width=40, minwidth=10)
    treeVO.column("nombre",width=40, minwidth=10)
    treeVO.column("fechanacimiento",width=40, minwidth=10)
    treeVO.column("sexo",width=10, minwidth=10)
    treeVO.column("raza",width=40, minwidth=10)
    treeVO.column("color",width=15, minwidth=10)
    treeVO.column("pelo",width=40, minwidth=10)
    treeVO.column("talla",width=40, minwidth=10)
    treeVO.column("temperamento",width=40, minwidth=10)
    treeVO.column("esterilizacion",width=40, minwidth=10)
    treeVO.column("discapacidad",width=40, minwidth=10)
    treeVO.column("adoptable",width=40, minwidth=10)
    treeVO.column("fechaesterilizacion",width=40, minwidth=10)
    treeVO.column("fechaingreso",width=40, minwidth=10)

#Ventanas Fotos Otros ------------------------------------------------------------------------------------
def crear_ventana_ver_fotos_O(archivado):
    try:
        valuesO
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un animal por favor")
        ventana_Otros.deiconify()
        return
    global ver_fotos_ven_O
    ver_fotos_ven_O = tk.Toplevel(ventana)
    ver_fotos_ven_O.geometry("1280x720")
    ver_fotos_ven_O.title("PawSystem Otros Fotos")
    ver_fotos_ven_O.iconbitmap('paw-icon.ico')
    ver_fotos_ven_O.configure(bg='#0a4369')
    ver_fotos_ven_O.state('zoomed')
    ver_fotos_ven_O.update_idletasks()
    folder_path = os.path.join(os.getcwd(), "oimg")
    # Verificar si la carpeta existe
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    abrir_ventana_ver_fotos_O(archivado)

def abrir_ventana_ver_fotos_O(archivado):
    fMainFrame3 = tk.Frame(ver_fotos_ven_O, bg='#0a4369')
    fMainFrame3.pack(fill="both", expand=True)
    fVerfotos_O_header = tk.Frame(fMainFrame3, bg='#0a4369')
    fVerfotos_O_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    fverFotos_O_footer = tk.Frame(fMainFrame3, bg = '#0a4369')
    fverFotos_O_footer.place(relx=0.01, rely=0.81, relwidth=0.98, relheight=0.15)

    btn_regresar_O = tk.Button(fVerfotos_O_header, text = "Regresar", font='Helvetica 18 bold', bg='#33ff6d')
    btn_regresar_O.pack(side = 'left')

    lbl_vfo_n_Otros = Label(fVerfotos_O_header, text="", font='Helvetica 30 bold', bg='#0a4369', fg='#2beda3')
    lbl_vfo_n_Otros.pack(side='left', padx=50)
    lbl_vfo_n_Otros.config(text=valuesO[0])
    lbl_vfo_fi_Otros = Label(fVerfotos_O_header, text = "",font='Helvetica 15 bold', bg='#0a4369', fg='#2beda3')
    lbl_vfo_fi_Otros.pack(side = 'right',padx=5)
    lbl_vfo_fi_Otros.config(text = valuesO[12])
    lbl_vfo_fit_Otros = Label(fVerfotos_O_header, text = "Fecha de ingreso: ",font='Helvetica 15 bold', bg='#0a4369', fg='#2beda3')
    lbl_vfo_fit_Otros.pack(side = 'right',padx=5)

    btn_agregarfoto_O = tk.Button(fverFotos_O_footer, text = "Agregar Foto", font='Helvetica 18 bold', bg='#33ff6d')
    btn_agregarfoto_O.pack(side= 'left', padx=45)
    btn_eliminarfotos_O = tk.Button(fverFotos_O_footer, text = "Eliminar foto", font='Helvetica 18 bold', bg='#db5142')
    btn_eliminarfotos_O.pack(side= 'right', padx=45)

    canvas_ver_foto_O = tk.Canvas(fverFotos_O_footer,height =70,width =500, bg = '#C1CDCD')
    canvas_ver_foto_O.pack(side = tk.BOTTOM,fill = tk.X)

    canvas_ver_foto_O.bind('<Configure>', lambda e:canvas_ver_foto_O.bbox('all'))
    slider = tk.Frame(canvas_ver_foto_O)
    canvas_ver_foto_O.create_window((0,0),window = slider, anchor = tk.NW)
    progbarFO = ttk.Progressbar(fVerfotos_O_header, orient='horizontal',mode='determinate',length=500)
    progbarFO.update_idletasks()
    progbarFO.pack(side=TOP,expand=YES)

    threading.Thread(target = lambda:contenido_ver_fotos_O(canvas_ver_foto_O,fverFotos_O_footer,fMainFrame3,archivado,slider,btn_agregarfoto_O,btn_regresar_O,btn_eliminarfotos_O,progbarFO)).start()

def contenido_ver_fotos_O(canvas_ver_foto_O,fverFotos_O_footer,fMainFrame3,archivado,slider,btn_agregarfoto_O,btn_regresar_O,btn_eliminarfotos_O,progbarFO):    
    #Frames de contenidos para fotos
    fVerFotos_O_contents = tk.Frame(fMainFrame3, bg = '#0a4369')
    fVerFotos_O_contents.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.71)

    #Botones ver fotos, regresar y eliminar COMMAND
    if archivado == False:
        btn_regresar_O.config(command = lambda: [ver_fotos_ven_O.destroy(),ventana_Otros.deiconify()])
        btn_agregarfoto_O.config(command = lambda: [agregar_fotos_O(ver_fotos_ven_O),abrir_ventana_ver_fotos_O(False)])
    else:
        btn_regresar_O.config(command = lambda: [ver_fotos_ven_O.destroy(),ventana_Otros_archivados.deiconify()])
        btn_agregarfoto_O.config(command = lambda: [agregar_fotos_O(ver_fotos_ven_O),abrir_ventana_ver_fotos_O(True)])
    btn_eliminarfotos_O.config(command = lambda:[eliminar_foto_O(dir_path_O_fotos, aux_index)])

    #Lbl desplegar imagenes
    lbl_desplegar_img_O = tk.Label(fVerFotos_O_contents,bg = '#0a4369')
    lbl_desplegar_img_O.pack(anchor = tk.CENTER)

    images_list_O = []
    images_vars_O = []

    global dir_path_O_fotos
    images_files = None
    dir_path_O_fotos = os.getcwd() + "/oimg/" + selectedO
    if not os.path.exists(dir_path_O_fotos):
        os.makedirs(dir_path_O_fotos)

    images_files = os.listdir(dir_path_O_fotos)

    for r in range(0, len(images_files)):
        original_image = Image.open(dir_path_O_fotos + '/' + images_files[r])
        width_img_O, height_img_O = original_image.size
        aspect_ratio_O = width_img_O/height_img_O
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_O = 500
        max_height_img_O = 500
        new_width_img_O = min(width_img_O, max_width_img_O)
        new_height_img_O = min(height_img_O, max_height_img_O)

        if aspect_ratio_O > 1:
            #Imagen más ancha que alta
            new_height_img_O = int(new_width_img_O / aspect_ratio_O)
        else:
            #Imagen más alta que ancha
            new_width_img_O = int(new_height_img_O * aspect_ratio_O)

        images_list_O.append([
                ImageTk.PhotoImage(original_image.resize((int(new_width_img_O/7),int(new_height_img_O/7) ), Image.Resampling.LANCZOS)),
                ImageTk.PhotoImage(resized_image.resize((new_width_img_O, new_height_img_O)), Image.Resampling.LANCZOS)
                             ])   
        images_vars_O.append(f'img_{r}')


        progbarFO['value'] += (100/len(images_files))
    progbarFO.pack_forget()


    def desplegar_img_G(index_O):
        global aux_index
        aux_index = index_O
        lbl_desplegar_img_O.config(image = images_list_O[index_O][1])
        lbl_desplegar_img_O.pack(side='left', anchor='center', expand=True)

    for n in range(len(images_vars_O)):
        globals()[images_vars_O[n]] = tk.Button(slider,image=images_list_O[n][0], bd = 0, command = lambda n = n:desplegar_img_G(n))
        globals()[images_vars_O[n]].pack(side =tk.LEFT)

    canvas_ver_foto_O.configure(scrollregion=canvas_ver_foto_O.bbox('all'))
    x_scroll_bar = tk.Scrollbar(fverFotos_O_footer, orient='horizontal')
    x_scroll_bar.pack(side = tk.BOTTOM,fill = tk.X)
    x_scroll_bar.configure(command=canvas_ver_foto_O.xview)
    canvas_ver_foto_O.configure(xscrollcommand=x_scroll_bar.set)
    slider.bind('<Configure>', lambda event: canvas_ver_foto_O.configure(scrollregion=canvas_ver_foto_O.bbox('all')))

    def eliminar_foto_O(dir_path_O_fotos, aux_index): 
        respuesta = messagebox.askyesno("Eliminar imagen","¿Seguro quieres eliminar la imagen?")
        if respuesta ==1:
            res = []
            for path in os.listdir(dir_path_O_fotos):
                # checar si el directorio es un archivo
                if os.path.isfile(os.path.join(dir_path_O_fotos, path)):
                    res.append(path) 
            deletepath = dir_path_O_fotos +"/" +str(res[aux_index])  
            os.remove(deletepath)
            fMainFrame3.destroy()
            if archivado == False:
                abrir_ventana_ver_fotos_O(False)
            else:
                abrir_ventana_ver_fotos_O(True)
        else:
            return 0

    def agregar_fotos_O(ventana):
        current_path_image = filedialog.askopenfilename(initialdir='Imagenes')   
        ruta_G,n_archivo_G = os.path.split(current_path_image)    
        new_path_image = dir_path_O_fotos + "/" + str(n_archivo_G)
        shutil.copyfile(current_path_image, new_path_image)
        fMainFrame3.destroy()

#Textos Otros ---------------------------------------------------------------------------------------------
def ventanaAdopcionO():
    ventana.withdraw()
    ventana_adop_O = tk.Toplevel()
    ventana_adop_O.geometry("1300x720")
    ventana_adop_O.title("Adopción")
    ventana_adop_O.iconbitmap('paw-icon.ico')
    ventana_adop_O.configure(bg='#0a4369')
    ventana_adop_O.state('zoomed')
    ventana_adop_O.update_idletasks()

    textos = [
        "SU 🎞 #HISTORIA CONTINÚA, en #ADOPCIÒN 🐾Un #rescate que aún sigue vigente"
        " 🇲🇽🐾\nNOMBRE: "+valuesO[1]+"\nNACIÓ: "+valuesO[2]+ "\nTALLA: "+valuesO[7]+"\nSEXO: "
        +valuesO[3]+" #"+valuesO[9]+"estaesterilizado\nTEMPERAMENTO: "+valuesO[8]+"#adopta"
        " #adopta #adoptanocompres #amigoomeyocan ❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀"
        " #APADRINAMIENTOVIRTUAL #UnperritogatitoabandonadoenunHOGAR\nPara más información comunícate a:"
        " adopcionesvirtualesomeyocan@yahoo.com.mx #"+valuesO[0]+" #amigo"+valuesO[0]+" #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Conoce a "+valuesO[1]+ "! SU #HISTORIA CONTINUA en #ADOPCION. Nació "+valuesO[2]+" y es un #rescate"
        " que aún sigue vigente, TÚ puedes cambiar su vida\nTALLA: "+valuesO[7]+"\nSEXO:"
        +valuesO[3]+"\n#"+valuesO[9]+"estaesterilizado\nTEMPERAMENTO: "+valuesO[8]+" Con tu ayuda nuestro"
        " #Omeyocanito puede tener una vida mejor y compartir su felicidad y alegría con más personas"
        "\n#adopta #adoptanocompres #amigoperruno ❤ #ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL"
        " #UnperritogatitoabandonadoenunHOGAR Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx" 
        "\n#animalitos #"+valuesO[0]+" #amigo"+valuesO[0]+" #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesO[1]+"!🐾 sigue aquí con nosotros. El es un #Omeyocanito "+valuesO[8]+". Estaríamos muy" 
        " felices de encontrarle una familia que le dé mucho amor.\nPara más información comunícate a:" 
        " adopcionesvirtualesomeyocan@yahoo.com.mx #"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesO[1]+", lleva un rato con nosotros, pero ya quiere conocer a las personas que serán"
        " su #familia ❤️. Es de talla"+valuesO[7]+" ¡ya es tiempo de darle la vida que merece!" 
        " Si no puedes adoptar puedes #apadrinar a"+valuesO[1]+" o #compartir para que encuentre un hogar"
        " 🐾❤️.\n#ADOPTA #adoptame #"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesO[1]+" merece una oportunidad!. Está con nosotros desde "+valuesO[13]+". Ayúdanos a encontrarle" 
        " una familia. Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx \n#adopta "
        "#"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        ""+valuesO[1]+" es de talla "+valuesO[7]+". Es"+valuesO[8]+", y "+valuesO[3]+""  
        "Si quieres adoptar a "+valuesO[1]+" y que formen una hermosa familia juntos❤️🐾, contáctanos."
        "#ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        "adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        "🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        "Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        "\n#"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Me llamo "+valuesO[1]+" estoy buscando una familia que me de mucho cariño🥰." 
        " Soy "+valuesO[8]+" y de tamaño "+valuesO[7]+". Ayúdame a encontrar la familia que tanto he esperado." 
        " #ADOPTA#adoptame #animalitos #Omeyocan #adopta #adoptanocompres ❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " \n#"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #-------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesO[1]+" ya quiere pertenece a una familia, es de talla "+valuesO[7]+"" 
        " Es "+valuesO[8]+". Estamos seguras de que le dará mucho a amor a la familia a la que vaya a pertenecer." 
        " Es muy amigable con otros perros y niños," 
        " pero necesita una familia que pueda brindarle la atención y el tiempo que necesita para mantenerse feliz y saludable."
        " #ADOPTA #adoptame #animalitos #Omeyocan #adopta #adoptanocompres ❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL #Un"+valuesO[0]+"abandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Soy "+valuesO[1]+" y soy "+valuesO[7]+"." 
        " Soy "+valuesO[8]+" Necesito una familia que tenga tiempo y amor para dedicar a un "+valuesO[0]+"activo como yo."
        " Si estás interesado en adoptarme, por favor asegúrate de que tienes el tiempo y los recursos necesarios para cuidarme adecuadamente." 
        " Estoy dispuesto a aprender y estoy ansioso por encontrar un hogar lleno de amor. ¡Gracias por considerarme!",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Hola nosotros somos #Omeyocan🖐🏼! Necesitamos tu ayuda🥹, "+valuesO[1]+" esta buscando una familia con quien compartir su felicidad y cariño ❤️"
        "\nNACIÓ: "+valuesO[2]+"\n"
        "TALLA: "+valuesO[7]+"\n"
        "SEXO: "+valuesO[3]+"\n"
        "#Esterilización "+valuesO[9]+"\n"
        "TEMPERAMENTO: "+valuesO[8]+"\n"
        " #ADOPTA #adoptame #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        "#"+valuesO[0]+" #amigo"+valuesO[0]+"#animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_adop_O,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_adop_O.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(ventana_adop_O, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_O)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_adop_O, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_adop_O, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_adop_O, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_O = Label(ventana_adop_O,text="",font='Helvetica 30 bold', fg='#2beda3', bg='#0a4369')
    lbl_nombre_O.place(relx=0.1, rely=0.02)
    lbl_nombre_O.config(text=valuesO[0])

    lbl_img_O = Label(ventana_adop_O,bg = '#0a4369')
    lbl_img_O.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_Otro_pub(lbl_img_O)).start()

def ventanaNoAdopcionO():
    ventana.withdraw()
    ventana_no_adopt_O = tk.Toplevel()
    ventana_no_adopt_O.geometry("1300x720")
    ventana_no_adopt_O.title("No adopción")
    ventana_no_adopt_O.iconbitmap('paw-icon.ico')
    ventana_no_adopt_O.configure(bg='#0a4369')
    ventana_no_adopt_O.state('zoomed')
    ventana_no_adopt_O.update_idletasks()

    textos = [
        "¡Hola! Soy "+valuesO[1]+" estoy buscando apoyo para poder tener una vida digna🐾." 
        " No soy adoptable, pero puedes apadrinarme de manera virtual  en adopcionesvirtualesomeyocan@yahoo.com.mx." 
        " No todos podemos ser adoptables por distintas razones, pero siempre existen más maneras de apoyar. ❤️"
        " #APADRINA #noadoptable #"+valuesO[0]+"#amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Existen muchos Omeyocanitos que no tienen la posibilidad de ser adoptados😥 ya que algunos se encuentran" 
        " en rehabilitación física y/o emocional, pero puedes apadrinar.\n" 
        ""+valuesO[1]+"🐾💞 no tiene la posibilidad y busca TU🫵 ayuda para poder tener la vida que merece." 
        " adopcionesvirtualesomeyocan@yahoo.com.mx #APADRINA #noadoptable #"+valuesO[0]+"#amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡"+valuesO[1]+" te necesita! Aunque 🚫NO es ADOPTABLE🚫 podrías hacer que tenga una mejor vida y pronta rehabilitación ❤‍🩹 ." 
        " En #Omeyocan hay #omeyocanitos que requieren de atención especial y rehabilitación física o emocional, sin embargo," 
        " puedes #apadrinar y contribuir y hacer el cambio 💓. Esta con nosotros desde "+valuesO[13]+". \n"
        "NACIÓ: "+valuesO[2]+"\n"
        "TALLA: "+valuesO[7]+"\n"
        "SEXO: "+valuesO[3]+"\n"
        "#Esterilizado\n"
        "TEMPERAMENTO: "+valuesO[8]+""
        "🧚🏻‍♀ APADRINAMIENTO VIRTUAL, comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx para mas informarción."
        " #APADRINA #Un"+valuesO[0]+"abandonadoenunHOGAR #"+valuesO[0]+"#amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "¡Haz la diferencia en la vida de "+valuesO[1]+"! Apadrina a uno de los adorables animalistos de Omeyocan, un refugio dedicado a cuidar y proteger a los animales." 
        " Tu apadrinamiento ayudará a cubrir los costos de alimentación, atención médica y cuidado diario de estos animalitos mientras esperan encontrar un hogar amoroso y permanente." 
        " ¡Únete a nosotros en nuestra misión de brindar una vida mejor a estos animalitos necesitados!"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #"+valuesO[0]+"#amigo"+valuesO[0]+"#animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "🚫"+valuesO[1]+" NO ES ADOPTABLE🚫\n"
        " Lleva con nosotros desde "+valuesO[13]+", necesita de tu apoyo para salir adelante,"
        " aunque 🚫NO ES ADOPTABLE🚫 puedes #Apadrinar para ayudar a su cuidado.\n"
        " Para más información comunícate a: adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #apadrina #"+valuesO[0]+"#amigo"+valuesO[0]+"#animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(ventana_no_adopt_O,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=ventana_no_adopt_O.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(ventana_no_adopt_O, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_O)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(ventana_no_adopt_O, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(ventana_no_adopt_O, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(ventana_no_adopt_O, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_O = Label(ventana_no_adopt_O,text="",font='Helvetica 30 bold', fg='#2beda3', bg='#0a4369')
    lbl_nombre_O.place(relx=0.1, rely=0.02)
    lbl_nombre_O.config(text=valuesO[0])

    lbl_img_O = Label(ventana_no_adopt_O,bg = '#0a4369')
    lbl_img_O.place(relx= 0.8, rely=0.05, anchor=N)

    threading.Thread(target = lambda:get_img_Otro_pub(lbl_img_O)).start()

def ventanaDonarO():
    ventana.withdraw()
    donar_O = tk.Toplevel()
    donar_O.geometry("1300x720")
    donar_O.title("Donación")
    donar_O.iconbitmap('paw-icon.ico')
    donar_O.configure(bg='#0a4369')
    donar_O.state('zoomed')

    textos = [
            "¡Hola! Somos Omeyoacan un albergue de animalitos 🐶🐱🐰 que les brinda hogar temporal y cuidado, a los omeyocanitos sin hogar y abandonados."
            " Nos dedicamos a ofrecerles un lugar seguro y amoroso ❤️mientras encontramos un hogar permanente para ellos. Sin embargo, para poder mantenernos y seguir"
            " brindando nuestros servicios, necesitamos tu ayuda🆘. Cualquier donación, por pequeña que sea, nos ayuda a alimentar, vacunar y mantener sanos a nuestros"
            " amigos caninos. Si te gustaría ayudar, dejamos la información aquí abajo. ¡Cualquier ayuda es bienvenida! ¡Gracias!🥰"
            "Si tienes la posibilidad #Échanos 🐾#Amiga dependemos al 💯 de tu ✅apoyo.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,

            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "🆘Amigos es 🚨#URGENTE!🆘\n"
            "A pesar de nuestros🐕 llamados 😢no logramos el OBJETIVO y NECESITAMOS DE TU APOYO\n"
            "🙏¿Crees poder ayudarnos para continuar con este proyecto de vida hecho realidad?🙏\n"
            " 🆘Amigos es 🚨#URGENTE!🆘\n"
            "¿Crees poder 🙏#Écharnos 🐾#Amiga 👍"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "🆘NECESITAMOS AYUDA🆘\n"
            "Los Omeyocanitos necesitan de tu apoyo\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Queremos invitarte a hacer una diferencia en la vida de los animalitos🐾❤️ necesitados en nuestro albergue." 
            " Cada día trabajamos arduamente para asegurarnos de que Omeyocanitos tengan un hogar seguro, comida y atención médica🏥🥖🏠." 
            " Pero no podemos hacerlo solos. Necesitamos de la ayuda de personas como tú para mantener nuestro albergue funcionando y poder ayudar a más animalitos." 
            "Cada donación es muy importante y apreciada. ¡Muchas gracias por considerarnos!🙏\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Omeyoacan es financiado por donaciones de personas como tú❤️🥰."
            " Sin su ayuda, no sería posible continuar nuestra labor de salvar y proteger a estos animales que tanto necesitan nuestro apoyo💪." 
            " Cada donación, por pequeña que sea, hace una gran diferencia💞." 
            "Con su ayuda, podemos proporcionar atención médica, comida nutritiva y juguetes para los perros, así como mantener el refugio en óptimas condiciones." 
            "Cada año, ayudamos a cientos de perros a encontrar un hogar amoroso y seguro❤️🏠.\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
         ,
            "Como Omeyoacan, es nuestra misión es asegurarnos de que cada animalito en nuestro cuidado tenga un hogar permanente y amoroso💞🐾." 
            " Pero para lograrlo, necesitamos de tu ayuda🫵." 
            " Cada donación que recibimos nos ayuda a proporcionar cuidado médico, alimento, agua y un lugar seguro para nuestros amigos peludos." 
            " También nos ayuda a publicitar y promocionar nuestros perros para que encuentren un hogar permanente🏠." 
            " Si te gustaría ayudar, puedes hacer una donación ¡Cualquier ayuda es apreciada y bienvenida! ¡Gracias por pensar en nosotros y en los perros necesitados!🥰"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
            "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
          ,  
            "¡Hola! Se hoy el cambio  que quieres mañana. Muchos #omeyocanitos requieren de tu donación." 
            "El refugio requiere de muchos recursos diariamente, para el alimento, cuidados, mantenimiento y muchas cosas más para cambiar la vida de muchos animalitos." 
            "Si esta en tus posibilidades ayudar, en #Omeyocan estariamos muy agradecidos."
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘🆘🆘 AYUDA🆘🆘🆘\n"
            "Necesitamos de tu apoyo, tu donación ayudará a muchos #Omeyocanitos ¿Nos podrias dar una 🐾 #amiga?\n"
            "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
            ,
            "🆘URGENTE🆘\n"
            "¡TE NECESITAMOS! 🐶🐱🐰\n"
            "¿Nos podrias dar una 🐾 #amiga? CUALQUIER DONATIVO HACE UNA GRAN DIFERENCIA. Todos los #Omeyocanitos te lo agradeceran.\n"
            "🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘🆘URGENTE🆘\n"
             "❤---❤---❤---❤---\n"
            "🐾 #Cuentasoficiales🐾 de Omeyocan👇\n"
            "🐾 💳 Banorte, 7 Eleven, Farmacias Guadalajara\n"
            "Omeyocan Comienzo a Una Nueva Vida, AC.\n"
            "Cta. 06 83 34 52 74\n"
            "CLABE: 07 21 80 00 68 33 45 27 48\n"
            "-------\n"
            "🐾 💳BancoAzteca (Guardadito)\n"
            "JESSICA CASARRUBIAS PLATAS\n"
                "Cta. 55-41 13-93 85-73-91\n"
            "clabe: 12-71- 800-13-93-85-73-910\n"
            "___\n"
            "Oxxo\n"
            "Número de tarjeta 4217 4700 7412 5077\n"
            "———\n"
            "💳 PAYPAL\n"
            "omeyocanac@yahoo.com.mx\n"
            "(De tu #aportación total descuentan un porcentaje)\n"
            "Para donativos en 🎁especie, hay ☝🏻dos opciones:\n"
            "1. Tenemos un 🏡centro de 🐾acopio en Coapa (mándanos inbox para que te demos la dirección).\n"
            "2. O puedes enviar tu donativo a través de la mesa de 🎁de Amazon con envío al centro de acopio; la liga a la lista de deseos de Amazon https://www.amazon.com.mx/hz/wishlist/ls/14I5E4IF9FUVQ\n"
            "💻 Informes vía inbox, mensaje o📧 correo: omeyocanac@yahoo.com.mx\n"
            "🙏 ✅confirmar a: omeyocanac@yahoo.com.mx\n"
            "De parte de de toda la familia de Omeyocan, te agaradecemos tu apoyo, tu like o que nos compartas. #Gracias\n"
            "#ayuda #tenecesitamos #hazladiferencia #donacion #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan\n"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.sample(textos, 1)[0]
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.sample(textos, 1)[0]

    regresar = tk.Button(donar_O,  text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=donar_O.destroy)
    regresar.place(relx=0.01, rely=0.02)

    fotos = tk.Button(donar_O, text="Carpeta de fotos", font='Helvetica 22 bold', bg='#33ff6d',command=carpeta_fotos_O)
    fotos.place(relx=0.8, rely=0.7,anchor=N)

    copy = tk.Button(donar_O, text="Copiar", font='Helvetica 22 bold', bg='#33ff6d',command=copy_to_clipboard)
    copy.place(relx=0.8, rely=0.8,anchor=N)

    otro = tk.Button(donar_O, text="Generar otro texto", font='Helvetica 22 bold', bg='#33ff6d', command=generar_otro_texto)
    otro.place(relx=0.8, rely=0.9,anchor=N)

    fr = Frame(donar_O, bg='#0a4369')
    fr.place(relx=0.025, rely=0.11,relwidth=0.55, relheight=0.85)

    text_box = tk.Text(fr, font=("Roboto", 17), bg="#0a4369", fg="white", bd=0, highlightthickness=0, insertborderwidth=0, exportselection=False,wrap=WORD)
    text_box.insert(tk.END, text)
    text_box.pack(side='left')

    lbl_nombre_O = Label(donar_O,text="",font='Helvetica 30 bold', fg='#2beda3', bg='#0a4369')
    lbl_nombre_O.place(relx=0.1, rely=0.02)
    lbl_nombre_O.config(text=valuesO[0])

    lbl_img_O = Label(donar_O,bg = '#0a4369')
    lbl_img_O.place(relx= 0.8, rely=0.05, anchor=N)

def ventanaPublicarO():
    try:
        valuesO
    except NameError:
        messagebox.showwarning("Advertencia","Seleccione un animal por favor")
        ventana_Otros.deiconify()
        return
    ventana_publicar_O = tk.Toplevel()
    ventana_publicar_O.geometry("1280x720")
    ventana_publicar_O.title("PawSystem Otros")
    ventana_publicar_O.iconbitmap('paw-icon.ico')
    ventana_publicar_O.configure(bg='#0a4369') 
    ventana_publicar_O.state('zoomed')
    ventana_publicar_O.update_idletasks()

    # Crear el botón de regresar
    regresar = tk.Button(ventana_publicar_O, text="Regresar", font='Helvetica 16 bold', bg='#33ff6d',command=lambda:[ventana_publicar_O.destroy(), ventana_Otros.deiconify()])
    regresar.place(relx=0.01, rely=0.02)

    lbl_nombre_O = Label(ventana_publicar_O,text="",font='Helvetica 40 bold', fg='#2beda3', bg='#0a4369')
    lbl_nombre_O.place(relx=0.12, rely=0.05)
    lbl_nombre_O.config(text=valuesO[0])

    # Crear el botón de opciones
    adopcion = tk.Button(ventana_publicar_O, text="Adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaAdopcionO(),ventana.deiconify])
    adopcion.place(relx=0.2, rely=0.85, anchor="center")

    noadop = tk.Button(ventana_publicar_O, text="No adopción", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaNoAdopcionO(),ventana.deiconify])
    noadop.place(relx=0.5, rely=0.85, anchor="center")

    donacion = tk.Button(ventana_publicar_O, text="Donación", font='Helvetica 24 bold', bg="#33ff6d",command=lambda: [ventanaDonarO(),ventana.deiconify])
    donacion.place(relx=0.8, rely=0.85, anchor="center")

    lbl_img_O = Label(ventana_publicar_O,bg = '#0a4369')
    lbl_img_O.place(relx= 0.5, rely=0.2, anchor=N)

    get_img_Otro_pub(lbl_img_O)

def get_img_Otro_pub(lbl_img_O):
    try:
        dir_path_O_fotos = os.getcwd() + "/oimg/" + selectedO #Conseguir directorio de la carpeta de imagenes
        images_files = os.listdir(dir_path_O_fotos)[0]
        original_image = Image.open(dir_path_O_fotos + '/' + images_files)
        width_img_O, height_img_O = original_image.size
        aspect_ratio_O = width_img_O/height_img_O
        resized_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        max_width_img_O = 400
        max_height_img_O = 400
        new_width_img_O = min(width_img_O, max_width_img_O)
        new_height_img_O = min(height_img_O, max_height_img_O)

        if aspect_ratio_O > 1:
            #Imagen más ancha que alta
            new_height_img_O = int(new_width_img_O / aspect_ratio_O)
        else:
            #Imagen más alta que ancha
            new_width_img_O = int(new_height_img_O * aspect_ratio_O)

        new_img = ImageTk.PhotoImage(resized_image.resize((new_width_img_O, new_height_img_O)), Image.Resampling.LANCZOS)
        lbl_img_O.config(image=new_img)
        lbl_img_O.image = new_img   
    except:
        missingImg = (Image.open("noimg.jpg"))
        resized_missingImg = missingImg.resize((300,300), Image.Resampling.LANCZOS)
        new_missingImg = ImageTk.PhotoImage(resized_missingImg)
        lbl_img_O.config(image=new_missingImg)
        lbl_img_O.image = new_missingImg 
        pass

def carpeta_fotos_O():
    try:
        dir_path_O_fotos = os.getcwd() + "/oimg/" + selectedO
        os.startfile(dir_path_O_fotos)
    except:
        messagebox.showwarning("ADVERTENCIA","No hay fotos del animalito registradas")
        return

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
#Código principal
logo = (Image.open("logoOmeyocan.jpg"))
resized_logo = logo.resize((300,200), Image.Resampling.LANCZOS)
new_logo = ImageTk.PhotoImage(resized_logo)

lblLogo = tk.Label(image=new_logo).pack(pady=30)

btnPerros = tk.Button(ventana, text="Perros", width=20, font='Helvetica 18 bold', bg='#33ff6d', command=lambda: [crear_ventana_perros(), abrir_ventana_perros(), ventana.iconify()]).pack(pady=30)
btnGatos = tk.Button(ventana, text="Gatos", width=20, font='Helvetica 18 bold', bg='#33ff6d', command=lambda: [crear_ventana_Gatos(), abrir_ventana_Gatos(), ventana.iconify()]).pack(pady=30)
btnOtros = tk.Button(ventana, text="Otros", width=20, font='Helvetica 18 bold', bg='#33ff6d', command=lambda: [crear_ventana_Otros(), abrir_ventana_Otros(), ventana.iconify()]).pack(pady=30)
btnCerrar = tk.Button(ventana, text="Salir", width=5, font='Helvetica 13 bold', bg='#33ff6d', command=ventana.destroy).place(relx=0.935, rely=0.015)

ventana.mainloop()
