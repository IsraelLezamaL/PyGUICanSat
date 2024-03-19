import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import*
#----------------------
from tkinter import* #Importa todos   #PYW genera ejecutable sin código atrás
from PIL import Image,ImageTk

#CREACIÓN DE PANTALLA PRINCIPAL
HMI=Tk()
HMI.title("Estación de Control CanSat: METEORO RACERS") #Nombre de ventana
w_hmi= HMI.winfo_screenwidth()  #Ancho de pantalla monitor.             
h_hmi= HMI.winfo_screenheight() #Alto de pantalla monitor              
HMI.geometry("%dx%d" % (w_hmi, h_hmi)) #Dimensiones de ventana.
HMI.resizable(1,1) #ancho,alto || Si False, no permite cambio de tamaño.
HMI.iconbitmap("Logo_MeteoroRacers.ico") #Ícono (.ico) de HMI.
HMI.config(cursor="shuttle",) #Cursor de transbordador espacial.
hmi=Canvas(HMI,width=w_hmi,height=h_hmi) #Creación de canvas para interfaz.
hmi.pack(fill="both",expand=True) #Tamaño de canvas.

#LOGOS Y BACKGROUND
back = PhotoImage(file = "back.png") #Fondo de ventana
hmi.create_image((w_hmi/2)+190,(h_hmi/2)+20,image=back, anchor="center") #Se centra y ancla imagen de fondo.
hmi.create_text((w_hmi/2+200), (h_hmi/10), text="Centro de Control CanSAT \n -Meteoro Racers-",justify='center', fill="white", font=('Helvetica 40 bold'),anchor="center") #Título de Ventana
logo1= Image.open("Logo1.png")
rsz_l1=logo1.resize((100,80),Image.LANCZOS)
l1=ImageTk.PhotoImage(rsz_l1)
hmi.create_image(0.5*w_hmi/18,0,image=l1, anchor="nw") #Se centra y ancla imagen de fondo.
logo2= Image.open("Logo2.png")
rsz_l2=logo2.resize((80,50),Image.LANCZOS)
l2=ImageTk.PhotoImage(rsz_l2)
hmi.create_image((2*w_hmi/18),0,image=l2, anchor="nw") #Se centra y ancla imagen de fondo.
logo3= Image.open("Logo3.png")
rsz_l3=logo3.resize((80,80),Image.LANCZOS)
l3=ImageTk.PhotoImage(rsz_l3)
hmi.create_image((16.6*w_hmi/18)+400,0,image=l3, anchor="nw") #Se centra y ancla imagen de fondo.

#MENÚ DE OPCIONES
hmi.create_text((w_hmi/2)+325,(4.2*h_hmi/10),text="Variable Graficada",justify='center', fill="white", font=('Helvetica 20 bold'),anchor="ne") #Menú de Opciones
opt=StringVar()
opt.set("Presión")
menu = OptionMenu(HMI, opt, "Temperatura", "Presión", "Orientación")
menu.pack()
menu.place(x=(w_hmi/2)+150,y=(3*h_hmi/10))
menu.config(cursor="arrow",fg="white", bg="steel blue4")
choice = opt.get()

#GRÁFICO
fig = Figure(figsize=(500, 1000), dpi=200)
fig, ax = plt.subplots()
t = np.arange(0, 3, .01)
if choice=="Temperatura":
    line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
elif choice == "Presión":
    line, = ax.plot(t, 2 * np.cos(2 * np.pi * t))
else:
    line, = ax.plot(t, 8 * np.sin(3 * np.pi * t))
graph= Canvas(hmi,width=2000,height=3000)
graph.place(x= w_hmi/2-100, y= h_hmi/2)
canvas = FigureCanvasTkAgg(fig, graph)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, hmi)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH,expand=1)

#ESTADO DE AUTOGIRO
state= Canvas(hmi,width=110,height=110)
state.place(x= 2*w_hmi/9, y= 8*h_hmi/9)
state.config(background="steel blue4")
estadoAG=StringVar()
estadoAG="INACTIVO"
if estadoAG=="INACTIVO":
    stAG=state.create_oval(10, 10, 100,100,width=3, fill="red")
elif estadoAG=="ACTIVO":
    stAG=state.create_oval(10, 10, 100,100,width=3, fill="green")
else:
    stAG=state.create_oval(10, 10, 100,100,width=3, fill="gray")
hmi.create_text((1.5*w_hmi/9),(8.2*h_hmi/9),text="Estado de \n Autogiro",justify='center', fill="white", font=('Helvetica 20 bold'),anchor="ne")

#ESTADO DE TRANSMISIÓN DE DATOS
state2= Canvas(hmi,width=110,height=110)
state2.place(x= (9*w_hmi/9)+150, y= 8*h_hmi/9)
state2.config(background="steel blue4")
estadoD=StringVar()
estadoD="ACTIVO"
if estadoD=="INACTIVO":
    stD=state2.create_oval(10, 10, 100,100,width=3, fill="red")
elif estadoD=="ACTIVO":
    stD=state2.create_oval(10, 10, 100,100,width=3, fill="green")
else:
    stD=state2.create_oval(10, 10, 100,100,width=3, fill="gray")
hmi.create_text((9*w_hmi/9)+90,(8.2*h_hmi/9),text="Recepción de \n Datos",justify='center', fill="white", font=('Helvetica 20 bold'),anchor="ne")

#VALORES MEDIDOS
Temp=17
T=str(Temp)
in1="Temperatura: "
u1=" °C"
var1=in1+T+u1
Ori=33
O=str(Ori)
in2="Orientación: "
u2=" ° respecto N"
var2=in2+O+u2
Pres=1
P=str(Pres)
in3="Presión: "
u3=" atm"
var3=in3+P+u3
Vel=12
V=str(Vel)
in4="Velocidad: "
u4=" m/s"
var4=in4+V+u4
Dist1=99
D1=str(Dist1)
in5="Distancia Mando-CanSat: "
u5=" m"
var5=in5+D1+u5
Dist2=25
D2=str(Dist2)
in6="Distancia entre Cargas: "
u6=" m"
var6=in6+D2+u6
hmi.create_text((1.82*w_hmi/9)+50,(4*h_hmi/9),text=var1,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((2.5*w_hmi/9)+50,(4.5*h_hmi/9),text=var2,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((1.45*w_hmi/9)+50,(5*h_hmi/9),text=var3,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((1.69*w_hmi/9)+50,(5.5*h_hmi/9),text=var4,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((2.68*w_hmi/9)+50,(6*h_hmi/9),text=var5,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((2.55*w_hmi/9)+50,(6.5*h_hmi/9),text=var6,justify='left', fill="white", font=('Helvetica 20 bold'),anchor="ne")
hmi.create_text((2*w_hmi/9)+50,(2.5*h_hmi/9),text="Recepción de \n Datos",justify='center', fill="white", font=('Helvetica 25 bold'),anchor="ne")

#CRONÓMETRO
hmi.create_text((9*w_hmi/9)+170,(3*h_hmi/9),text="Tiempo de \n Misión",justify='center', fill="white", font=('Helvetica 25 bold'),anchor="ne")
crono= Canvas(hmi,width=200,height=300)
crono.place(x= (8.75*w_hmi/9), y= h_hmi/2)
crono.config(bg="steel blue4")
def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    cronometro.config(text=hour+":"+minute+":"+second)
    cronometro.after(1000,clock)
def update():
    cronometro.config(text="New Text")
cronometro=Label(crono,text="",font=("Helvetica",50),fg="white",bg="steel blue4")
cronometro.pack(pady=20)
clock()

HMI.mainloop() #Ejecución de ventana en bucle infinito (y a escucha de eventos).


