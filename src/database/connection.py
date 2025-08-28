# Importações principais
import sqlite3
import os

# Cria e retorna a conexão com o banco de dados SQLite
def get_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do arquivo
    db_path = os.path.join(base_dir, '..', '..', 'data', 'walleto.db')  # Caminho até o banco de dados
    return sqlite3.connect(db_path)