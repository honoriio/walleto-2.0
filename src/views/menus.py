# Área destinada as importações
from colors import cores

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = cores()



def menu_principal():
    print('=' * 100)
    print(f"{VERDE}WALLETO - MENU PRINCIPAL{RESET}".center(100))
    print('=' * 100)
    print("[1] - Gerenciar Gastos")
    print("[2] - Consultar Gastos e Relatorios")
    print("[0] - Sair")
    print('-' * 100)


def menu_gerenciar_gastos():
    print('=' * 100)
    print(f"{VERDE}GERENCIAR GASTOS{RESET}".center(100))
    print('=' * 100)
    print("[1] - Adicionar Novo Gasto")
    print("[2] - Editar Gasto")
    print("[3] - Excluir Gasto")
    print("[0] - Voltar ao Menu Principal")
    print('-' * 100)


def consultas_e_relatorios():
    print('=' * 100)
    print(f"{VERDE}CONSULTAS E RELATORIOS{RESET}".center(100))
    print('=' * 100)
    print("[1] Listar Todos os Gastos")
    print("[2] Buscar Gasto por ID")
    print("[3] Filtrar por Categoria")
    print("[4] Filtrar por Data")
    print("[5] Filtrar por Valor")
    print("[9] Voltar ao Menu Principal")
    print('-' * 100)


menu_principal()
menu_gerenciar_gastos()
consultas_e_relatorios()
