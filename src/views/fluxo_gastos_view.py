from src.controllers.gasto_controller import adicionar_gastos_controller, editar_gastos_controller, buscar_gasto_para_exclusao_controller, excluir_gasto_controller, listar_gastos_controller, exportar_gastos_controller, abrir_dashboard_controller
from src.views.gastos_views import coletar_dados_edicao, entrada_gastos
from src.views.menus import menu_adicionar_gastos, menu_editar_gasto, menu_anterior, cabecalho_excluir_gasto, confirmar_exclusao, menu_listar_gastos, menu_filtro_exportação
from src.views.tela import exibir_mensagem, mostrar_gasto, exibir_gastos, exibir_total
from src.core.constants import VERDE_CLARO, VERMELHO_CLARO, AMARELO_CLARO



def fluxo_adicionar_gasto():
    menu_adicionar_gastos()
    novo_gasto = entrada_gastos()
    resultado = adicionar_gastos_controller(novo_gasto)
    if resultado["status"] == "sucesso":
        exibir_mensagem(resultado["mensagem"], VERDE_CLARO)
    else:
        exibir_mensagem(resultado["mensagem"], VERMELHO_CLARO)



def fluxo_editar_gasto():
    menu_editar_gasto()
    dados = coletar_dados_edicao()
    resultado = editar_gastos_controller(dados)
    if resultado["status"] == "sucesso":
        exibir_mensagem(resultado["mensagem"], VERDE_CLARO)
    else:
        exibir_mensagem(resultado["mensagem"], VERMELHO_CLARO)
        menu_anterior() # --> Retorna ao menu anterior


def fluxo_excluir_gasto():
    id_gasto = cabecalho_excluir_gasto()

    resultado_busca = buscar_gasto_para_exclusao_controller(id_gasto)

    if resultado_busca["status"] == "erro":
        exibir_mensagem(resultado_busca["mensagem"], VERMELHO_CLARO)
        return

    mostrar_gasto(resultado_busca["gasto"])

    opc = confirmar_exclusao()

    match opc:
        case 1:
            resultado_exclusao = excluir_gasto_controller(id_gasto)

            if resultado_exclusao["status"] == "sucesso":
                exibir_mensagem(resultado_exclusao["mensagem"], VERDE_CLARO)
            else:
                exibir_mensagem(resultado_exclusao["mensagem"], VERMELHO_CLARO)

        case 2:
            exibir_mensagem("Exclusão cancelada.", AMARELO_CLARO)
            return
            

def fluxo_listar_gastos():
    menu_listar_gastos()

    resultado = listar_gastos_controller()
    gastos = resultado["gastos"]
    total = resultado["total"]

    exibir_gastos(gastos)
    exibir_total(total)

    opc = menu_filtro_exportação()

    match opc:
        case 1:
            exportar_gastos_controller(gastos)

        case 2:
            abrir_dashboard_controller(gastos)

        case 0:
            return

            