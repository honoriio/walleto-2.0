import pytest
from decimal import Decimal, InvalidOperation
from src.views.gastos_views import *

# ----------------- Teste de coleta de nome do gasto-------------------

def test_nome_gasto_valido(simular_input):
    # Simula um input válido diretamente
    simular_input(["Aluguel"])

    resultado = nome_gasto()
    assert resultado == "Aluguel"

def test_nome_gasto_vazio_ou_muito_longo(simular_input):
    # Simula uma sequência de inputs: primeiro vazio, depois muito longo, por fim válido
    simular_input(["", "A" * 50, "Supermercado"])
    
    resultado = nome_gasto()
    # Deve retornar apenas o nome válido no final
    assert resultado == "Supermercado"

# ----------------- Teste de coleta do valor do gasto-------------------

def test_valor_gasto(simular_input):
    # Vai simular um input valido de primeira 
    simular_input(["10.50"])

    resultado = valor_gasto()
    assert resultado == Decimal("10.50")


def test_valor_gasto_negaivo_ou_zero(simular_input):
    # Simula a senguencia: valor negativo, zero e por fim valido
    simular_input(["-5", "0", "100,25"])
   
    resultado = valor_gasto()
    # o mesmo retorna apenas o valor valido
    assert resultado == Decimal("100.25")


def test_valor_gasto_texto_invalido(simular_input):
    # Simnula uma seguencia: texto invalido, depois valido.
    simular_input(["abc", "50,75"])

    resultado = valor_gasto()
    assert resultado == Decimal("50.75")


# ----------------- Teste de coleta da categoria do gasto-------------------------

def test_categoria_gasto_valida(simular_input):
    # Testa primeiro uma entrada valida
    simular_input(["Alimentação"])

    resultado = categoria_gasto()
    assert resultado == "Alimentação"


def test_categoria_gasto_numero_invalido(simular_input):
    # Simula primeiro uma entrada valida
    simular_input(["123456", "Alimentação"])

    resultado = categoria_gasto()
    assert resultado == "Alimentação"


def test_categoria_gasto_caracter_invalido(simular_input):
    # Simula primieiro uma entrada de caracteres invalidos, depois uma entrada valida.
    simular_input(["@#$%¨&*", "Alimentação"])

    resultado = categoria_gasto()
    assert resultado == "Alimentação"


def test_categoria_gasto_tamanho_invalido(simular_input):
    # Simula primiero uma entrada com tamanho excedido e depois uma entrada com tamanho valido.
    simular_input(["mingau" * 60, "Alimentação"])

    resultado = categoria_gasto()
    assert resultado == "Alimentação"

# ----------------- Teste de coleta da descrição do gasto-------------------------------
 
def test_descricao_gasto_valida(simular_input):
    #Insire um input valido de primeira.
    simular_input(["Compra de comida no restaurante", "@#!$"])

    resultado = descricao_gasto()
    assert resultado == "Compra de comida no restaurante"

def test_descricao_gasto_limite_caracter(simular_input):
    # Insiri um input com mais caracteres do que o permitido, depois inserimos um input valido
    simular_input(["A" * 350, "Compra de comida no restaurante"])

    resultado = descricao_gasto()
    assert resultado == "Compra de comida no restaurante"
    

def test_descricao_gasto_descricao_automatica(simular_input):
    # Não inseri um input, e verifica se o programa adicionol uma descrção automatica
    simular_input([" "])

    resultado = descricao_gasto()
    assert resultado == "Descrição não informada pelo usuario"

# ----------------- Teste de coleta da data do gasto-------------------------------

