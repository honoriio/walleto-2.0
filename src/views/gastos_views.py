# área destinada as importações
from decimal import Decimal, InvalidOperation   

def nome_gasto():
    while True:
        try:
            nome = input('Nome do gasto: ').strip()
            
            if not nome: # --> Validação 1, O nome não pode estar vazio
                raise ValueError("O nome não pode estar vazio.")
            
            if len(nome) > 40: #-->  Validação 2, O nome não pode ter mais que 40 caracteres.
                raise ValueError("O nome não pode ter mais que 40 caracteres.")
            return nome
            
        except ValueError as erro:
            print(f"ERRO: {erro}")


def valor_gasto(): # --> Função que coleta e valida o valor do gasto inserido pelo usuario.
    while True:
        try:
            valor = input("Valor R$: ") #-->  corrigir o mesmo pois gera erro ao usar virgula como separador.
            valor = valor.replace(',', '.')  # --> Substitui a vírgula por ponto
            valor = Decimal(valor)
            if valor <= 0: # --> Validação 1, o valor não pode ser menor que zero.
                raise ValueError
            
            return valor
            
        except InvalidOperation:
            print("Por favor, informe um valor numérico válido (ex: 10,50 ou 100).")

        except ValueError:
            print("O valor não pode ser negativo ou menor que zero.")
            
        