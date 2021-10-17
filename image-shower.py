import tkinter as tk
import requests
from tkinter import filedialog
from webscraping import WebScraping
import os

#instanciamento do tkinter:
ws = tk.Tk()
ws.title("Image shower")

#definindo as configurações do workspace:
canvas = tk.Canvas(ws, width=800, height=400, bg="#AFEEEE")
canvas.grid(columnspan=8, rowspan=8)

#instruções para o usuário:
instructions = tk.Label(ws, bg="#AFEEEE", text="Digite a URL:", font=('Helvatical bold',11))
instructions.grid(columnspan=8, column=0, row=1)

#variáveis:
urlvar = tk.StringVar()


#Input do usuário:
urlentry=tk.Entry(ws, textvariable=urlvar, width=50, font=("default", 11))
urlentry.grid(columnspan=8, column=0, row=2)

#função de download:
def downloadimages():
    options = []
    url_link=urlvar.get()

    options = WebScraping.soup(url_link)

    website_name = url_link.split('//')
    website_name = website_name[1]

    c = 0
    for imgs in options:
        if '.svg' not in imgs:
            c += 1

    message = f"Existem {c} imagens no link indicado."
    imglinks = tk.Label(ws, bg="#AFEEEE", text= f'{message}', font=('Helvatical bold',11))
    imglinks.grid(columnspan=8, column=0, row=3)
    
    current_dic = os.getcwd()
    if not os.path.exists(website_name):
        os.mkdir(website_name)

    os.chdir(website_name)

    i = 0
    for imgs in options:
        if '.svg' not in imgs:
            i += 1
        try:
            url_img = requests.get(imgs)
        except ValueError:
            print("Não foi possível acessar esta url.")
        f = open(f'img{i}.jpg', 'wb')
        f.write(url_img.content)
        f.close()
        
    os.chdir(current_dic)
    

optionButton = tk.Button(text='Baixar imagens', command=downloadimages, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas.create_window(150, 180, window=optionButton)
optionButton.grid(columnspan=8, column=0, row=4)

ws.mainloop()
