from src.repositories.gasto_repository import inserir_gasto_repository, editar_gastos_repository, buscar_gasto_por_id_repository, excluir_gastos_repository, listar_gastos_repository
from src.services.relatorio_service import calcular_gastos_services
from src.infrastructure.exporters.excel_exporter import exportar_gastos_excel
from src.infrastructure.dashboard.streamlit_dashboard import painel_dashboard_em_execucao

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


def listar_gastos_controller():
    gastos = listar_gastos_repository()
    total = calcular_gastos_services(gastos)

    return {
        "gastos": gastos,
        "total": total,
    }


def exportar_gastos_controller(gastos):
    return exportar_gastos_excel(gastos)


def abrir_dashboard_controller(gastos):
    caminho_arquivo = exportar_gastos_excel(gastos)
    painel_dashboard_em_execucao(caminho_arquivo)
    return caminho_arquivo