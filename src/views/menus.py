# Área destinada as importações
from src.views.colors import cores
from decimal import InvalidOperation 
from src.views.tela import limpar_tela
import string
PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = cores()

TM = 120

def menu_principal():
    limpar_tela()
    print('=' * TM)
    print(f"{VERDE}WALLETO - MENU PRINCIPAL{RESET}".center(100))
    print('=' * TM)
    print("[1] - Gerenciar Gastos")
    print("[2] - Consultar Gastos e Relatorios")
    print("[0] - Sair")
    print('-' * TM)
        
    while True:
        try:
            opc_str = input("Opção: ")
            if not opc_str:
                print("Digite uma opção, o campo não pode ficar em branco.")
                continue
            opc = int(opc_str)
            return opc

        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("Digite um valor númerico.")



def menu_gerenciar_gastos():
    limpar_tela()
    print('=' * TM)
    print(f"{VERDE}GERENCIAR GASTOS{RESET}".center(100))
    print('=' * TM)
    print("[1] - Adicionar Novo Gasto")
    print("[2] - Editar Gasto")
    print("[3] - Excluir Gasto")
    print("[0] - Voltar ao Menu Principal")
    print('-' * TM)

    while True:
        try:
            opc_str = input("Opção: ")
            if not opc_str:
                print("Digite uma opção, o campo não pode ficar em branco.")
                continue
            opc = int(opc_str)
            return opc

        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("Digite um valor númerico.")



def consultas_e_relatorios():
    limpar_tela()
    print('=' * TM)
    print(f"{VERDE}CONSULTAS E RELATORIOS{RESET}".center(TM))
    print('=' * TM)
    print("[1] Listar Todos os Gastos")
    print("[2] Buscar Gasto por ID")
    print("[3] Filtrar por Categoria")
    print("[4] Filtrar por Data")
    print("[5] Filtrar por Valor")
    print("[0] Voltar ao Menu Principal")
    print('-' * TM)

    while True:
        try:
            opc_str = input("Opção: ")
            if not opc_str:
                print("Digite uma opção, o campo não pode ficar em branco.")
                continue
            opc = int(opc_str)
            return opc

        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("Digite um valor númerico.")



def menu_listar_gastos():
    limpar_tela()
    print("=" * TM)
    print(f"{VERDE}LISTA DE GASTOS{RESET}".center(120))
    print("=" * TM)

def cabecalho_excluir_gasto():
    limpar_tela() 
    print('=' * TM)
    print(f'{VERMELHO}EXCLUIR GASTOS{RESET}'.center(TM))
    print('=' * TM)

    while True:
        # Pede o dado ao usuário usando a mensagem fornecida
        entrada_usuario = input("Informe o id do gasto: ")
        
        try:
            numero = int(entrada_usuario)
            return numero
        
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros. Tente novamente.")


    
def cabecalho_buscar_por_id():
    limpar_tela() 
    print('=' * TM)
    print(f'{AZUL}BUSCA POR ID{RESET}'.center(TM))
    print('=' * TM)

    while True:
        # Pede o dado ao usuário usando a mensagem fornecida
        entrada_usuario = input("Informe o id do gasto: ")
        
        try:
            numero = int(entrada_usuario)
            return numero
        
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros. Tente novamente.")


def menu_filtrar_categoria():
    limpar_tela() 
    print('=' * TM)
    print(f'{AMARELO}BUSCA POR ID{RESET}'.center(TM))
    print('=' * TM)

    while True:
        try:
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
