import cv2
import time
import serial
import sqlite3
import imutils
import datetime
import threading
import customtkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox

try:
    arduino = serial.Serial('COM5',9600)
    print('Conexion hecha con exito')
except:
    messagebox.showerror('Arduino no conectado','El arduino no puede conectarse a la aplicación.')

#mi_conexion = sqlite3.connect('db.sqlite3')
#cursor = mi_conexion.cursor()
#cursor.execute("DROP TABLE reglas")
#ursor.execute("CREATE TABLE regla(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ticket TEXT, regla TEXT)")
#def insertar(query):
#    cursor.execute(query)
#    mi_conexion.commit()

#def obtener(query):
#    cursor.execute(query)
#    res = cursor.fetchall()
#    return res

#def obteneruno(query):
#    cursor.execute(query)
#    res = cursor.fetchone()
#    return res

blanco = "#ffffff"
negro = "#000000"
gris = "#3c3c3c"
gris_claro = "#e6e6e6"
gris_oscuro = "#1e1e1e"
azul = "#078bf7"
azul_oscuro = "#0767f7"
verde = "#42b300"
verde_oscuro = "#389800"
azul_claro = "#71bfff"
rojo = "#ff4848"
rojo_oscuro = "#ff1616"

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

def ctkbutton(root,text,color,hover_color,command,y):
    btn = customtkinter.CTkButton(
        root,
        width=200,
        text=text,
        corner_radius=20,
        fg_color=color,
        hover_color=hover_color,
        command=command)
    btn.pack(pady=y)

def ctklabel(root,text,anchor,font,text_color):
    label = customtkinter.CTkLabel(
        root,
        width=200,
        text="Contraseña",
        anchor="sw",
        font=normal_f,
        text_color=gris)
    label.pack()

def ctktitle(root,text,font,y):
    titulo = customtkinter.CTkLabel(
        root,
        text=text,
        font=font)
    titulo.pack(pady=y)

def ctkentry(root,placeholder,variable):
    entry = customtkinter.CTkEntry(
        root,
        width=200,
        placeholder_text=placeholder,
        border_width=1,
        border_color=gris_claro,
        textvariable=variable)
    entry.pack()

def ctkpass(root,placeholder,variable):
    entry = customtkinter.CTkEntry(
        root,
        width=200,
        placeholder_text=placeholder,
        border_width=1,
        border_color=gris_claro,
        show="*",
        textvariable=variable)
    entry.pack()

def glabel(root,text,r,c):
    label = customtkinter.CTkLabel(
        root,
        width=100,
        text=text,
        text_color=blanco
        #anchor="sw"
    )
    label.grid(row=r, column=c)

def plabel(root,text,x,y):
    label = customtkinter.CTkLabel(
        root,
        width=100,
        text=text,
        #anchor="sw"
        text_color=blanco
    )
    label.place(x=x, y=y)

def gtitle(root,text,r,c):
    label = customtkinter.CTkLabel(
        root,
        width=200,
        text=text,
        anchor='w',
        font=title_f
    )
    label.grid(row=r, column=c)

def gentry(root,placeholder,r,c):
    entry = customtkinter.CTkEntry(
        root,
        width=200,
        placeholder_text=placeholder,
        border_width=1,
        border_color=gris_claro)
    entry.grid(row=r, column=c)
    return entry

def pentry(root,placeholder,x,y):
    entry = customtkinter.CTkEntry(
        root,
        width=200,
        placeholder_text=placeholder,
        border_width=1,
        border_color=gris_claro)
    entry.place(x=x, y=y)
    return entry

def gbutton(root,text,color,hover_color,command,r,c,y):
    gua = customtkinter.CTkButton(
        root,
        width=200,
        text=text,
        corner_radius=20,
        fg_color=color,
        hover_color=hover_color,
        command=command)
    gua.grid(row=r, column=c, pady=y)

def selector(root,color,command,x,y):
    gua = customtkinter.CTkButton(
        root,
        width=40,
        height=40,
        text='🖌',
        corner_radius=0,
        fg_color=color,
        hover=color,
        command=command)
    gua.place(x=x, y=y)

def gcombo(root,values,r,c):
    combo = customtkinter.CTkComboBox(
        root,
        values=values,
        width=200,
        border_width=1,
        border_color=gris_claro)
    combo.grid(row=r, column=c)
    return combo

def template(root):
    f1 = customtkinter.CTkFrame(root, width=250, fg_color=blanco)
    f1.pack(side="left", fill="y")
    f2 = customtkinter.CTkFrame(root, fg_color=blanco)
    f2.pack(side="right", fill="both", expand="true")
    return [f1,f2]

def gcustomlabel(root,text,r,c):
    label = customtkinter.CTkLabel(
        root,
        width=200,
        text=text,
        anchor="sw")
    label.grid(row=r, column=c)
    return label

title_f = customtkinter.CTkFont(size=20)
normal_f = customtkinter.CTkFont(size=14)
simple_f = customtkinter.CTkFont(size=12)

root.title("Tempie")
root.geometry("600x400")
root.config(borderwidth=0,background=negro)
root.resizable(1,1)

main = customtkinter.CTkFrame(root, width=600, height=400, fg_color=blanco)
main.pack(fill='both', expand='true')

my_tab = customtkinter.CTkTabview(
    main,
    text_color=blanco,
    segmented_button_selected_hover_color=azul_oscuro,
    segmented_button_selected_color=azul_oscuro,
    segmented_button_unselected_hover_color=azul,
    segmented_button_fg_color=azul,
    segmented_button_unselected_color=azul,
    fg_color=azul,
    bg_color=azul,
    text_color_disabled=gris,
    anchor='center',
    corner_radius=20)
my_tab.pack(fill='both', expand='true')

tab_1 = my_tab.add("Inicio")
tab_2 = my_tab.add("Opciones")

def imagen(img,w,h):
    image = customtkinter.CTkImage(light_image=Image.open(img),size=(w,h))
    return image

t1 = imagen('t1.png',60,200)
t2 = imagen('t2.png',60,200)
t3 = imagen('t3.png',60,200)
t4 = imagen('t4.png',60,200)
h1 = imagen('h1.png',40,40)
h2 = imagen('h2.png',40,40)
h3 = imagen('h3.png',40,40)
h4 = imagen('h4.png',40,40)