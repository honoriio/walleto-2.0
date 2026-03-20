# Área destinada as importações
from src.views.gastos_views import entrada_gastos, coletar_dados_edicao, id_editar_gasto
from src.repositories.gasto_repository import  listar_gastos, excluir_gastos, buscar_gasto_por_id, filtrar_gastos_categoria, filtrar_gastos_data, filtrar_gasto_valor
from src.services.relatorio_service import calcular_gastos
from src.controllers.gasto_controller import adicionar_gastos_controller
from src.views.menus import *
from src.views.tela import encerrar_programa, exibir_mensagem, mostrar_gasto, exibir_gastos
from src.core.constants import *
from src.core.database import inicializar_banco
import time
from src.infrastructure.exporters.excel_exporter import exportar_gastos_excel
from src.infrastructure.dashboard.streamlit_dashboard import painel_dashboard_em_execucao
from src.views.fluxo_gastos_view import fluxo_adicionar_gasto, fluxo_editar_gasto



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
                        id_gasto = cabecalho_excluir_gasto()
                        gasto = buscar_gasto_por_id(id_gasto)

                        if gasto is None:
                            exibir_mensagem("Gasto não encontrado.", VERMELHO_CLARO)
                            continue
                        
                        mostrar_gasto(gasto)

                        opc = confirmar_exclusao()

                        match opc:
                            case 1: 
                                resultado = excluir_gastos(id_gasto)

                                if resultado["status"] == "sucesso":
                                    exibir_mensagem(resultado["mensagem"], VERDE_CLARO)
                                else:
                                    exibir_mensagem(resultado["mensagem"], VERMELHO_CLARO)
                            case 2:
                                exibir_mensagem("Exclusão cancelada.", AMARELO_CLARO)
                                continue
                    
                    case 0: # --> Volta para o menu anterior
                        continue # ---> usado para voltar ao menu anterior
                    
                    case _: # O "_" captura qualquer outra opção
                        print(f"{VERMELHO_CLARO}Opção inválida. Por favor, tente novamente.{RESET}")
                        time.sleep(2)

            case 2: # --> Menu de consultas e relatorios.
                opc = consultas_e_relatorios()

                match opc:
                    case 1:# --> Lista todos os gastos
                        menu_listar_gastos()
                        gastos = listar_gastos()
                        exibir_gastos(gastos)
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

                    case 2: # --> Busca gastos por ID
                        id_busca = cabecalho_buscar_por_id()
                        gastos = buscar_gasto_por_id(id_busca)
                        mostrar_gasto(gastos)
                        opc = menu_anterior() # --> Retorna ao menu anterior

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
