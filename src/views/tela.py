# Area destinada a importação
import sys
import os
import platform
import time
from src.views.colors import cores
from src.models.gastos import Gasto


TM = 160

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET =  cores()

def limpar_tela():
    # Verifica o sistema operacional
    if platform.system() == "Windows":
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux/macOS



def exibir_mensagem(mensagem, cor):
    print("-" * TM)
    print(f'{cor}{mensagem}{RESET}')
    time.sleep(2)



def encerrar_programa():
    limpar_tela()
    print('=' * TM) 
    print(f'{VERMELHO}PROGRAMA ENCERRADO...{RESET}'.center(TM))
    print('=' * TM)
    time.sleep(2)
    limpar_tela()
    sys.exit()


def extrato(relatorio, saldo): #--> precisamos passar o saldo da conta na hora de chamarmos a função e a lista de transação que e retornada da função obter transações

    print("\nEXTRATO DA CONTA")
    print("-" * 30)

    for t in relatorio:
        print(f"{t['tipo']} | R${t['valor']} | {t['descricao']}")

    print("-" * 30)
    print(f"Saldo atual: R${saldo}")


def mostrar_gasto(gasto: Gasto):
    valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    print("-" * TM)
    print(
        f"ID: {gasto.id} | Nome Do Gasto: {gasto.nome} | Valor: {valor_formatado} | "
        f"Categoria: {gasto.categoria} | Descrição: {gasto.descricao} | Data: {gasto.data}"
    )
    print("-" * TM)


def exibir_gastos(gastos):
    """Recebe uma lista de gastos e imprime no terminal."""
    if not gastos:
        print("Nenhum gasto encontrado.")
        return

    for gasto in gastos:
        valor_formatado = f"R$ {gasto.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        print(
            f"ID: {gasto.id} | "
            f"Nome: {gasto.nome} | "
            f"Valor: {valor_formatado} | "
            f"Categoria: {gasto.categoria} | "
            f"Descrição: {gasto.descricao} | "
            f"Data: {gasto.data}"
        )
        print('-' * TM)