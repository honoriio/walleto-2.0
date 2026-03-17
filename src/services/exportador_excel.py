from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime
from tqdm import tqdm
import os


def exportar_gastos_excel(gastos):
    workbook = Workbook()
    pagina = workbook.active
    pagina.title = "Gastos"

    cabecalhos = ["Data", "Nome", "Descrição", "Categoria", "Valor"]
    pagina.append(cabecalhos)

    # Negrito no cabeçalho
    for celula in pagina[1]:
        celula.font = Font(bold=True)

    meses = []

    for gasto in tqdm(
        gastos,
        desc="Exportando gastos",
        unit="gasto",
        ncols=160
    ):
        # suporte tanto dict quanto objeto
        if isinstance(gasto, dict):
            data = gasto.get("data", "")
            nome = gasto.get("nome", "")
            descricao = gasto.get("descricao", "")
            categoria = gasto.get("categoria", "")
            valor = gasto.get("valor", 0)
        else:
            data = gasto.data
            nome = gasto.nome
            descricao = gasto.descricao
            categoria = gasto.categoria
            valor = gasto.valor

        # pegar mês
        try:
            data_obj = datetime.strptime(data, "%Y-%m-%d")
            meses.append(data_obj.strftime("%B"))
        except ValueError:
            pass

        pagina.append([data, nome, descricao, categoria, valor])

    # Formatar valores
    for linha in pagina.iter_rows(min_row=2, min_col=5, max_col=5):
        for celula in linha:
            celula.number_format = 'R$ #,##0.00'

    # Largura
    pagina.column_dimensions["A"].width = 15
    pagina.column_dimensions["B"].width = 20
    pagina.column_dimensions["C"].width = 30
    pagina.column_dimensions["D"].width = 20
    pagina.column_dimensions["E"].width = 15

    # definir mês principal
    mes_nome = meses[0] if meses else "sem_mes"

    # caminho para Documentos
    pasta_documentos = os.path.expanduser("~/Documentos")

    # cria pasta se não existir
    os.makedirs(pasta_documentos, exist_ok=True)

    # nome final do arquivo
    nome_arquivo = f"despesas_{mes_nome}.xlsx"
    caminho_completo = os.path.join(pasta_documentos, nome_arquivo)

    workbook.save(caminho_completo)

    return caminho_completo

