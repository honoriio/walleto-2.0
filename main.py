# Área destinada as importações
from src.views.menus import *
from src.views.tela import encerrar_programa
from src.core.constants import *
from src.core.database import inicializar_banco
import time
from src.views.fluxo_gastos_view import fluxo_adicionar_gasto, fluxo_editar_gasto, fluxo_excluir_gasto, fluxo_listar_gastos, fluxo_filtrar_gasto_por_id, fluxo_filtrar_gastos_por_categoria, fluxo_filtrar_gastos_por_data, fluxo_filtrar_gastos_por_valor, fluxo_exportacao



def main():
    inicializar_banco()

    while True:
        opc = menu_principal()

        match opc:
            case 1: # -->  GERENCIAR GASTOS
                opc = menu_gerenciar_gastos()

                match opc:
                    case 1: # --> ADICIONAR GASTOS
                        fluxo_adicionar_gasto()

                    case 2: # --> EDITAR GASTOS JA CRIADOS.
                        fluxo_editar_gasto()
                        
                    case 3:# --> Exclui um gasto Ja criado
                        fluxo_excluir_gasto()

            case 2: # --> Menu de consultas e relatorios.
                opc = consultas_e_relatorios()

                match opc:
                    case 1:
                        fluxo_listar_gastos()

                    case 0:
                        continue

                    case 2: # --> Busca gastos por ID
                        fluxo_filtrar_gasto_por_id()

                    case 3: # --> Busca gastos por categoria
                        fluxo_filtrar_gastos_por_categoria()
                        
                    case 4: # --> Busca gastos por datas
                        fluxo_filtrar_gastos_por_data()

                    case 5: # --> Filtra gastos por valores
                        fluxo_filtrar_gastos_por_valor()

                    case 6: #--> Menu de exportação de dados
                        fluxo_exportacao()
                    case 0: # --> volta ao menu principal
                        continue  # ---> usado para voltar ao menu anterior

                    case _: # O "_" captura qualquer outra opção
                        print(f"{VERMELHO_CLARO}Opção inválida. Por favor, tente novamente.{RESET}")
                        time.sleep(2)

            case 0: # --> Encerra o Programa.
                encerrar_programa()

            case _: # O "_" captura qualquer outra opção
                print(f"{VERMELHO_CLARO}Opção inválida. Por favor, tente novamente.{RESET}")
                time.sleep(2)

if __name__ == "__main__":   
    main()
