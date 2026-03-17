from __future__ import annotations

import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

import pandas as pd
import streamlit as st


HOST_PADRAO = "127.0.0.1"
PORTA_PADRAO = 8501
TIMEOUT_STREAMLIT = 15
NOME_PLANILHA = "Gastos"


def formatar_moeda_brl(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def obter_pasta_logs() -> Path:
    pasta_logs = Path("logs")
    pasta_logs.mkdir(exist_ok=True)
    return pasta_logs


def obter_arquivo_log_dashboard() -> Path:
    return obter_pasta_logs() / "streamlit_dashboard.log"


def validar_colunas_obrigatorias(df: pd.DataFrame) -> None:
    colunas_obrigatorias = {"Nome", "Valor", "Categoria", "Data", "Descrição"}
    colunas_encontradas = set(df.columns)

    colunas_faltando = colunas_obrigatorias - colunas_encontradas
    if colunas_faltando:
        raise ValueError(
            "O arquivo XLSX não contém todas as colunas esperadas. "
            f"Faltando: {', '.join(sorted(colunas_faltando))}"
        )


def carregar_dados_excel(caminho_arquivo: str | Path) -> pd.DataFrame:
    caminho_arquivo = Path(caminho_arquivo)

    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo XLSX não encontrado: {caminho_arquivo}")

    df = pd.read_excel(caminho_arquivo, sheet_name=NOME_PLANILHA)
    validar_colunas_obrigatorias(df)

    df = df[df["Nome"] != "TOTAL"].copy()
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")
    df["Categoria"] = df["Categoria"].fillna("Sem categoria")
    df["Descrição"] = df["Descrição"].fillna("")

    df = df.dropna(subset=["Valor"])
    return df


def renderizar_dashboard(caminho_arquivo: str | Path | None = None) -> None:
    st.set_page_config(page_title="Walleto Dashboard", layout="wide")
    st.title("Dashboard Financeiro - Walleto")

    if caminho_arquivo is None:
        st.info("Nenhum arquivo XLSX foi informado.")
        st.info("Abra o dashboard passando um arquivo exportado pelo Walleto.")
        return

    caminho_arquivo = Path(caminho_arquivo)

    if not caminho_arquivo.exists():
        st.error(f"Arquivo não encontrado: {caminho_arquivo}")
        return

    try:
        df = carregar_dados_excel(caminho_arquivo)
    except Exception as erro:
        st.error(f"Erro ao carregar o arquivo Excel: {erro}")
        return

    if df.empty:
        st.warning("O arquivo foi carregado, mas não há dados para exibir.")
        return

    col_filtro1, col_filtro2 = st.columns(2)

    categorias = sorted(df["Categoria"].dropna().unique().tolist())
    categoria_selecionada = col_filtro1.multiselect(
        "Filtrar por categoria",
        options=categorias,
        default=categorias,
    )

    data_min = df["Data"].min()
    data_max = df["Data"].max()

    intervalo_datas = col_filtro2.date_input(
        "Filtrar por período",
        value=(data_min, data_max),
    )

    df_filtrado = df[df["Categoria"].isin(categoria_selecionada)].copy()

    if isinstance(intervalo_datas, tuple) and len(intervalo_datas) == 2:
        data_inicio = pd.to_datetime(intervalo_datas[0])
        data_fim = pd.to_datetime(intervalo_datas[1])

        df_filtrado = df_filtrado[
            (df_filtrado["Data"] >= data_inicio) &
            (df_filtrado["Data"] <= data_fim)
        ]

    total_gasto = df_filtrado["Valor"].sum()
    quantidade_gastos = len(df_filtrado)
    ticket_medio = df_filtrado["Valor"].mean() if quantidade_gastos > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("Total gasto", formatar_moeda_brl(total_gasto))
    col2.metric("Quantidade de gastos", quantidade_gastos)
    col3.metric("Ticket médio", formatar_moeda_brl(ticket_medio))

    st.divider()

    st.subheader("Gastos por categoria")
    gastos_categoria = (
        df_filtrado.groupby("Categoria", as_index=False)["Valor"]
        .sum()
        .sort_values("Valor", ascending=False)
    )

    if not gastos_categoria.empty:
        st.bar_chart(gastos_categoria.set_index("Categoria"))
    else:
        st.info("Nenhum dado para exibir no gráfico de categorias.")

    st.subheader("Gastos por mês")
    df_filtrado["Mes"] = df_filtrado["Data"].dt.to_period("M").astype(str)

    gastos_mes = (
        df_filtrado.groupby("Mes", as_index=False)["Valor"]
        .sum()
        .sort_values("Mes")
    )

    if not gastos_mes.empty:
        st.line_chart(gastos_mes.set_index("Mes"))
    else:
        st.info("Nenhum dado para exibir no gráfico mensal.")

    st.subheader("Últimos gastos")
    df_exibicao = df_filtrado.sort_values("Data", ascending=False).copy()
    df_exibicao["Data"] = df_exibicao["Data"].dt.strftime("%d/%m/%Y")
    df_exibicao["Valor"] = df_exibicao["Valor"].apply(formatar_moeda_brl)

    st.dataframe(df_exibicao, width="stretch")


def obter_arquivo_por_argumento() -> str | None:
    if len(sys.argv) > 1:
        return sys.argv[-1]
    return None


def porta_esta_ativa(host: str, porta: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        return sock.connect_ex((host, porta)) == 0


def esperar_streamlit(
    host: str = HOST_PADRAO,
    porta: int = PORTA_PADRAO,
    timeout: int = TIMEOUT_STREAMLIT,
) -> bool:
    inicio = time.time()

    while time.time() - inicio < timeout:
        if porta_esta_ativa(host, porta):
            return True
        time.sleep(0.5)

    return False


def obter_caminho_script_dashboard(caminho_script: str | Path | None = None) -> Path:
    if caminho_script is None:
        return Path(__file__).resolve()
    return Path(caminho_script).resolve()


def abrir_dashboard(
    caminho_arquivo: str | Path,
    caminho_script: str | Path | None = None,
    porta: int = PORTA_PADRAO,
    abrir_navegador: bool = True,
) -> tuple[subprocess.Popen, str]:
    caminho_arquivo = Path(caminho_arquivo).resolve()
    caminho_script_resolvido = obter_caminho_script_dashboard(caminho_script)

    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo XLSX não encontrado: {caminho_arquivo}")

    if not caminho_script_resolvido.exists():
        raise FileNotFoundError(
            f"Script do dashboard não encontrado: {caminho_script_resolvido}"
        )

    url = f"http://localhost:{porta}"
    caminho_log = obter_arquivo_log_dashboard()

    arquivo_log = open(caminho_log, "a", encoding="utf-8")

    processo = subprocess.Popen(
        [
            "streamlit",
            "run",
            str(caminho_script_resolvido),
            "--server.address",
            HOST_PADRAO,
            "--server.port",
            str(porta),
            "--",
            str(caminho_arquivo),
        ],
        stdout=arquivo_log,
        stderr=arquivo_log,
    )

    pronto = esperar_streamlit(porta=porta)

    if not pronto:
        processo.terminate()
        raise RuntimeError(
            "O dashboard não iniciou a tempo. "
            "Verifique se o Streamlit está instalado, se a porta está livre "
            f"e consulte o log em: {caminho_log}"
        )

    if abrir_navegador:
        try:
            webbrowser.open(url)
        except Exception:
            pass

    return processo, url


def encerrar_processo(processo: subprocess.Popen) -> None:
    if processo.poll() is not None:
        return

    processo.terminate()

    try:
        processo.wait(timeout=5)
    except subprocess.TimeoutExpired:
        processo.kill()


def painel_dashboard_em_execucao(
    caminho_arquivo: str | Path,
    caminho_script: str | Path | None = None,
    porta: int = PORTA_PADRAO,
    abrir_navegador: bool = True,
) -> None:
    try:
        processo, url = abrir_dashboard(
            caminho_arquivo=caminho_arquivo,
            caminho_script=caminho_script,
            porta=porta,
            abrir_navegador=abrir_navegador,
        )
    except Exception as erro:
        print("\nErro ao abrir o dashboard.")
        print(f"Detalhes: {erro}")
        print(f"Log: {obter_arquivo_log_dashboard()}")
        input("\nPressione Enter para voltar...")
        return

    while True:
        print("\n" + "=" * 70)
        print("DASHBOARD EM EXECUÇÃO")
        print("=" * 70)
        print(f"Arquivo base : {Path(caminho_arquivo).resolve()}")
        print(f"Link         : {url}")
        print(f"Log          : {obter_arquivo_log_dashboard().resolve()}")
        print("\n[1] Abrir dashboard no navegador")
        print("[2] Voltar ao menu anterior")
        print("[3] Encerrar dashboard e voltar")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            try:
                webbrowser.open(url)
                print("\nAbrindo dashboard no navegador...")
            except Exception as erro:
                print(f"\nNão foi possível abrir o navegador automaticamente: {erro}")
                print(f"Acesse manualmente: {url}")

        elif opcao == "2":
            print("\nVoltando ao menu anterior...")
            print("O dashboard continuará rodando em segundo plano.")
            time.sleep(1.5)
            break

        elif opcao == "3":
            print("\nEncerrando dashboard...")
            encerrar_processo(processo)
            print("Dashboard encerrado com sucesso.")
            time.sleep(1.5)
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    arquivo_xlsx = obter_arquivo_por_argumento()
    renderizar_dashboard(arquivo_xlsx)