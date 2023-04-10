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
    try:
        mesConvP = monthToNum(mesNacP.get())
        fechanacimientoP = anoNacP.get() + "-" + mesConvP
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al crear el registro")
        return
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
    try:
        mesConvP = monthToNum(mesNacP.get())
        fechanacimientoP = anoNacP.get() + "-" + mesConvP
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error al editar el registro")
        return
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

def monthToNum(monthName):
    if monthName == '01' or monthName == '02' or monthName == '03' or monthName == '04' or monthName == '05' or monthName == '06' or monthName == '07' or monthName == '08' or monthName == '09' or monthName == '10' or monthName == '11' or monthName == '12':
        return monthName
    else:
        return {
                'enero': "01",
                'febrero': "02",
                'marzo': "03",
                'abril': "04",
                'mayo': "05",
                'junio': "06",
                'julio': "07",
                'agosto': "08",
                'septiembre': "09", 
                'octubre': "10",
                'noviembre': "11",
                'diciembre': "12",
                'Enero': "01",
                'Febrero': "02",
                'Marzo': "03",
                'Abril': "04",
                'Mayo': "05",
                'Junio': "06",
                'Julio': "07",
                'Agosto': "08",
                'Septiembre': "09", 
                'Octubre': "10",
                'Noviembre': "11",
                'Diciembre': "12",
                '1': "01",
                '2': "02",
                '3': "03",
                '4': "04",
                '5': "05",
                '6': "06",
                '7': "07",
                '8': "08",
                '9': "09", 
                '10': "10",
                '11': "11",
                '12': "12",
                'ENERO': "01",
                'FEBRERO': "02",
                'MARZO': "03",
                'ABRIL': "04",
                'MAYO': "05",
                'JUNIO': "06",
                'JULIO': "07",
                'AGOSTO': "08",
                'SEPTIEMBRE': "09", 
                'OCTUBRE': "10",
                'NOVIEMBRE': "11",
                'DICIEMBRE': "12",
                'ene': "01",
                'feb': "02",
                'mar': "03",
                'abr': "04",
                'may': "05",
                'jun': "06",
                'jul': "07",
                'ago': "08",
                'sep': "09", 
                'oct': "10",
                'nov': "11",
                'dic': "12",
                'Ene': "01",
                'Feb': "02",
                'Mar': "03",
                'Abr': "04",
                'May': "05",
                'Jun': "06",
                'Jul': "07",
                'Ago': "08",
                'Sep': "09", 
                'Oct': "10",
                'Nov': "11",
                'Dic': "12"
        }[monthName]

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
    conexion = sqlite3.connect("dbomeyocan.db")
    cursor = conexion.cursor()
    if messagebox.askyesno(message="¿Realmente desea eliminar el registro? Se borrarán los datos y las imágenes", title="ADVERTENCIA"):
        try:
            path_2erase_p = os.getcwd() + "\\pimg\\" + selectedp
            print(path_2erase_p)
            shutil.rmtree(path_2erase_p)
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
    e_mesNacP.delete(0,END)
    e_razap.delete(0,END)
    e_colorp.delete(0,END)
    e_pelop.delete(0,END)
    e_temperamentop.delete(0,END)
    e_discapacidadp.delete(0,END)

def insertar_editables_perros():
    #0 nombre
    e_nombrep.insert(0,valuesp[0])
    #1 fecha nacimiento
    split_fnp = valuesp[1].split('-')
    e_anoNacP.insert(0,split_fnp[0])
    e_mesNacP.insert(0,split_fnp[1])
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

def ventana_buscarP():
    global ventana_buscar_perros
    ventana_buscar_perros = tk.Toplevel()
    ventana_buscar_perros.geometry("475x230")
    ventana_buscar_perros.title("PawSystem Perros Búsqueda")
    ventana_buscar_perros.iconbitmap('paw-icon.ico')
    ventana_buscar_perros.configure(bg='#0a4369')
    ventana_buscar_perros.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_perros, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_perros,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Discapacidad","Adoptable","Fecha de esterilización","Fecha de ingreso"])
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
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm")
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
            case "Discapacidad":
                lbl_busqueda_formato.config(text="escriba sí o no")
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
        global mesNacP
        mesNacP = StringVar()
        global e_mesNacP
        e_mesNacP = tk.Entry(fagregar_p, textvariable=mesNacP,font=('Helvetica 14'))
        e_mesNacP.grid(row=1,column=1,padx=70,sticky=W)
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
        lbl_discapacidad=tk.Label(fagregar_p,text="Discapacidad",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_discapacidad.grid(row=10,column=0,sticky=W,padx=20,pady=7)
        lbl_adoptable=tk.Label(fagregar_p,text="Adoptable",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_adoptable.grid(row=11,column=0,sticky=W,padx=20,pady=7)
        lbl_fecha_esterilizacion=tk.Label(fagregar_p,text="Fecha de esterilización:",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_fecha_esterilizacion.grid(row=9,column=1,sticky=W,padx=(267,0),pady=7)
        lbl_fecha_ingreso=tk.Label(fagregar_p,text="Fecha de ingreso",font='Helvetica 18',bg='#0a4369',fg="white")
        lbl_fecha_ingreso.grid(row=2,column=0,sticky=W,padx=20,pady=7)
        lbl_na_discapacidad=tk.Label(fagregar_p,text="(escribir N/A si no aplica)",font='Helvetica 14',bg='#0a4369',fg="white")
        lbl_na_discapacidad.grid(row=10,column=1,sticky=W,padx=(270,0),pady=7)

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
    treeVP.heading("discapacidad", text="Discapacidad")
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
    try:
        dir_path_p_fotos = os.getcwd() + "/pimg/" + selectedp #Conseguir directorio de la carpeta de imagenes
        images_files = os.listdir(dir_path_p_fotos)
    except:
        os.makedirs(os.getcwd() + "/pimg/" + selectedp)
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
        " #adopta #adoptanocompres #amigoperruno ❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA 🧚🏻‍♀"
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
        "#ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        "adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        "🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        "Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        "#amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #--------------------------------------------------------------------------------------------------------------------
        "Me llamo "+valuesp[0]+" estoy buscando una familia que me de mucho cariño🥰." 
        " Soy "+valuesp[7]+" y de tamaño "+valuesp[6]+". Ayúdame a encontrar la familia que tanto he esperado." 
        " #ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan",
        #-------------------------------------------------------------------------------------------------------------------
        "Adopta a "+valuesp[0]+" ya quiere pertenece a una familia, es de talla "+valuesp[6]+"" 
        " Es "+valuesp[7]+". Estamos seguras de que le dará mucho a amor a la familia a la que vaya a pertenecer." 
        " Es muy amigable con otros perros y niños," 
        " pero necesita una familia que pueda brindarle la atención y el tiempo que necesita para mantenerse feliz y saludable."
        " #ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
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
        " #ADOPTA#adoptame #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
        " adopta #adoptanocompres #amigoperruno❤#ADOPCIÓN🇲🇽 #ADOPTA #APADRINA"
        " 🧚🏻‍♀ #APADRINAMIENTOVIRTUAL#UnperritogatitoabandonadoenunHOGAR"
        " Para más información comunícate a adopcionesvirtualesomeyocan@yahoo.com.mx"
        " #amigoperruno #amigogatuno #perritos #gatitos #animalitos #Omeyocan"
    ]

    def copy_to_clipboard():
        text = text_box.get("1.0", "end-1c")
        pyperclip.copy(text)

    def generar_otro_texto():
        nuevo_texto = random.choice(textos)
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.choice(textos)

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
        nuevo_texto = random.choice(textos)
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.choice(textos)

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
        nuevo_texto = random.choice(textos)
        text_box.delete("1.0", "end")
        text_box.insert("1.0", nuevo_texto)

    text = random.choice(textos)

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
#Código principal
logo = (Image.open("logoOmeyocan.jpg"))
resized_logo = logo.resize((300,200), Image.Resampling.LANCZOS)
new_logo = ImageTk.PhotoImage(resized_logo)

lblLogo = tk.Label(image=new_logo).pack(pady=30)

btnPerros = tk.Button(ventana, text="Perros", width=20, font='Helvetica 18 bold', bg='#33ff6d' , command=lambda: [crear_ventana_perros(), abrir_ventana_perros(), ventana.iconify()]).pack(pady=30)
btnGatos = tk.Button(ventana, text="Gatos", width=20, font='Helvetica 18 bold', bg='#33ff6d').pack(pady=30)
btnOtros = tk.Button(ventana, text="Otros", width=20, font='Helvetica 18 bold', bg='#33ff6d').pack(pady=30)
btnCerrar = tk.Button(ventana, text="Salir", width=5, font='Helvetica 13 bold', bg='#33ff6d', command=ventana.destroy).place(relx=0.935, rely=0.015)

ventana.mainloop()
