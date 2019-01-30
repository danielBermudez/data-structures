from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os.path as path
import grafo

def cargarArchivo():
    entrada = filedialog.askopenfile()
    res =grafo.cargarFloydWarshall(entrada.name)
    grafo.persistencia(res)
    fpunto1()
    fpunto2()

def buscar():
    viaje= [origen.get(),destino.get()]
    ruta = grafo.buscarPunto2(viaje)
    cadena = "Origen -> Destino -> Costo -> Ruta \n\n"
    cadena =cadena + "-> ".join(ruta[0]) + "\n "
    new_winF(cadena)

def donothing(val):
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button" + str(val.get()))
    button.pack()

def selection(paises):
    pos = v.get()
    selection = "You selected the option " + str(paises)
    label.config(text = selection)

def new_winF(texto):
    newwin = Toplevel(root)
    display = Label(newwin, text=texto)
    display.pack()

def selection_changed(self):
    rutas = grafo.buscarPunto1(combo.get())
    cadena = "Origen -> Destino -> Costo -> Ruta \n\n"
    for i in range(len(rutas)):
        cadena =cadena + "-> ".join(rutas[i]) + "\n "
    new_winF(cadena)

def fpunto1():
    combo["values"]=paises
    combo.bind("<<ComboboxSelected>>", selection_changed)

def fpunto2():
    origen["values"]=paises
    destino["values"]=paises

paises = grafo.cargarDatosComprimidos()
root = Tk()
root.geometry("500x500")
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=cargarArchivo)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

labelframe = LabelFrame(root, text="Traveling to all other possible countries:")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="Go File -> Open, to upload the data.")
left.pack()
punto1 = Label(labelframe, text="Select one country to see all the posible routes.")
punto1.pack()
combo = ttk.Combobox(root)

combo.place(x=150, y=80)
labelframe2 = LabelFrame(root, text="Data Structure Challenge")
labelframe2.pack(fill="both", expand="yes")
punto2 = Label(labelframe2, text="Given two countries searching the route:")
punto2.pack()
origenlbl = Label(labelframe2, text="Origin:")
origenlbl.pack()
origenlbl.place(x=40, y=50)
destinolbl = Label(labelframe2, text="Destination:")
destinolbl.pack()
destinolbl.place(x=260, y=50)
origen= ttk.Combobox(labelframe2)
origen.place(x=40, y=80)
destino= ttk.Combobox(labelframe2)
boton = Button(labelframe2,text = "Search",command=buscar)
boton.pack()

destino.place(x=260, y=80)
res = Label(labelframe, text="")
root.config(menu=menubar)

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
languages = ["uno", "dos", "tres", "cuatro", "cinco"]

if(path.exists("paises.xz") and path.exists("rutas.xz")):
    fpunto1()
    fpunto2()
else:
    cargarArchivo()

label = Label(root)
label.pack()
root.mainloop()