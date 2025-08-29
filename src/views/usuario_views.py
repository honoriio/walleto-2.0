# Área exclusiva para importações
import re 

def nome_usuario():
     while True:
        try:
            nome = input('Nome do usuário: ').strip()
            
            if not nome: # --> VALIDAÇÃO 1, VERIFICA SE A STRING ESTA VAZIA
                raise ValueError("O nome não pode estar vazio.")
            
            if len(nome) >= 300: #-->  VALIDAÇÃO 2, O NOME NÃO PODE TER MAIS DE 40 CARACTERES
                raise ValueError("O nome não pode ter mais que 300 caracteres.")
            return nome
            
        except ValueError as erro:
            print(f"ERRO: {erro}")



def email_usuario():
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # --> PADRÃO DE CARACTERES QUE É USADO NOS EMAILS.
    while True:
        try:
            email = input("Digite o e-mail: ")

            if not email: # --> VERIFICA SE A VARIAVEK EMAIL ESTA VAZIA
                raise ValueError("O e-mail não pode estar em branco.")
            
            if re.match(padrao, email): # --> FAZ A VERIFICAÇÃO SE O EMAIL SEGUE O PADRÃO CORRETO
                print("E-mail válido!")
                return email
            else:
                print('O e-mail informado não é válido.')

        except ValueError as erro:
                print(f"ERRO: {erro}")
        
    

def sexo_usuario():
    masculino = "Masculino"
    feminino = "Feminino"
    while True:
        try:
            print("-" * 60)
            print("[1] - MASCULINO")
            print("[2] - FEMININO")
            print("-" * 60)
            escolha = int(input("opção: "))

            if escolha == 1:
                sexo = masculino
                return sexo 
            elif escolha == 2:
                sexo = feminino
                return sexo
            else:
                raise ValueError("Opção invalida.")
            
        except ValueError as erro:
            print(f"ERRO: {erro}")


def data_nascimento_usuario():
    pass