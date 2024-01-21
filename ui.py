import json
from tkinter import *
from tkinter import messagebox

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

        self.title_label = Label(text="Gestão de Inventarios", bg=THEME_COLOR)
        self.title_label.grid(row=0, column=1, sticky="EW")

        self.artigo_label = Label(text="artigo", bg=THEME_COLOR)
        self.artigo_label.grid(row=1, column=0, sticky="EW")
        self.artigo_entry = Entry(width=35)
        self.artigo_entry.grid(row=1, column=1)

        self.localizacao = Label(text="localização", bg=THEME_COLOR)
        self.localizacao.grid(row=2, column=0, sticky="EW")
        self.localizacao_entry = Entry(width=35)
        self.localizacao_entry.grid(row=2, column=1)

        self.stock = Label(text="Stock", bg=THEME_COLOR)
        self.stock.grid(row=3, column=0, sticky="EW")
        self.stock_entry = Entry(width=35)
        self.stock_entry.grid(row=3, column=1)

        def save():
            artigo = self.artigo_entry.get()
            localizacao = self.localizacao_entry.get()
            stock = self.stock_entry.get()
            new_data = {
                artigo: {
                    "localizacao": localizacao,
                    "Stock": stock
                }
            }

            if len(artigo) == 0 or len(localizacao) == 0 or len(stock) == 0:
                messagebox.showinfo(title="Erro", message="Não deixe campos vazios")
            else:
                try:
                    with open("stock.json", "r") as stock_file:
                        # Verifica se há ficheiro criado
                        data = json.load(stock_file)
                except FileNotFoundError:
                    with open("stock.json", "w") as stock_file:
                        json.dump(new_data, stock_file, indent=4)

                else:
                    data.update(new_data)
                    with open("stock.json", "w") as stock_file:
                        json.dump(data, stock_file, indent=4)

                finally:
                    self.artigo_entry.delete(0, END)
                    self.localizacao_entry.delete(0, END)
                    self.stock_entry.delete(0, END)

        def find():
            stock = self.stock_entry.get()
            try:
                with open("stock.json") as stock_file:
                    data = json.load(stock_file)
            except FileNotFoundError:
                messagebox.showinfo(title="Erro", message="Artigo não encontrado")
            else:
                if stock in data:
                    artigo = data[self.stock]["artigo"]
                    localizacao = data[self.stock]["localizacao"]
                    messagebox.showinfo(title=stock, message=f"artigo:{artigo}\nLocalização: {localizacao}")
                else:
                    messagebox.showinfo(title="Erro", message="Não há stock para esse artigo")

        search_button = Button(text="Search", command=find)
        search_button.grid(row=4, column=0, sticky="EW")

        add_button = Button(text="Add", width=36, command=save)
        add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
        self.window.mainloop()
