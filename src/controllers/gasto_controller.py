from src.repositories.gasto_repository import inserir_gasto_repository, editar_gastos_repository


def adicionar_gastos_controller(novo_gasto):
    resultado = inserir_gasto_repository(novo_gasto)
    return resultado



def editar_gastos_controller(dados):
    resultado = editar_gastos_repository(dados)
    return resultado