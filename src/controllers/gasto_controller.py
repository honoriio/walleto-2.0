from src.repositories.gasto_repository import inserir_gasto_repository, editar_gastos_repository, buscar_gasto_por_id_repository, excluir_gastos_repository


def adicionar_gastos_controller(novo_gasto):
    resultado = inserir_gasto_repository(novo_gasto)
    return resultado



def editar_gastos_controller(dados):
    resultado = editar_gastos_repository(dados)
    return resultado


def buscar_gasto_para_exclusao_controller(id_gasto: int):
    gasto = buscar_gasto_por_id_repository(id_gasto)

    if gasto is None:
        return {
            "status": "erro",
            "mensagem": "Gasto não encontrado.",
            "gasto": None,
        }

    return {
        "status": "sucesso",
        "mensagem": "Gasto encontrado.",
        "gasto": gasto,
    }


def excluir_gasto_controller(id_gasto: int):
    return excluir_gastos_repository(id_gasto)


