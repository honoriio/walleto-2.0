import pytest
from src.views.gastos_views import *


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

