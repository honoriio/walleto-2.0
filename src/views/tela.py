# Area destinada a importação
import sys
import os
import platform
import time
from src.views.colors import cores

TM = 120

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