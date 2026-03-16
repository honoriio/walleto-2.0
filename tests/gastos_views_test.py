from decimal import Decimal
from src.views.gastos_views import nome_gasto, valor_gasto, categoria_gasto, descricao_gasto, data_gasto, entrada_gastos
import datetime


#======================================================================================================================
#------------------------------------- Teste de coleta do Nome do gasto -----------------------------------------------
#======================================================================================================================

class TestColetaCriacaoGasto:

    def test_nome_gasto_valido(self, simular_input):
        # Simula um input válido diretamente
        simular_input(["Aluguel"])

        resultado = nome_gasto()
        assert resultado == "Aluguel"

    def test_nome_gasto_vazio_ou_muito_longo(self, simular_input):
        # Simula uma sequência de inputs: primeiro vazio, depois muito longo, por fim válido
        simular_input(["", "A" * 50, "Supermercado"])
    
        resultado = nome_gasto()
        # Deve retornar apenas o nome válido no final
        assert resultado == "Supermercado"

#======================================================================================================================
#------------------------------------- Teste de coleta do Valor do gasto ----------------------------------------------
#======================================================================================================================

    def test_valor_gasto(self, simular_input):
        # Vai simular um input valido de primeira 
        simular_input(["10.50"])

        resultado = valor_gasto()
        assert resultado == Decimal("10.50")


    def test_valor_gasto_negativo_ou_zero(self, simular_input):
        # Simula a senguencia: valor negativo, zero e por fim valido
        simular_input(["-5", "0", "100,25"])
   
        resultado = valor_gasto()
        # o mesmo retorna apenas o valor valido
        assert resultado == Decimal("100.25")


    def test_valor_gasto_texto_invalido(self, simular_input):
        # Simnula uma seguencia: texto invalido, depois valido.
        simular_input(["abc", "50,75"])

        resultado = valor_gasto()
        assert resultado == Decimal("50.75")


#======================================================================================================================
#------------------------------------- Teste de coleta da Categoria do gasto ------------------------------------------
#======================================================================================================================

    def test_categoria_gasto_valida(self, simular_input):
        # Testa primeiro uma entrada valida
        simular_input(["Alimentação"])

        resultado = categoria_gasto()
        assert resultado == "Alimentação"


    def test_categoria_gasto_numero_invalido(self, simular_input):
        # Simula primeiro uma entrada valida
        simular_input(["123456", "Alimentação"])

        resultado = categoria_gasto()
        assert resultado == "Alimentação"


    def test_categoria_gasto_caracter_invalido(self, simular_input):
        # Simula primieiro uma entrada de caracteres invalidos, depois uma entrada valida.
        simular_input(["@#$%¨&*", "Alimentação"])

        resultado = categoria_gasto()
        assert resultado == "Alimentação"


    def test_categoria_gasto_tamanho_invalido(self, simular_input):
        # Simula primiero uma entrada com tamanho excedido e depois uma entrada com tamanho valido.
        simular_input(["mingau" * 60, "Alimentação"])

        resultado = categoria_gasto()
        assert resultado == "Alimentação"

#======================================================================================================================
#------------------------------------- Teste de coleta da descrição do gasto ------------------------------------------
#======================================================================================================================
 
    def test_descricao_gasto_valida(self, simular_input):
        #Insire um input valido de primeira.
        simular_input(["Compra de comida no restaurante @#!$"])

        resultado = descricao_gasto()
        assert resultado == "Compra de comida no restaurante @#!$"

    def test_descricao_gasto_limite_caracter(self, simular_input):
        # Insiri um input com mais caracteres do que o permitido, depois inserimos um input valido
        simular_input(["A" * 350, "Compra de comida no restaurante"])

        resultado = descricao_gasto()
        assert resultado == "Compra de comida no restaurante"
    

    def test_descricao_gasto_descricao_automatica(self, simular_input):
        # Não inseri um input, e verifica se o programa adicionol uma descrção automatica
        simular_input([" "])

        resultado = descricao_gasto()
        assert resultado == "Descrição não informada pelo usuario"

#======================================================================================================================
#------------------------------------- Teste de coleta de data do gasto -----------------------------------------------
#======================================================================================================================


    def test_data_do_gasto_entrada_valida(self, simular_input):
        # ira inserir uma entrada valida de data.
        simular_input(["16/03/2026"])

        resultado = data_gasto()
        assert resultado == "16/03/2026"


    def test_data_do_gasto_entrada_vazia_invalida(self, simular_input):
        # Ira inserir uma entrada vazia, a fim de, testar se a mesma retornara a data atual como na funçãoi.
        data_atual = datetime.date.today().strftime("%d/%m/%Y")
        simular_input([""])

        resultado = data_gasto()
        assert resultado == data_atual


    def test_data_do_gasto_sem_separadores(self, simular_input):
        # Ira inserir uma data sem separadores para testar o tratamento da mesma.
        simular_input(["16032026"])

        resultado = data_gasto()
        assert resultado == "16/03/2026"


    def test_data_do_gasto_separadores_diferentes(self, simular_input):
        #Ira inserir uma data com separadores diferentes para tratar a substituição dos mesmo pela função
        simular_input(["16,03,2026"])

        resultado = data_gasto()
        assert resultado == "16/03/2026"


    def test_data_do_gasto_em_invalido_em_outro_formato(self, simular_input):
        # Primeiro ira inserir um valor invalido de data e em seguida ira inserir um valor valido de data.
        simular_input(["2026/08/24", "16/03/2026"])

        resultado = data_gasto()
        assert resultado == "16/03/2026"


    def test_entrada_gastos_cria_objeto_gasto_corretamente(self, mocker):

        mocker.patch("src.views.gastos_views.nome_gasto", return_value="Mercado")
        mocker.patch("src.views.gastos_views.valor_gasto", return_value=Decimal("50.00"))
        mocker.patch("src.views.gastos_views.categoria_gasto", return_value="Alimentação")
        mocker.patch("src.views.gastos_views.descricao_gasto", return_value="Compra do mês")
        mocker.patch("src.views.gastos_views.data_gasto", return_value="16/03/2026")

        gasto_mock = mocker.patch("src.views.gastos_views.Gasto")

        resultado = entrada_gastos()

        gasto_mock.assert_called_once_with(
            "Mercado",
            Decimal("50.00"),
            "Alimentação",
            "Compra do mês",
            "16/03/2026"
        )

        assert resultado == gasto_mock.return_value

#======================================================================================================================
#--------------------------------- Teste de coleta de dados para edição de gasto --------------------------------------
#======================================================================================================================

#class TestColetaEdicaoGasto: