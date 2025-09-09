# Área destinada as importações
from src.views.gastos_views import entrada_gastos, coletar_dados_edicao
from src.views.usuario_views import nome_usuario, email_usuario, sexo_usuario, data_nascimento_usuario
from src.models.gastos import criar_tabela, inserir_gasto, listar_gastos, editar_gastos, excluir_gastos, buscar_gasto_por_id, filtrar_gastos_categoria, filtrar_gastos_data, filtrar_gasto_valor, Gasto
from src.views.menus import menu_principal, menu_gerenciar_gastos, consultas_e_relatorios, menu_listar_gastos, cabecalho_excluir_gasto, cabecalho_buscar_por_id, menu_filtrar_categoria, menu_filtrar_data, menu_filtrar_valor, menu_anterior
from src.views.tela import encerrar_programa, limpar_tela, exibir_mensagem
from src.views.colors import cores


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
                        novo_gasto  = entrada_gastos()
                        resultado = inserir_gasto(novo_gasto)
                        if resultado["status"] == "sucesso":
                            exibir_mensagem(resultado["mensagem"], VERDE)
                        else:
                            exibir_mensagem(resultado["mensagem"], VERMELHO)

                    case 2: # --> EDITAR GASTOS JA CRIADOS.
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
                        continue

            case 2: # --> Menu de consultas e relatorios.
                opc = consultas_e_relatorios()

                match opc:
                    case 1:# --> Lista todos os gastos
                        menu_listar_gastos()
                        listar_gastos()
                        menu_anterior() # --> Retorna ao menu anterior
                    
                    case 2: # --> Busca gastos por ID
                        id_busca = cabecalho_buscar_por_id()
                        buscar_gasto_por_id(id_busca)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 3: # --> Busca gastos por categoria
                        categoria_busca = menu_filtrar_categoria()
                        filtrar_gastos_categoria(categoria_busca)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 4: # --> Busca gastos por datas
                        data_inicio, data_final = menu_filtrar_data()
                        filtrar_gastos_data(data_inicio, data_final)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 5: # --> Filtra gastos por valores
                        valor_min, valor_max = menu_filtrar_valor()
                        filtrar_gasto_valor(valor_min, valor_max)
                        menu_anterior() # --> Retorna ao menu anterior

                    case 0: # --> volta ao menu principal
                        continue

            case 0: # --> Encerra o Programa.
                encerrar_programa()

if __name__ == "__main__":   
    main()
