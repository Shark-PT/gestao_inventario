from ui import InventarioInterface
import json
from tkinter import messagebox
class gestao(InventarioInterface):
    def __init__(self):



        def save():
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