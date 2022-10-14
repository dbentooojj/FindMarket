import mysql.connector
class CRUD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='banco-findmarket.cwoypjmfzxcr.us-east-1.rds.amazonaws.com',
            user='admin',
            password='findentra21',
            database='findmarket',
        )
        self.cursor = self.conexao.cursor()
    def insert_peso(self, mercado, categoria, nome_produto, peso_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto):
        # CRUD
        comando = f'INSERT INTO Produtos (mercado, categoria, nome_produto, peso_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto) VALUES ("{mercado}", "{categoria}", "{nome_produto}", {peso_produto}, {preco_produto}, "{imagem_produto}", "{link_produto}", "{link_logo}", "{data_produto}")'
        self.cursor.execute(comando)
        self.conexao.commit() #confirmar edição do banco
        #resultado = self.cursor.fetchall() #ler o banco de dados
    
    def insert_volume(self, mercado, categoria, nome_produto, volume_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto):
        # CRUD
        comando = f'INSERT INTO Produtos (mercado, categoria, nome_produto, volume_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto) VALUES ("{mercado}", "{categoria}", "{nome_produto}", {volume_produto}, {preco_produto}, "{imagem_produto}", "{link_produto}", "{link_logo}", "{data_produto}")'
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def insert(self, mercado, categoria, nome_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto):
        # CRUD
        comando = f'INSERT INTO Produtos (mercado, categoria, nome_produto, preco_produto, imagem_produto, link_produto, link_logo, data_produto) VALUES ("{mercado}", "{categoria}", "{nome_produto}", {preco_produto}, "{imagem_produto}", "{link_produto}", "{link_logo}", "{data_produto}")'
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def finaliza(self):
        self.cursor.close()
        self.conexao.close()