import tkinter as tk
import requests
from tkinter import filedialog
from webscraping import WebScraping

#instanciamento do tkinter:
ws = tk.Tk()
ws.title("Image shower")

#definindo as configurações do workspace:
canvas = tk.Canvas(ws, width=800, height=400, bg="#AFEEEE")
canvas.grid(columnspan=8, rowspan=8)

#instruções para o usuário:
instructions = tk.Label(ws, bg="#AFEEEE", text="Digite a URL:", font=('Helvatical bold',11))
instructions.grid(columnspan=8, column=0, row=1)

instructions2 = tk.Label(ws, bg="#AFEEEE", text="Digite a URL da imagem:", font=('Helvatical bold',11))
instructions2.grid(columnspan=8, column=0, row=4)

#variáveis:
urlvar = tk.StringVar()
imgvar = tk.StringVar()


#Input do usuário:
urlentry=tk.Entry(ws, textvariable=urlvar, width=50, font=("default", 11))
urlentry.grid(columnspan=8, column=0, row=2)

imgvar=tk.Entry(ws, textvariable=imgvar, width=50, font=("default", 11))
imgvar.grid(columnspan=8, column=0, row=5)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Sucesso")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack(pady=5)
    popup.mainloop()

#função de download:
def setoptions():
    options = []
    url_link=urlvar.get()
    if '.jpg' or '.png' not in url_link:
        options = WebScraping.soup(url_link)
    else:
        options = url_link
    message = "esses são os links de imagens:\n\n"
    for option in options:
        message += option + '\n'
    imglinks = tk.Label(ws, bg="#AFEEEE", text= f'{message}', font=('Helvatical bold',11))
    imglinks.grid(columnspan=8, column=0, row=3)

optionButton = tk.Button(text='Links para imagem', command=setoptions, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas.create_window(150, 180, window=optionButton)
optionButton.grid(columnspan=8, column=6, row=2)


def image_downloader():
    url_link=urlvar.get()
    file_request = filedialog.asksaveasfilename(defaultextension='.jpg')
    url_link = requests.get(url_link)
    f = open(file_request, 'wb')
    f.write(url_link.content)
    f.close()
    popupmsg("Seu download foi bem sucedido!")
#Não há necessidade de usar a função save, pois se pretende não fazer uma lista de arquivos.


#Butão utilizado pelo usuário:
saveAsButton = tk.Button(text='Baixar imagem', command=image_downloader, bg='green', fg='white', font=('Arial', 12, 'bold'))
canvas.create_window(150, 180, window=saveAsButton)
saveAsButton.grid(columnspan=8, column=6, row=5)

ws.mainloop()