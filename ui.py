from tkinter import *

THEME_COLOR = "#527853"

class InventarioInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Loja das Ferragens")
        self.window.config(bg=THEME_COLOR, width=1024, height=1024)
        self.canvas = Canvas(width=100, height=100, highlightthickness=0)
        self.logo_img = PhotoImage(file="picture/logo.png")
        self.canvas.create_image(50, 50, image=self.logo_img)
        self.canvas.grid(row=0, column=0)

        self.title_label = Label(text="Gestão de Inventarios",bg=THEME_COLOR)
        self.title_label.grid(row=0, column=1, sticky="EW")

        self.artigo_label = Label(text="artigo",bg=THEME_COLOR)
        self.artigo_label.grid(row=1, column= 0, sticky="EW")

        self.localizacao = Label(text="localização",bg=THEME_COLOR)
        self.localizacao.grid(row=2, column=0, sticky="EW")

        self.stock = Label(text="Stock",bg=THEME_COLOR)
        self.stock.grid(row=3, column=0, sticky="EW")



        self.window.mainloop()
