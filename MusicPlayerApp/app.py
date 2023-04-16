#Importar librerías
import tkinter as tk
import fnmatch
import os
from pygame import mixer

#Crear Ventana
canvas = tk.Tk()
canvas.iconbitmap('Icon/music_icon.ico')
canvas.title("Music Player")
canvas.geometry("600x500")
canvas.config(bg= "#454545")

#Seleccionar ruta de carpeta
rootpath = "C:/Users/ASUS/Desktop/MusicPlayerApp/Music"


# Especificar el tipo de archivo a seleccionar (Mp3)
pattern = "*.mp3"


#Iniciar el mezclador de pygame
mixer.init()


# Visualizar los archivos en una listbox
frame0 =tk.Frame(canvas, bg="#454545")
scrollbar1 = tk.Scrollbar(frame0, orient="vertical")

listBox = tk.Listbox(frame0, fg="#FF6000", bg="#454545", width=90, font =("Courier",16), yscrollcommand=scrollbar1.set)
scrollbar1.configure(command= listBox.yview)
scrollbar1.pack(side="right", fill="y")
frame0.pack(pady=10)
listBox.pack(padx=15, pady=15)
#prueba de Listbox
#listBox.insert(0, "Coding") 
#listBox.insert(0, "With")
#listBox.insert(2, "Evan")

# Enviar Nombre de canciones a listbox
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert("end", filename)

#Cargar Imagenes para iconos de boton
prev_img =tk.PhotoImage(file="Icon/prev.png")
pause_img =tk.PhotoImage(file="Icon/pause.png")
play_img =tk.PhotoImage(file="Icon/play.png")
stop_img =tk.PhotoImage(file="Icon/stop.png")
next_img =tk.PhotoImage(file="Icon/next.png")


# Definir funciones para cada boton
def select():
    label.config(text= listBox.get("anchor")) # enviar nombre de cancion a etiqueta
    mixer.music.load(rootpath + "//" + listBox.get("anchor")) #ubicar archivo a reproducir
    mixer.music.play() 

def stop():
    mixer.music.stop() #Detiene reproduccion
    listBox.select_clear("active") #Deseleccionar archivo de lista

def pause():
    if pauseButton["text"]=="Pause":
        mixer.music.pause()
        pauseButton["text"]="Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]="Pause"

def play_prev():
       
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    #Reproducir siguiente archivo
    mixer.music.load(rootpath + "//" + prev_song_name)
    mixer.music.play() 

    #Resaltar seleccion
    listBox.select_clear(0,"end")
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    #Reproducir siguiente archivo
    mixer.music.load(rootpath + "//" + next_song_name)
    mixer.music.play() 

    #Resaltar seleccion
    listBox.select_clear(0,"end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


#Crear Etiquetas y Botones

label = tk.Label(canvas, text="", bg="#454545", fg="#FFA559", width=100, font=("Courier", 12))
label.pack(pady=15)

top = tk.Frame(canvas, bg="#454545" )
top.pack(padx=10, pady=15, anchor = "center")

prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg="#454545", borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_= top, side= "left")

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg="#454545", borderwidth=0, command= stop)
stopButton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, text="Play", image=play_img, bg="#454545", borderwidth=0, command= select)
playButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg="#454545", borderwidth=0, command=pause)
pauseButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="Next", image=next_img, bg="#454545", borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side="left")


canvas.mainloop()

