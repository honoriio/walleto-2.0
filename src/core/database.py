# Importações principais
import sqlite3
import os

# Cria e retorna a conexão com o banco de dados SQLite
def get_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do arquivo
    db_path = os.path.join(base_dir, '..', '..', 'data', 'walleto.db')  # Caminho até o banco de dados
    return sqlite3.connect(db_path)




def inicializar_banco():
    criar_tabela_gastos()


def criar_tabela_gastos():
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