import pytest
from decimal import Decimal, InvalidOperation
from src.views.gastos_views import *

# ----------------- Teste de coleta de nome do gasto-------------------

def test_nome_gasto_valido(monkeypatch):
    # Simula um input válido diretamente
    monkeypatch.setattr('builtins.input', lambda _: "Aluguel")
    resultado = nome_gasto()
    assert resultado == "Aluguel"

def test_nome_gasto_vazio_ou_muito_longo(monkeypatch):
    # Simula uma sequência de inputs: primeiro vazio, depois muito longo, por fim válido
    entradas = ["", "A" * 50, "Supermercado"]
    iter_entradas = iter(entradas)
    
    monkeypatch.setattr('builtins.input', lambda _: next(iter_entradas))
    
    resultado = nome_gasto()
    # Deve retornar apenas o nome válido no final
    assert resultado == "Supermercado"

# ----------------- Teste de coleta do valor do gasto-------------------

def test_valor_gasto(monkeypatch):
    # Vai simular um input valido de primeira 
    monkeypatch.setattr('builtins.input', lambda _: "10,50")
    resultado = valor_gasto()
    assert resultado == Decimal("10.50")


def testar_valor_gasto_negaivo_ou_zero(monkeypatch):
    # Simula a senguencia: valor negativo, zero e por fim valido
    entradas = ["-5", "0", "100,25"]
    iter_entradas = iter(entradas)

    monkeypatch.setattr("builtins.input", lambda _: next(iter_entradas))

    resultado = valor_gasto()
    # o mesmo retorna apenas o valor valido
    assert resultado == Decimal("100.25")


def test_valor_gasto_texto_invalido(monkeypatch):
    # Simnula uma seguencia: texto invalido, depois valido.
    entradas = ["abc", "50,75"]
    iter_entradas = iter(entradas)

    monkeypatch.setattr("builtins.input", lambda _: next(iter_entradas))

    resuultado = valor_gasto()
    assert resuultado == Decimal("50.75")
