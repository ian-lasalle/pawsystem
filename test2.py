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
            mostrarCamposP()
        else:
            for record in records:
                treeVPa.insert("",0,text=record[0], iid=record[0],values=(record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrió un error")
        mostrarCamposP()
    ventana_buscar_perros_arch.destroy()


def ventana_buscarPa():
    global ventana_buscar_perros_arch
    ventana_buscar_perros_arch = tk.Toplevel()
    ventana_buscar_perros_arch.geometry("475x230")
    ventana_buscar_perros_arch.title("PawSystem Perros Búsqueda")
    ventana_buscar_perros_arch.iconbitmap('paw-icon.ico')
    ventana_buscar_perros_arch.configure(bg='#0a4369')
    ventana_buscar_perros_arch.resizable(False, False)
    lbl_opcion = Label(ventana_buscar_perros_arch, text="Opción:", bg='#0a4369', fg="white",font='Helvetica 14')
    lbl_opcion.grid(column=0, row=0, sticky=W, padx=5, pady=(10,5))
    combo = ttk.Combobox(ventana_buscar_perros_arch,state="readonly", font='Helvetica 10', values=["Nombre", "Fecha de nacimiento", "Sexo", "Raza", "Color", "Pelo","Talla","Temperamento","Esterilización","Discapacidad","Adoptable","Fecha de esterilización","Fecha de ingreso","Estado"])
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
                lbl_busqueda_formato.config(text="escriba en formato aaaa-mm")
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
            case "Discapacidad":
                lbl_busqueda_formato.config(text="escriba sí o no")
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