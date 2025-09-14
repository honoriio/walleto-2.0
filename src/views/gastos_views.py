# área destinada as importações
from decimal import Decimal, InvalidOperation  
import string 
import datetime
from src.models.gastos import Gasto

TM = 160

def nome_gasto(): # --> FUNÇÃO CRIADA PARA COLETAR E VALIDAR NOME
    while True:
        try:
            print("-" * TM)
            nome = input('Nome do gasto: ').strip()
            
            if not nome: # --> VALIDAÇÃO 1, VERIFICA SE A STRING ESTA VAZIA
                raise ValueError("O nome não pode estar vazio.")
            
            if len(nome) >= 41: #-->  VALIDAÇÃO 2, O NOME NÃO PODE TER MAIS DE 40 CARACTERES
                raise ValueError("O nome não pode ter mais que 40 caracteres.")
            return nome
            
        except ValueError as erro:
            print(f"ERRO: {erro}")


def valor_gasto(): # --> FUNÇÃO QUE COLETA, TRATA E VALIDA O VALOR DO GASTO INFORMADO PELO USUARIO
    while True:
        try:
            print("-" * TM)
            valor = input('Valor: R$ ')
            valor = valor.replace(',', '.')  # --> Substitui a vírgula por ponto
            valor = Decimal(valor)
            if valor <= 0: # --> VALIDAÇÃO 1, O VALOR NÃO PODE SER MENOR OU IGUAL A ZERO.
                raise ValueError
            
            return valor
            
        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("O valor não pode ser negativo ou menor que zero.")
            
        

def categoria_gasto(): # --> COLETA E TRATA A CATEGORIA
    while True:
        try:
            print("-" * TM)
            categoria = input('Categoria: ').strip().capitalize()
            if not categoria: # --> CASO O USUARIO NÃO INFORME A CATEGORIA DO GASTO, O PROGRAMA INSERE UMA MENSAGEM GENERICA NA CATEORIA
                categoria = "Categoria não informada"
            
            caracteres_proibidos = string.punctuation + string.digits
            if any(char in caracteres_proibidos for char in categoria): # --> BARRA O USUARIO DE INSERIR CARACTERES E NUMEROS NA CATEGORIA.
                raise ValueError("A categoria deve conter apenas letras.")
            
            if len(categoria) >= 50: # --> O CAMPO CATEGORIA E LIMITADO A 50  CARACTERES.
                raise ValueError("A categoria não pode ser maior que 50 caracteres.")
            
            return categoria
            
        except ValueError as erro:
            print(f"ERRO: {erro}")
            

def descricao_gasto(): # --> COLETA E TRATA O CAMPO DESCRIÇÃO
    while True:
        try:
            print("-" * TM)
            descricao = input("Descrição: ").strip().lower()
            if not descricao: # --> CASO O USUARIO NÃO INFPORME UMA DESCRIÇÃO O PROGRAMA IRA INSERIR UMA DESCRIÇÃO GENERICA
                descricao = "Descrição não informada pelo usuario"
            
            if len(descricao) >= 500: # -->  CAMPO DESCRIÇÃO NÃO PODE TER MAIS DE 500 CARACTERES
                raise ValueError("Descrção não pode ter mais que 500 caracteres.")
            return descricao
        
        except ValueError as erro:
            print(f"ERRO: {erro}")



def data_gasto(): # --> COLETA E TRATA A DATA INFORMADA PELO USUARIO
    while True:
        try:
            print("-" * TM)
            data_str = input("Data (DD/MM/AAAA): ").strip()
            
            if not data_str:
                return datetime.date.today().strftime("%d/%m/%Y")
            
            
            if len(data_str) == 8 and data_str.isdigit(): # --> TRATA DATOS SEM SEPARADORES (DDMMAAAA)
                data_str = f"{data_str[0:2]}/{data_str[2:4]}/{data_str[4:8]}"

            # --> TRATA DADOS COM OUTROS SEPARADORES
            data_limpa = data_str.replace('.', '/').replace('-', '/').replace('_', '/').replace('=', '/')

            data_valida = datetime.datetime.strptime(data_limpa, "%d/%m/%Y").date()
            
            return data_valida.strftime("%d/%m/%Y") # --> RETORNA A DATA NO FORMATO BRASILEIRO
        
        except ValueError:
            print("ERRO: Formato de data inválido ou data não existe. Por favor, use DD/MM/AAAA ou DDMMAAAA.")


def entrada_gastos(): # --> REUNE TODAS AS FUNÇÕES DE COLETA DE DADOS NA ORDEM CORRETA
    nome = nome_gasto()
    valor = valor_gasto()
    categoria = categoria_gasto()
    descricao = descricao_gasto()
    data = data_gasto()

    return Gasto(nome, valor, categoria, descricao, data)


# ------------------- FUNÇÕES PARA COLETAR DADOS PARA EDIÇÃO ----------------------------------


def id_editar_gasto(): # --> Função que coleta o ID do gasto para edição
   while True:
        # Pede o dado ao usuário usando a mensagem fornecida
        print("-" * TM)
        entrada_usuario = input("Informe o id do gasto: ")
        
        try:
            numero = int(entrada_usuario)
            return numero
        
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros. Tente novamente.")


def nome_editar_gasto(): # --> FUNÇÃO CRIADA PARA COLETAR E VALIDAR NOME PARA EDITAR UM GASTO
    while True:
        try:
            print("-" * TM)
            nome = input('Nome do gasto: ').strip()
            
            if len(nome) >= 41: #-->  VALIDAÇÃO 2, O NOME NÃO PODE TER MAIS DE 40 CARACTERES
                raise ValueError("O nome não pode ter mais que 40 caracteres.")
            return nome
            
        except ValueError as erro:
            print(f"ERRO: {erro}")


def valor_editar_gasto(): # --> FUNÇÃO QUE COLETA, TRATA E VALIDA O VALOR DO GASTO INFORMADO PELO USUARIO
    while True:
        try:
            print("-" * TM)
            valor = input("Valor R$: ")
            if valor == "":
                return valor
            else:

                valor = valor.replace(',', '.')  # --> Substitui a vírgula por ponto
                valor = Decimal(valor)
            
                return valor
            
        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("O valor não pode ser negativo ou menor que zero.")


def categoria_editar_gasto(): # --> COLETA E TRATA A CATEGORIA
    while True:
        try:
            print("-" * TM)
            categoria = input('Categoria: ').strip().capitalize()
            
            caracteres_proibidos = string.punctuation + string.digits
            if any(char in caracteres_proibidos for char in categoria): # --> BARRA O USUARIO DE INSERIR CARACTERES E NUMEROS NA CATEGORIA.
                raise ValueError("A categoria deve conter apenas letras.")
            
            if len(categoria) >= 50: # --> O CAMPO CATEGORIA E LIMITADO A 50  CARACTERES.
                raise ValueError("A categoria não pode ser maior que 50 caracteres.")
            
            return categoria
            
        except ValueError as erro:
            print(f"ERRO: {erro}")


def descricao_editar_gasto(): # --> COLETA E TRATA O CAMPO DESCRIÇÃO
    while True:
        try:
            print("-" * TM)
            descricao = input("Descrição: ").strip().lower()
            
            if len(descricao) >= 500: # -->  CAMPO DESCRIÇÃO NÃO PODE TER MAIS DE 500 CARACTERES
                raise ValueError("Descrção não pode ter mais que 500 caracteres.")
            return descricao
        
        except ValueError as erro:
            print(f"ERRO: {erro}")

def data_editar_gasto(): # --> COLETA E TRATA A DATA INFORMADA PELO USUARIO
    while True:
        try:
            print("-" * TM)
            data_str = input("Data (DD/MM/AAAA): ").strip()
            
            if not data_str:
                return datetime.date.today().strftime("%d/%m/%Y")
            
            
            if len(data_str) == 8 and data_str.isdigit(): # --> TRATA DATOS SEM SEPARADORES (DDMMAAAA)
                data_str = f"{data_str[0:2]}/{data_str[2:4]}/{data_str[4:8]}"

            # --> TRATA DADOS COM OUTROS SEPARADORES
            data_limpa = data_str.replace('.', '/').replace('-', '/').replace('_', '/').replace('=', '/')

            data_valida = datetime.datetime.strptime(data_limpa, "%d/%m/%Y").date()
            
            return data_valida.strftime("%d/%m/%Y") # --> RETORNA A DATA NO FORMATO BRASILEIRO
        
        except ValueError:
            print("ERRO: Formato de data inválido ou data não existe. Por favor, use DD/MM/AAAA ou DDMMAAAA.")



def coletar_dados_edicao(): # --> essa função coleta e passa os dados para a função de editar gastos la no main
    id = id_editar_gasto()
    nome = nome_editar_gasto()
    valor = valor_editar_gasto()
    categoria = categoria_editar_gasto()
    descricao = descricao_editar_gasto()
    data = data_editar_gasto()




    return {
        "id": id,
        "nome": nome if nome else None,
        "valor": valor if valor else None,
        "categoria": categoria if categoria else None,
        "descricao": descricao if descricao else None,
        "data": data if data else None
        }




def valor_gasto_filtrar(mensagem): # --> FUNÇÃO USADA PARA COELTAR  VALORES PARA BUSCA DE GASTOS COM PERIODO DE VALOR, A MESMA RECEBE UYM STRING PARA A MENSAGEM PARA O USUARIO
    while True:
        try:
            print("-" * TM)
            valor = input(f"{mensagem}")
            valor = valor.replace(',', '.')  # --> Substitui a vírgula por ponto
            valor = Decimal(valor)
            if valor <= 0: # --> VALIDAÇÃO 1, O VALOR NÃO PODE SER MENOR OU IGUAL A ZERO.
                raise ValueError
            
            return valor
            
        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("O valor não pode ser negativo ou menor que zero.")
