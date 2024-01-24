from tkinter import *
import json
from tkinter import messagebox
# from gestao_stock import gestao


THEME_COLOR = "#527853"


class InventarioInterface:
    def __init__(self):

        def save():
            artigo = artigo_entry.get()
            local = localizacao_entry.get()
            quant = stock_entry.get()
            new_data = {
                artigo: {
                    "localizacao": local,
                    "Stock": quant
                }
            }

            if len(artigo) == 0 or len(local) == 0 or len(quant) == 0:
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
                    artigo_entry.delete(0, END)
                    localizacao_entry.delete(0, END)
                    stock_entry.delete(0, END)

        def find():
            artigo = artigo_entry.get()
            try:
                with open("stock.json") as stock_file:
                    data = json.load(stock_file)

            except FileNotFoundError:
                messagebox.showinfo(title="Erro", message="Artigo não encontrado")
            else:
                if artigo in data:
                    local = data[artigo]["localizacao"]
                    quantidade = data[artigo]["Stock"]
                    messagebox.showinfo(title=artigo, message=f"Localização: {local}\n Stock: {quantidade}")
                else:
                    messagebox.showinfo(title="Erro", message="Não há stock para esse artigo")

        def ficha():
            artigo = artigo_entry.get()

        window = Tk()
        window.title("Loja das Ferragens")
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.config(bg=THEME_COLOR,)

        canvas = Canvas(width=200, height=200, highlightthickness=0)
        logo_img = PhotoImage(file="picture/logo.png")
        canvas.create_image(100, 100, image=logo_img)
        canvas.grid(row=0, column=0)

        img_ficha = Canvas(width=400, height=400, highlightthickness=0)
        ficha_img = PhotoImage(file="picture/GA1304.500W.png")
        img_ficha.create_image(200, 200, image=ficha_img)
        img_ficha.grid(row=0, column=4)

        title_label = Label(text="Gestão de Inventarios", bg=THEME_COLOR)
        title_label.grid(row=0, column=1, sticky="EW")

        artigo_label = Label(text="artigo", bg=THEME_COLOR)
        artigo_label.grid(row=1, column=0, sticky="EW")
        artigo_entry = Entry(width=35)
        artigo_entry.grid(row=1, column=1)

        localizacao = Label(text="localização", bg=THEME_COLOR)
        localizacao.grid(row=2, column=0, sticky="EW")
        localizacao_entry = Entry(width=35)
        localizacao_entry.grid(row=2, column=1)

        stock = Label(text="Stock", bg=THEME_COLOR)
        stock.grid(row=3, column=0, sticky="EW")
        stock_entry = Entry(width=35)
        stock_entry.grid(row=3, column=1)

        search_button = Button(text="Search", command=find)
        search_button.grid(row=4, column=0, sticky="EW")

        add_button = Button(text="Add", width=36, command=save)
        add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

        ficha_button = Button(text="Ficha Técnica", width=36, command=ficha)
        ficha_button.grid(row=5, column=0, columnspan=2, sticky="EW")

        window.mainloop()
