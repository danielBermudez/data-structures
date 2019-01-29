from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os.path as path
import grafo
# ********** grafo *************


# ****** metodo grafo ******************************************


    # Lb1 = Listbox(root)

    # totalPaises = len(paises-1)
    # for x in range(0, len(paises)):
    #     Lb1.insert(x+1, paises[x])
    # Lb1.insert(1, "Python")
    # Lb1.insert(2, "Perl")
    # Lb1.insert(3, paises[0])

    # Lb1.pack()


def cargarArchivo():

    entrada = filedialog.askopenfile()
    res =grafo.cargarFloydWarshall(entrada.name)
    grafo.persistencia(res)
    punto1()
    punto2()

def buscar():
    viaje= [origen.get(),destino.get()]
    ruta = grafo.buscarPunto2(viaje)
    cadena = " "

    cadena =cadena + "-> ".join(ruta[0]) + "\n "
    new_winF(cadena)
    # ******** interfaz ****************************************

def donothing(val):
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button" + str(val.get()))
    button.pack()

root = Tk()
root.geometry("500x500")

menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=cargarArchivo)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)

# editmenu.add_command(label="Undo", command=donothing)
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

# ****************** radio button with array
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
languages = ["uno", "dos", "tres", "cuatro", "cinco"]

# Label(root, text="You selected the option " + str(languages[v.get()]), justify = LEFT, padx = 20).pack()

def selection(paises):
    pos = v.get()
    selection = "You selected the option " + str(paises)
    label.config(text = selection)
def new_winF(texto): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text=texto)
    display.pack()
def selection_changed(self):

    rutas = grafo.buscarPunto1(combo.get())
    cadena = " "
    for i in range(len(rutas)):
        cadena =cadena + "-> ".join(rutas[i]) + "\n "

    new_winF(cadena)

def punto1():

    paises = grafo.cargarDatosComprimidos()
    combo["values"]=paises
    combo.bind("<<ComboboxSelected>>", selection_changed)

def punto2():

    paises =grafo.cargarDatosComprimidos()
    origen["values"]=paises
    destino["values"]=paises


if(path.exists("paises.xz") and path.exists("rutas.xz")):
    punto1()
    punto2()
else:
    cargarArchivo()













label = Label(root)
label.pack()
root.mainloop()

