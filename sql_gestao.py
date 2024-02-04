import sqlite3 as db

# cursor.execute('CREATE TABLE Stock(artigo Text, localizacao FLOAT, stock INTEGER)')
#
# connection.commit()

escolha = input("Consultar stock (C), adicionar (A), remover(R), sair(Q) ").upper()


def save():
    artigo = input("qual o artigo a inserir? ")
    localizacao = input("Localizacao? ")
    stock = input("Stock? ")
    connection = db.connect("stock.db")
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO stock VALUES({artigo}, {localizacao}, {stock})")
    connection.commit()
    connection.close()


def find():
    art = input("Qual o artigo? ")
    connection = db.connect("stock.db")
    cursor = connection.cursor()
    artigo_procurar = cursor.execute(f"SELECT localizacao, stock FROM Stock WHERE artigo = {art}").fetchall()
    connection.close()
    print(artigo_procurar)


def remove():
    artigo_remover = input("Artigo? ")
    connection = db.connect("stock.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM stock WHERE artigo = {artigo_remover}")
    connection.commit()
    connection.close()


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
