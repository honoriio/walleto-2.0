# área destinada as importaçoes
from src.database.connection import get_connection

class Gasto:
#Representa um gasto e contém as regras de negócio e a lógica de persistência.  
    def __init__(self, nome, valor, categoria, descricao, data, id=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.data = data


class Usuario:
    def __init__(self, nome, email, sexo=None,idade=None, id=None):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.idade = idade
        self.id = id
        self.senha_hash = None

    

def criar_tabela(): # Cria a tabela gastos para armazenar os dados.
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                valor NUMERIC NOT NULL,
                categoria TEXT,
                descricao TEXT,
                data TEXT
            )
        """)

        conn.commit()
        