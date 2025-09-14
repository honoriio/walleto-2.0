# área destinada as importaçoes
from src.database.connection import get_connection
from decimal import Decimal
from src.views.colors import cores
import uuid

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = cores()

TM = 160


# --- Definição da Classe Gasto ---
class Gasto:
    def __init__(self, nome, valor, categoria, descricao, data, id=None):

        # Lógica para o ID
        if id is None:
            self.id = str(uuid.uuid4())  # Se nenhum id foi passado, GERE um novo.
        else:
            self.id = id

        self.nome = nome
        self.valor = Decimal(valor) # --> como iremos usar valores monetarios, decidimos usar decimal.
        self.categoria = categoria
        self.descricao = descricao
        self.data = data




# --- Funções do Banco de Dados Refatoradas ---

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



def inserir_gasto(gasto): # insere os valores informados pelo usuario a tabela gastos 
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO gastos (nome, valor, categoria, descricao, data) VALUES (?, ?, ?, ?, ?)", 
                (gasto.nome, str(gasto.valor), gasto.categoria, gasto.descricao, gasto.data)
            )
            if cursor.rowcount > 0:
                conn.commit()
                return {"status": "sucesso", "mensagem": "Gasto Cadastrado com Sucesso!"}
            else:
                return {"status": "erro", "mensagem": "Nenhum gasto cadastrado"}
            
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao cadastrar gasto: {e}"}



def excluir_gastos(id): # exclui o gasto com base no ID informado pelo usuario
     try: 
         with get_connection() as conn: 
             cursor = conn.cursor()
             cursor.execute("SELECT * FROM gastos WHERE id = ?", (id,))
             if cursor.fetchone() is None: 
                 return {"status": "erro", "mensagem": "Nenhum gasto encontrado com esse ID."}
             cursor.execute("DELETE FROM gastos WHERE id = ?", (id,))
             if cursor.rowcount > 0: 
                 conn.commit() 
                 return {"status": "sucesso", "mensagem": f"Gasto com ID {id} foi excluído com sucesso."} 
             else: 
                 return {"status": "erro", "mensagem": "Falha ao excluir o gasto."}
     except Exception as e: 
         return {"status": "erro", "mensagem": f"Erro ao excluir o gasto: {str(e)}"}




def buscar_gasto_por_id(id: int):
    """Busca um gasto, imprime na tela e retorna o objeto Gasto ou None."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gastos WHERE id = ?", (id,))
            resultado = cursor.fetchone()

            if resultado:
                # 1. Converte o resultado para um objeto Gasto
                gasto_obj = Gasto(id=resultado[0], nome=resultado[1], valor=resultado[2], 
                                  categoria=resultado[3], descricao=resultado[4], data=resultado[5])
                
                # 2. Mantém o print de exibição
                valor_formatado = f"R$ {gasto_obj.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
                print("-" * TM)
                print(f"ID: {gasto_obj.id} | Nome Do Gasto: {gasto_obj.nome} | Valor: {valor_formatado} | Categoria: {gasto_obj.categoria} | Descrição: {gasto_obj.descricao} | Data: {gasto_obj.data} ")
                print('-' * TM)
                
                # 3. Retorna o objeto para uso futuro
                return gasto_obj
            
            print(f"Nenhum gasto encontrado com o ID {id}.")
            return None
    except Exception as e:
        print(f"Erro ao buscar gasto: {e}")
        return None



def editar_gastos(dados): 
   
    try:  
         # Validação inicial do ID. O ID não pode estar vazio.
         id_gasto = dados.get("id")
         if not id_gasto:
             return {"status": "erro", "mensagem": "ID do gasto não fornecido."}

         with get_connection() as conn: 
            cursor = conn.cursor() 

            # --- Passo 1: Buscar dados antigos ---
            cursor.execute("SELECT nome, valor, categoria, descricao, data FROM gastos WHERE id = ?", (id_gasto,)) 
            resultado = cursor.fetchone() 

            if not resultado: 
                return {"status": "erro", "mensagem": "Gasto não encontrado."} 

            nome_antigo, valor_antigo, categoria_antiga, descricao_antiga, data_antiga = resultado 


            # Se o novo valor (dados.get(campo)) existir E não for uma string vazia, use-o.
            # Caso contrário (se for None ou ""), mantenha o valor antigo.
            
            nome_novo = dados.get("nome")
            nome = nome_novo if nome_novo else nome_antigo
            
            categoria_nova = dados.get("categoria")
            categoria = categoria_nova if categoria_nova else categoria_antiga
            
            descricao_nova = dados.get("descricao")
            descricao = descricao_nova if descricao_nova else descricao_antiga
            
            data_nova = dados.get("data")
            data = data_nova if data_nova else data_antiga


    
            valor = valor_antigo # Assume o valor antigo por padrão
            valor_novo_str = dados.get("valor")
            
            if valor_novo_str: # Apenas tenta atualizar se um novo valor foi fornecido
                try:
                    valor = float(valor_novo_str)
                except (ValueError, TypeError):
                    # Se a conversão falhar (ex: "abc" ou um formato inválido), 
                    # o código ignora a alteração e mantém o valor_antigo.
                    pass 

            cursor.execute(""" 
                UPDATE gastos 
                SET nome = ?, valor = ?, categoria = ?, descricao = ?, data = ? 
                WHERE id = ? 
            """, (nome, valor, categoria, descricao, data, id_gasto)) 

            if cursor.rowcount > 0: 
                conn.commit() 
                return {"status": "sucesso", "mensagem": "Gasto editado com sucesso!"} 
            else: 
                # Isso pode acontecer se os dados novos forem idênticos aos antigos.
                return {"status": "info", "mensagem": "Nenhuma alteração detectada, os dados já estavam atualizados."}
            
    except KeyError as e: 
         return {"status": "erro", "mensagem": f"Chave {e} não encontrada nos dados fornecidos."} 
    except Exception as e: 
         # Captura genérica para outros erros inesperados (ex: falha de conexão)
         return {"status": "erro", "mensagem": f"Erro inesperado ao editar gasto: {e}"}




def listar_gastos():
    """Busca todos os gastos, imprime na tela e retorna uma lista de objetos Gasto."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gastos")
        resultados = cursor.fetchall()
        
        # 1. Converte todos os resultados para uma lista de objetos Gasto
        gastos_objetos = []
        for tupla in resultados:
            gastos_objetos.append(Gasto(id=tupla[0], nome=tupla[1], valor=tupla[2], 
                                        categoria=tupla[3], descricao=tupla[4], data=tupla[5]))


        for gasto in gastos_objetos:
            valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            print(f"ID: {gasto.id} | Nome Do Gasto: {gasto.nome} | Valor: {valor_formatado} | Categoria: {gasto.categoria} | Descrição: {gasto.descricao} | Data: {gasto.data} ")
            print('-' * TM)

        # 3. Retorna a lista de objetos para uso futuro
        return gastos_objetos



def filtrar_gastos_data(data_inicio, data_final):
    with get_connection() as conn:
        cursor  = conn.cursor()
        cursor.execute("SELECT * FROM gastos WHERE data BETWEEN ? AND ?", (data_inicio, data_final))
        resultados = cursor.fetchall()

        gastos_objetos = []
        for tupla in resultados:
            gastos_objetos.append(Gasto(id=tupla[0], nome=tupla[1], valor=tupla[2], 
                                        categoria=tupla[3], descricao=tupla[4], data=tupla[5]))

        for gasto in gastos_objetos:
            valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            print("-" * TM)
            print(f"ID: {gasto.id} Nome Do Gasto: {gasto.nome}, Valor: {valor_formatado}, Categoria: {gasto.categoria}, Descrição: {gasto.descricao}, Data: {VERDE}{gasto.data}{RESET} ")
            print('-' * TM)
        
        return gastos_objetos



def filtrar_gasto_valor(valor_min, valor_max):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gastos WHERE valor BETWEEN ? AND ?", (str(valor_min), str(valor_max)))
        resultados = cursor.fetchall()
        
        if not resultados:
            print("Não existe gasto com essa faixa de valor.")

        gastos_objetos = []
        for tupla in resultados:
            gastos_objetos.append(Gasto(id=tupla[0], nome=tupla[1], valor=tupla[2], 
                                        categoria=tupla[3], descricao=tupla[4], data=tupla[5]))

        for gasto in gastos_objetos:
            valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            print(f"ID: {gasto.id} Nome Do Gasto: {gasto.nome}, Valor: {VERDE}{valor_formatado}{RESET}, Categoria: {gasto.categoria}, Descrição: {gasto.descricao}, Data: {gasto.data} ")
            print('-' * TM)
        
        return gastos_objetos



def filtrar_gastos_categoria(categoria):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gastos WHERE categoria = ?", (categoria,))
            resultados = cursor.fetchall()

            if not resultados:  # Verifica se a consulta retornou algo
                print(f"Nenhum gasto encontrado na categoria: {categoria}.")
                return None

            gastos_objetos = []
            for tupla in resultados:
                gastos_objetos.append(Gasto(id=tupla[0], nome=tupla[1], valor=tupla[2], 
                                            categoria=tupla[3], descricao=tupla[4], data=tupla[5]))
        
            # Este loop agora vai rodar por completo para todos os gastos
            for gasto in gastos_objetos:
                valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

                print(f'{VERDE}-{RESET}' * TM)
                print(f"ID: {gasto.id} Nome Do Gasto: {gasto.nome}, Valor: {valor_formatado}, Categoria: {VERDE}{gasto.categoria}{RESET}, Descrição: {gasto.descricao}, Data: {gasto.data} ")
                print(f'{VERDE}-{RESET}' * TM)
        
            # O return foi movido para fora do loop.
            # Ele só será executado DEPOIS que o loop de print terminar.
            return gastos_objetos

    except Exception as e:
        print(f"Erro ao buscar gasto: {e}")
        return None


def filtrar_gastos_nome(nome):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gastos WHERE nome = ?", (nome,))
        resultados = cursor.fetchall()

        gastos_objetos = []
        for tupla in resultados:
            gastos_objetos.append(Gasto(id=tupla[0], nome=tupla[1], valor=tupla[2], 
                                        categoria=tupla[3], descricao=tupla[4], data=tupla[5]))

        for gasto in gastos_objetos:
            valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            print(f"ID: {gasto.id} Nome Do Gasto: {VERDE}{gasto.nome}{RESET}, Valor: {valor_formatado}, Categoria: {gasto.categoria}, Descrição: {gasto.descricao}, Data: {gasto.data} ")
            print('-' * TM)

        return gastos_objetos



def calcular_gastos(lista_de_gastos: list[Gasto]):
    """Recebe uma LISTA DE OBJETOS Gasto e calcula o total."""
    if not lista_de_gastos:
        return Decimal('0.00')
    total = sum(gasto.valor for gasto in lista_de_gastos)

    valor_formatado = f"R$ {total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    print("=" * TM)
    print(f"Valor Total Gasto: {VERDE}{valor_formatado}{RESET}")
    return total
