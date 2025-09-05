# Área destinada as importações
from src.views.gastos_views import entrada_gastos
from src.views.usuario_views import nome_usuario, email_usuario, sexo_usuario, data_nascimento_usuario
from src.models.gastos import criar_tabela, inserir_gasto, listar_gastos, editar_gastos, Gasto
from src.views.menus import menu_principal, menu_gerenciar_gastos, consultas_e_relatorios
from src.views.tela import encerrar_programa, limpar_tela, exibir_mensagem
from time import time
from src.views.colors import cores

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET =  cores()


def main():
    criar_tabela()
    
    opc = menu_principal()
    match opc:
        case 1: # -->  GERENCIAR GASTOS
            opc = menu_gerenciar_gastos()

            match opc:
                case 1: # --> ADICIONAR GASTOS
                    novo_gasto  = entrada_gastos()
                    resultado = inserir_gasto(novo_gasto)
                    if resultado["status"] == "sucesso":
                        exibir_mensagem(resultado["mensagem"], VERDE)
                    else:
                        exibir_mensagem(resultado["mensagem"], VERMELHO)

                case 2: # --> EDITAR GASTOS JA CRIADOS.
                    editar_gastos()
                    
        case 2:
            opc = consultas_e_relatorios()
            match opc:
                case 1:
                    listar_gastos()

        case 0:
            encerrar_programa()





if __name__ == "__main__":   
    main()