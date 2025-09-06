# Área destinada as importações
from src.views.gastos_views import entrada_gastos, coletar_dados_edicao
from src.views.usuario_views import nome_usuario, email_usuario, sexo_usuario, data_nascimento_usuario
from src.models.gastos import criar_tabela, inserir_gasto, listar_gastos, editar_gastos, excluir_gastos, buscar_gasto_por_id, filtrar_gastos_categoria, Gasto
from src.views.menus import menu_principal, menu_gerenciar_gastos, consultas_e_relatorios, menu_listar_gastos, cabecalho_excluir_gasto, cabecalho_buscar_por_id, menu_filtrar_categoria
from src.views.tela import encerrar_programa, limpar_tela, exibir_mensagem
import time
from src.views.colors import cores


PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET =  cores()


def main():
    criar_tabela()

    time.sleep(0.2)
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
                            time.sleep(10)

                    case 3:
                        id_gasto = cabecalho_excluir_gasto()
                        resultado = excluir_gastos(id_gasto)

                        if resultado["status"] == "sucesso":
                            exibir_mensagem(resultado["mensagem"], VERDE)
                        else:
                            exibir_mensagem(resultado["mensagem"], VERMELHO)
                            time.sleep(10)     

                    case 0:
                        continue

            case 2:
                opc = consultas_e_relatorios()
                match opc:
                    case 1:
                        menu_listar_gastos()
                        listar_gastos()
                        time.sleep(15)
                    
                    case 2:
                        id_busca = cabecalho_buscar_por_id()
                        buscar_gasto_por_id(id_busca)
                        time.sleep(5) # -->CRIAR A LOGICA PARA NÃO TER QUE USAR TIME

                    case 3:
                        categoria_busca = menu_filtrar_categoria()
                        filtrar_gastos_categoria(categoria_busca)
                        time.sleep(5) # --> CRIAR A LOGICA PARA NÃO TER QUE USAR TIME

                    case 4:
                        pass

                    case 5:
                        pass

                    case 0:
                        continue

            case 0:
                encerrar_programa()





if __name__ == "__main__":   
    main()