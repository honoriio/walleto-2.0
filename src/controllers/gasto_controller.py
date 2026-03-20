from src.repositories.gasto_repository import inserir_gasto


def adicionar_gastos_controller(novo_gasto):
    resultado = inserir_gasto(novo_gasto)
    return resultado
