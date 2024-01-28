import json


escolha = input("Consultar stock (C), adicionar (A), remover(R), sair(Q) ").upper()


def save():
    artigo = input("Qual o artigo? ")
    local = input("Localização? ")
    quant = input("Stock? ")
    new_data = {
        local: {
            "artigo": artigo,
            "Stock": quant
        }
    }

    if len(artigo) == 0 or len(local) == 0 or len(quant) == 0:
        print("Não deixe campos vazios")
    else:
        try:
            with open("stock_test.json", "r") as stock_file:
                # Verifica se há ficheiro criado
                data = json.load(stock_file)
        except FileNotFoundError:
            with open("stock_test.json", "w") as stock_file:
                json.dump(new_data, stock_file, indent=4)

        else:
            data.update(new_data)
            with open("stock_test.json", "w") as stock_file:
                json.dump(data, stock_file, indent=4)


def remove():
    artigo = input("Qual o artigo? ")
    try:
        with open("stock_test.json") as stock_file:
            data = json.load(stock_file)
    except FileNotFoundError:
        print("Artigo não encontrado")
    else:
        if artigo in data:
            data.pop(artigo)
            data.update(data)
        with open("stock_test.json", "w") as stock_file:
            json.dump(data, stock_file, indent=4)


def find():
    local = input("Qual o artigo? ")
    try:
        with open("stock_test.json") as stock_file:
            data = json.load(stock_file)
            list_data = list(data.values())
            print(list_data)

    except FileNotFoundError:
        print("Artigo não encontrado")
    else:
        index = list_data(local)
        value = list_data[index]
        print(value)
        # if local in data:
        #     artigo = data
        #     print(artigo)
        #     quantidade = data[local]["Stock"]
        #     # print(list(data.keys()[list(data.values()).index(artigo)]))
        #     print(f"O artigo {artigo} está na localização {local} com o stock de {quantidade}")
        # else:
        #     print("Não há stock para esse artigo")


while escolha != "Q":
    if escolha == "A":
        save()
        escolha = input("Consultar stock (C), adicionar (A), remover(R), sair(Q)").upper()

    elif escolha == "C":
        find()
        escolha = input("Consultar stock (C), adicionar (A), remover(R), sair(Q)").upper()

    elif escolha == "R":
        remove()
        escolha = input("Consultar stock (C), adicionar (A), remover(R), sair(Q)").upper()
