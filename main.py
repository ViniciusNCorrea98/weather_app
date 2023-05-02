import tkinter
from tkinter import *
from tkinter import ttk

import requests
import json
from datetime import datetime

import pycountry_convert as pc
import pytz

from PIL import Image, ImageTk

co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


# Criando Frame Top
frame_top = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

# Criando Frame Body
frame_body = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_body.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

global imagem

def informacao():
    api_key = 'f2a8a87693c04da33d1fe79a9b3641e9'
    city_name = entry_local.get()
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, api_key)
    result = requests.get(api_link)

    datas = result.json()

    country = datas['sys']['country']
    zona_fuso = pytz.country_timezones[country]
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")
    city = datas['name']
    humidity = datas['main']['humidity']
    pressure = datas['main']['pressure']
    speed_wind = datas['wind']['speed']
    description = datas['weather'][0]['description']
    state = pytz.country_names[country]


    def country_to_continent(i):
        alpha_country = pc.country_name_to_country_alpha2(i)
        code_continent_country = pc.country_alpha2_to_continent_code(alpha_country)
        continent_name = pc.convert_continent_code_to_continent_name(code_continent_country)

        return continent_name

    continente = country_to_continent(state)
    label_data['text'] = zona_horas
    label_descricao['text'] = description
    label_cidade['text'] = city + " - "+state+" / "+continente
    label_pressao['text'] ="Pressão: " + str(pressure)
    label_hum_simb['text'] = '%'
    label_hum_nome['text'] = 'Humidade'
    label_humidade['text'] = humidity
    label_vel_vento['text'] = "Velocidade do vento: " + str(speed_wind)

    #Trocando o fundo
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H")

    global imagem

    zona_periodo = int(zona_periodo)
    if zona_periodo <= 5 or zona_periodo>=19:
        imagem = Image.open('images/lua.png')
        fundo = fundo_noite
    elif zona_periodo > 5 and zona_periodo <= 12:
        imagem = Image.open('images/sol.png')
        fundo = fundo_dia
    else:
        imagem = Image.open('images/sol_tarde.png')
        fundo = fundo_tarde

    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    label_icon = Label(frame_body, image=imagem, font=('Arial 8 bold'), bg=fundo)
    label_icon.place(x=160, y=50)

    label_data['bg'] = fundo
    label_descricao['bg'] = fundo
    label_cidade['bg'] = fundo
    label_pressao['bg'] = fundo
    label_hum_simb['bg'] = fundo
    label_hum_nome['bg'] = fundo
    label_humidade['bg'] = fundo
    label_vel_vento['bg'] = fundo

    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_body.configure(bg=fundo)




#Configurando o Frame Top

entry_local = Entry(frame_top, width=20, justify='left', font=('', 14), highlightthickness=1, relief='solid')
entry_local.place(x=15 , y=10)

botao_ver_clima = Button(frame_top, comman=informacao,text='Ver clima', font=('Ivy 9 bold'), bg=co1, fg=co2, relief='raised', overrelief=RIDGE)
botao_ver_clima.place(x=250, y=10)



#Configurando o frame body

label_cidade = Label(frame_body, text='Juiz de Fora - Brazil / South America', font=('Arial 10 bold'), bg=fundo, fg=co1, anchor='center')
label_cidade.place(x=10, y=4)

label_data = Label(frame_body, text='09 03 2023 | 10:35:55 AM', font=('Arial 8 bold'), bg=fundo, fg=co1, anchor='center')
label_data.place(x=10, y=54)

label_humidade = Label(frame_body, text='84', font=('Arial 45'), bg=fundo, fg=co1, anchor='center')
label_humidade.place(x=10, y=100)

label_hum_simb = Label(frame_body, text='%', font=('Arial 10 bold'), bg=fundo, fg=co1, anchor='center')
label_hum_simb.place(x=85, y=110)

label_hum_nome = Label(frame_body, text='Humidade', font=('Arial 8'), bg=fundo, fg=co1, anchor='center')
label_hum_nome.place(x=85, y=140)

label_pressao = Label(frame_body, text='Pressão : 1000', font=('Arial 8 bold'), bg=fundo, fg=co1, anchor='center')
label_pressao.place(x=10, y=184)

label_vel_vento = Label(frame_body, text='Velocidade do Vento : 1000', font=('Arial 8 bold'), bg=fundo, fg=co1, anchor='center')
label_vel_vento.place(x=10, y=212)



imagem = Image.open('images/sol.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

label_icon = Label(frame_body, image=imagem, font=('Arial 8 bold'), bg=fundo)
label_icon.place(x=160, y=50)

label_descricao = Label(frame_body, text='Nublado', font=('Arial 8 bold'), bg=fundo, fg=co1, anchor='center')
label_descricao.place(x=170, y=190)




janela.mainloop()