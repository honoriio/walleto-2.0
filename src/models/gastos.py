# área destinada as importaçoes

class Gasto:
#Representa um gasto e contém as regras de negócio e a lógica de persistência.  
    def __init__(self, nome, valor, categoria, descricao, data, id=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.data = data


class Usuario:
    def __init__(self, nome, email, sexo=None,idade=None, id=None):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.idade = idade
        self.id = id
        self.senha_hash = None

        
        