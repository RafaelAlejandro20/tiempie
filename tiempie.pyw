from tools import *

registro = True

def f_tem(data):
    tem.configure(text=data)

def f_hum(data):
    hum.configure(text=data)

def f_imagen_t(data):
    if data < 12.5:
        my_label.configure(image=t1)
    elif data < 25:
        my_label.configure(image=t2)
    elif data < 37.5:
        my_label.configure(image=t3)
    elif data < 50:
        my_label.configure(image=t4)

def f_imagen_h(data):
    if data < 37.5:
        my_label2.configure(image=h1)
    elif data < 55:
        my_label2.configure(image=h2)
    elif data < 72.5:
        my_label2.configure(image=h3)
    elif data < 90:
        my_label2.configure(image=h4)

def clima():
    old_tem = 0
    old_hum = 0
    while registro == True:
        time.sleep(1) 
        datos = arduino.readline().strip().decode().split(',')
        if datos[0] != old_tem:
            f_tem(datos[0])
            f_imagen_t(float(datos[0]))
        if datos[1] != old_hum:
            f_hum(datos[1])
            f_imagen_h(float(datos[1]))
        old_tem = datos[0]
        old_hum = datos[1]

def sel1():
    my_tab.configure(bg_color=azul_claro,fg_color=azul_claro)
    my_tab.configure(bg_color=azul_claro,fg_color=azul_claro)
    resultado.configure(fg_color=azul_claro)
    resultado2.configure(fg_color=azul_claro)

def sel2():
    my_tab.configure(bg_color=azul,fg_color=azul)
    my_tab.configure(bg_color=azul,fg_color=azul)
    resultado.configure(fg_color=azul)
    resultado2.configure(fg_color=azul)

def sel3():
    my_tab.configure(bg_color=azul_oscuro,fg_color=azul_oscuro)
    my_tab.configure(bg_color=azul_oscuro,fg_color=azul_oscuro)
    resultado.configure(fg_color=azul_oscuro)
    resultado2.configure(fg_color=azul_oscuro)

def sel4():
    my_tab.configure(bg_color=gris_oscuro,fg_color=gris_oscuro)
    my_tab.configure(bg_color=gris_oscuro,fg_color=gris_oscuro)
    resultado.configure(fg_color=gris_oscuro)
    resultado2.configure(fg_color=gris_oscuro)
    

resultado = customtkinter.CTkFrame(tab_1,fg_color=azul, width=210, height=250)
resultado.place(relx=0.5,rely=0.5,anchor='center')

plabel(resultado,'Temperatura',0,0)
tem = customtkinter.CTkLabel(resultado,text='Iniciando...',font=simple_f,bg_color=azul,corner_radius=20,width=100,height=20,text_color=blanco)
tem.place(x=0,y=20)

plabel(resultado,'Humedad',110,0)
hum = customtkinter.CTkLabel(resultado,text='Iniciando...',font=simple_f,bg_color=azul,corner_radius=10,width=100,height=20,text_color=blanco)
hum.place(x=110, y=20)

image = customtkinter.CTkImage(light_image=Image.open('t1.png'),size=(60,200))
my_label = customtkinter.CTkLabel(resultado, text='', image=image)
my_label.place(x=75, y=40)

image = customtkinter.CTkImage(light_image=Image.open('h1.png'),size=(40,40))
my_label2 = customtkinter.CTkLabel(resultado, text='', image=image)
my_label2.place(x=120, y=120)

resultado2 = customtkinter.CTkFrame(tab_2,fg_color=azul, width=160)
resultado2.place(relx=0.5,rely=0.5,anchor='center')

glabel(resultado2,'Color de fondo',0,0)

colores = customtkinter.CTkFrame(resultado2,width=160,height=40,corner_radius=0)
colores.grid(column=0,row=1)

selector(colores,azul_claro,sel1,0,0)
selector(colores,azul,sel2,40,0)
selector(colores,azul_oscuro,sel3,80,0)
selector(colores,gris_oscuro,sel4,120,0)

thread1 = threading.Thread(target=clima, daemon=True)
thread1.start()
root.mainloop()