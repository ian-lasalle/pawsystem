import tkinter as tk
from tkinter import StringVar, ttk, messagebox, filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import *
from tkcalendar import DateEntry
from  datetime import date
import sqlite3
import os
import shutil

ventana = tk.Tk()
ventana.geometry("1280x720")
ventana.title("PawSystem")
ventana.iconbitmap('paw-icon.ico')
ventana.configure(bg='#0a4369') 

conexion = sqlite3.connect("dbomeyocan.db")
cursor = conexion.cursor()

#Funciones

#CRUD PERROS
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
            treeVPa.insert("",0,text=row[0], iid=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
    except:
        pass

def archivarP():
    if messagebox.askyesno(message="¿Realmente desea archivar el registro?", title="ADVERTENCIA"):
        conexion = sqlite3.connect("dbomeyocan.db")
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM perros WHERE ID="+selectedp)
            conexion.commit()
            print("Archivando perro")
            datosPa = [selectedp]
            for i in range(len(valuesp)):
                datosPa.append(valuesp[i])
            cursor.execute("INSERT INTO perrosarchivados VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosPa))
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
            cursor.execute("INSERT INTO perros VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (datosPa))
            conexion.commit()
            mostrarCamposPa()
            mostrarCamposP()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al desarchivar el perro")
            pass

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
    fContents_vpa= tk.Frame(fMainFrame1, bg='red')
    fContents_vpa.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

    column_names = ("nombre","fechanacimiento","sexo","raza","color","pelo","talla","temperamento","esterilizacion","discapacidad","adoptable","fechaesterilizacion","fechaingreso")
    global treeVPa
    treeVPa = ttk.Treeview(fContents_vpa)
    columnas_perros(column_names, treeVPa)
    headings_perros(treeVPa)
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
    fContents_vp= tk.Frame(fMainFrame1, bg='red')
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
    btn_vp_VerArchivados = tk.Button(fFooter_vp, text="Ver archivados", font='Helvetica 20 bold', bg='#bced72', command=lambda:[crear_ventana_perros_archivados(), abrir_ventana_perros_archivados(), ventana_perros.iconify()]).pack(side='right', padx=10)
    btn_vp_VerFotos = tk.Button(fFooter_vp, text="Fotos", font='Helvetica 20 bold', bg='#33ff6d', command = lambda:[crear_ventana_ver_fotos(False),ventana_perros.iconify()]).pack(side='left', padx=10)
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
        fagregar_p.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.75)

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

    #Funciones para compactar codigo
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

def crear_ventana_ver_fotos(archivado):
    global ver_fotos_ven
    ver_fotos_ven = tk.Toplevel(ventana)
    ver_fotos_ven.geometry("1280x720")
    ver_fotos_ven.title("PawSystem Perros")
    ver_fotos_ven.iconbitmap('paw-icon.ico')
    ver_fotos_ven.configure(bg='#0a4369')
    ver_fotos_ven.state('zoomed')
    abrir_ventana_ver_fotos(archivado)        #ventana.deiconify()

def abrir_ventana_ver_fotos(archivado):
    fMainFrame3 = tk.Frame(ver_fotos_ven, bg='#0a4369')
    fMainFrame3.pack(fill="both", expand=True)
    contenido_ver_fotos(fMainFrame3,archivado)

def contenido_ver_fotos(fMainFrame3,archivado):    
    #Frames de contenidos para fotos
    fVerfotos_p_header = tk.Frame(fMainFrame3, bg='#0a4369')
    fVerfotos_p_header.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)
    fVerFotos_p_contents = tk.Frame(fMainFrame3, bg = '#0a4369')
    fVerFotos_p_contents.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.71)
    fverFotos_p_footer = tk.Frame(fMainFrame3, bg = '#0a4369')
    fverFotos_p_footer.place(relx=0.01, rely=0.84, relwidth=0.98, relheight=0.15)

    images_list_p = []
    images_vars_p = []

    def desplegar_img_p(index_p):
        global aux_index
        aux_index = index_p
        lbl_desplegar_img_p.config(image = images_list_p[index_p][1])
        lbl_desplegar_img_p.pack(side='left', anchor='center', expand=True)

    #Botones ver fotos
    if archivado == False:
        btn_regresar_p = tk.Button(fVerfotos_p_header, text = "Regresar", font='Helvetica 18 bold', bg='#33ff6d', command = lambda: [ver_fotos_ven.destroy(),ventana_perros.deiconify()]).pack(side = 'left')
        btn_agregarfoto_p = tk.Button(fverFotos_p_footer, text = "Agregar Foto", font='Helvetica 18 bold', bg='#33ff6d', command = lambda: [agregar_fotos_p(ver_fotos_ven),abrir_ventana_ver_fotos(False)])
        btn_agregarfoto_p.pack(side= 'left', padx=45)
    else:
        btn_regresar_p = tk.Button(fVerfotos_p_header, text = "Regresar", font='Helvetica 18 bold', bg='#33ff6d', command = lambda: [ver_fotos_ven.destroy(),ventana_perros_archivados.deiconify()]).pack(side = 'left')
        btn_agregarfoto_p = tk.Button(fverFotos_p_footer, text = "Agregar Foto", font='Helvetica 18 bold', bg='#33ff6d', command = lambda: [agregar_fotos_p(ver_fotos_ven),abrir_ventana_ver_fotos(True)])
        btn_agregarfoto_p.pack(side= 'left', padx=45)
    lbl_vfp_n_Perros = Label(fVerfotos_p_header, text="", font='Helvetica 30 bold', bg='#0a4369', fg='pink')
    lbl_vfp_n_Perros.pack(side='left', padx=50)
    lbl_vfp_n_Perros.config(text=valuesp[0])
    lbl_vfp_fi_Perros = Label(fVerfotos_p_header, text = "",font='Helvetica 15 bold', bg='#0a4369', fg='pink')
    lbl_vfp_fi_Perros.pack(side = 'right',padx=5)
    lbl_vfp_fi_Perros.config(text = valuesp[12])
    lbl_vfp_fit_Perros = Label(fVerfotos_p_header, text = "Fecha de ingreso: ",font='Helvetica 15 bold', bg='#0a4369', fg='pink')
    lbl_vfp_fit_Perros.pack(side = 'right',padx=5)
    
    btn_eliminarfotos_p = tk.Button(fverFotos_p_footer, text = "Eliminar foto", font='Helvetica 18 bold', bg='#db5142', command = lambda:[ eliminar_foto_p(dir_path_p_fotos, aux_index)])
    btn_eliminarfotos_p.pack(side= 'right', padx=45)

    #Lbl desplegar imagenes
    lbl_desplegar_img_p = tk.Label(fVerFotos_p_contents,bg = '#0a4369')
    lbl_desplegar_img_p.pack(anchor = tk.CENTER)

    canvas_ver_foto_p = tk.Canvas(fverFotos_p_footer,height =75,width =500, bg = '#C1CDCD')
    canvas_ver_foto_p.pack(side = tk.BOTTOM,fill = tk.X)

    x_scrool_bar = ttk.Scrollbar(fverFotos_p_footer, orient = tk.HORIZONTAL)
    x_scrool_bar.pack(side = tk.BOTTOM, fill=tk.X )
    x_scrool_bar.config(command = canvas_ver_foto_p.xview)

    canvas_ver_foto_p.config(xscrollcommand=x_scrool_bar.set)
    canvas_ver_foto_p.bind('<Configure>', lambda e:canvas_ver_foto_p.bbox('all'))

    slider = tk.Frame(canvas_ver_foto_p)
    canvas_ver_foto_p.create_window((0,0),window = slider, anchor = tk.NW)

    global dir_path_p_fotos
    try:
        dir_path_p_fotos = os.getcwd() + "/pimg/" + selectedp #Conseguir directorio de la carpeta de imagenes
        images_files = os.listdir(dir_path_p_fotos)
    except:
        os.makedirs(os.getcwd() + "/pimg/" + selectedp)
        images_files = os.listdir(dir_path_p_fotos)

    for r in range(0, len(images_files)):
        original_image = Image.open(dir_path_p_fotos + '/' + images_files[r])
        width, height = original_image.size
        aspect_ratio = height / width
        resized_image = original_image.resize((400, 400), Image.LANCZOS)
        images_list_p.append([
            ImageTk.PhotoImage(original_image.resize((60, 70), Image.LANCZOS)),
            ImageTk.PhotoImage(resized_image.resize((350, int(350 * aspect_ratio)), Image.LANCZOS))
        ])   
        images_vars_p.append(f'img_{r}')
            
    for n in range(len(images_vars_p)):
        globals()[images_vars_p[n]] = tk.Button(slider,image=images_list_p[n][0], bd = 0, command = lambda n = n:desplegar_img_p(n))
        globals()[images_vars_p[n]].pack(side =tk.LEFT)
            
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
#--------------------------------------------------------------------------------------------------------------------------------
#Main page code
logo = (Image.open("logoOmeyocan.jpg"))
resized_logo = logo.resize((300,200), Image.Resampling.LANCZOS)
new_logo = ImageTk.PhotoImage(resized_logo)

lblLogo = tk.Label(image=new_logo).pack(pady=30)

btnPerros = tk.Button(ventana, text="Perros", width=20, font='Helvetica 18 bold', bg='#33ff6d' , command=lambda: [crear_ventana_perros(), abrir_ventana_perros(), ventana.iconify()]).pack(pady=30)
btnGatos = tk.Button(ventana, text="Gatos", width=20, font='Helvetica 18 bold', bg='#33ff6d',command=lambda: [crear_ventana_gatos(), abrir_ventana_gatos()]).pack(pady=30)
btnConejos = tk.Button(ventana, text="Otros", width=20, font='Helvetica 18 bold', bg='#33ff6d').pack(pady=30)
btnCerrar = tk.Button(ventana, text="Salir", width=5, font='Helvetica 13 bold', bg='#33ff6d', command=ventana.destroy).place(relx=0.935, rely=0.015)

ventana.mainloop()