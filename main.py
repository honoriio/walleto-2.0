# Área destinada as importações
from src.repositories.gasto_repository import filtrar_gastos_categoria, filtrar_gastos_data, filtrar_gasto_valor
from src.views.menus import *
from src.views.tela import encerrar_programa,mostrar_gasto
from src.core.constants import *
from src.core.database import inicializar_banco
import time
from src.infrastructure.exporters.excel_exporter import exportar_gastos_excel
from src.infrastructure.dashboard.streamlit_dashboard import painel_dashboard_em_execucao
from src.views.fluxo_gastos_view import fluxo_adicionar_gasto, fluxo_editar_gasto, fluxo_excluir_gasto, fluxo_listar_gastos, fluxo_buscar_gasto_por_id



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
                        fluxo_buscar_gasto_por_id()

                    case 3: # --> Busca gastos por categoria
                        categoria_busca = menu_filtrar_categoria()
                        gastos = filtrar_gastos_categoria(categoria_busca)
                        calcular_gastos(gastos)
                        opc = menu_filtro_exportação() # --> Retorna ao menu anterior

                        match opc:
                            case 1:
                                exportar_gastos_excel(gastos)

                            case 2:
                                caminho_arquivo = exportar_gastos_excel(gastos)
                                painel_dashboard_em_execucao(caminho_arquivo)

                            case 0: # --> Volta ao menu anterior
                                continue

                    case 4: # --> Busca gastos por datas
                        data_inicio, data_final = menu_filtrar_data()
                        gastos = filtrar_gastos_data(data_inicio, data_final)
                        calcular_gastos(gastos)
                        opc = menu_filtro_exportação() # --> Retorna ao menu anterior

                        match opc:
                            case 1:
                                exportar_gastos_excel(gastos)

                            case 2:
                                caminho_arquivo = exportar_gastos_excel(gastos)
                                painel_dashboard_em_execucao(caminho_arquivo)

                            case 0: # --> Volta ao menu anterior
                                continue

                    case 5: # --> Filtra gastos por valores
                        valor_min, valor_max = menu_filtrar_valor()
                        gastos = filtrar_gasto_valor(valor_min, valor_max)
                        calcular_gastos(gastos)
                        opc = menu_filtro_exportação() # --> Retorna ao menu anterior

                        match opc:
                            case 1:
                                exportar_gastos_excel(gastos)

                            case 2:
                                caminho_arquivo = exportar_gastos_excel(gastos)
                                print(caminho_arquivo)
                                painel_dashboard_em_execucao(caminho_arquivo)
                                

                            case 0: # --> Volta ao menu anterior
                                continue

                    case 6: #--> Menu de exportação de dados
                        opc = menu_exportacao()

                        match opc:
                            case 1:
                                gastos = listar_gastos()
                                arquivo = exportar_gastos_excel(gastos)
                                print(f"{VERDE_CLARO}Exportado para{RESET} {AMARELO_CLARO}{arquivo}{RESET}")
                                time.sleep(2)
                            
                            case 2:
                                gastos = listar_gastos()
                                caminho_arquivo = exportar_gastos_excel(gastos)
                                painel_dashboard_em_execucao(caminho_arquivo)

                                pass

                            case 3:
                                pass

                            case 0:
                                continue  # ---> usado para voltar ao menu anterior

                            case _: # O "_" captura qualquer outra opção
                                print(f"{VERMELHO_CLARO}Opção inválida. Por favor, tente novamente.{RESET}")
                                time.sleep(2)

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
