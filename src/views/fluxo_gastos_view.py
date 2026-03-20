from src.controllers.gasto_controller import adicionar_gastos_controller
from src.views.gastos_views import entrada_gastos
from src.views.menus import menu_adicionar_gastos
from src.views.tela import exibir_mensagem
from src.core.constants import VERDE_CLARO, VERMELHO_CLARO



def fluxo_adicionar_gasto():
    menu_adicionar_gastos()
    novo_gasto = entrada_gastos()
    resultado = adicionar_gastos_controller(novo_gasto)
    if resultado["status"] == "sucesso":
        exibir_mensagem(resultado["mensagem"], VERDE_CLARO)
    else:
        exibir_mensagem(resultado["mensagem"], VERMELHO_CLARO)

