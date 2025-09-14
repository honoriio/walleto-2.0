# Área destinada as importações
from src.views.gastos_views import entrada_gastos, coletar_dados_edicao, id_editar_gasto
from src.views.usuario_views import nome_usuario, email_usuario, sexo_usuario, data_nascimento_usuario
from src.models.gastos import criar_tabela, inserir_gasto, listar_gastos, editar_gastos, excluir_gastos, buscar_gasto_por_id, filtrar_gastos_categoria, filtrar_gastos_data, filtrar_gasto_valor, calcular_gastos, Gasto
from src.views.menus import *
from src.views.tela import encerrar_programa, exibir_mensagem
from src.views.colors import cores
import time


PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET =  cores()


def main():
    criar_tabela()

    while True:
        opc = menu_principal()

        match opc:
            case 1: # -->  GERENCIAR GASTOS
                opc = menu_gerenciar_gastos()

                match opc:
                    case 1: # --> ADICIONAR GASTOS
                        menu_adicionar_gastos()
                        novo_gasto  = entrada_gastos()
                        resultado = inserir_gasto(novo_gasto)
                        if resultado["status"] == "sucesso":
                            exibir_mensagem(resultado["mensagem"], VERDE)
                        else:
                            exibir_mensagem(resultado["mensagem"], VERMELHO)

                    case 2: # --> EDITAR GASTOS JA CRIADOS.
                        menu_editar_gasto()
                        dados = coletar_dados_edicao()
                        resultado = editar_gastos(dados)

                        if resultado["status"] == "sucesso":
                            exibir_mensagem(resultado["mensagem"], VERDE)
                        else:
                            exibir_mensagem(resultado["mensagem"], VERMELHO)
                            menu_anterior() # --> Retorna ao menu anterior

                    case 3:# --> Exclui um gasto Ja criado
                        id_gasto = cabecalho_excluir_gasto()
                        resultado = excluir_gastos(id_gasto)

                        if resultado["status"] == "sucesso":
                            exibir_mensagem(resultado["mensagem"], VERDE)
                        else:
                            exibir_mensagem(resultado["mensagem"], VERMELHO)
                            menu_anterior() # --> Retorna ao menu anterior
                    
                    case 0: # --> Volta para o menu anterior
                        continue # ---> usado para voltar ao menu anterior
                    
                    case _: # O "_" captura qualquer outra opção
                        print(f"{VERMELHO}Opção inválida. Por favor, tente novamente.{RESET}")
                        time.sleep(2)

            case 2: # --> Menu de consultas e relatorios.
                opc = consultas_e_relatorios()

                match opc:
                    case 1:# --> Lista todos os gastos
                        menu_listar_gastos()
                        gasto = listar_gastos()
                        calcular_gastos(gasto)
                        menu_anterior() # --> Retorna ao menu anterior
                    
                    case 2: # --> Busca gastos por ID
                        id_busca = cabecalho_buscar_por_id()
                        buscar_gasto_por_id(id_busca)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 3: # --> Busca gastos por categoria
                        categoria_busca = menu_filtrar_categoria()
                        gasto = filtrar_gastos_categoria(categoria_busca)
                        calcular_gastos(gasto)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 4: # --> Busca gastos por datas
                        data_inicio, data_final = menu_filtrar_data()
                        gasto = filtrar_gastos_data(data_inicio, data_final)
                        calcular_gastos(gasto)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 5: # --> Filtra gastos por valores
                        valor_min, valor_max = menu_filtrar_valor()
                        gasto = filtrar_gasto_valor(valor_min, valor_max)
                        calcular_gastos(gasto)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 0: # --> volta ao menu principal
                        continue  # ---> usado para voltar ao menu anterior
 
                    case _: # O "_" captura qualquer outra opção
                        print(f"{VERMELHO}Opção inválida. Por favor, tente novamente.{RESET}")
                        time.sleep(2)

            case 0: # --> Encerra o Programa.
                encerrar_programa()

            case _: # O "_" captura qualquer outra opção
                print(f"{VERMELHO}Opção inválida. Por favor, tente novamente.{RESET}")
                time.sleep(2)

if __name__ == "__main__":   
    main()
