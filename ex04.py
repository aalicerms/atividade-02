import json

ARQUIVO_USUARIOS = "usuarios.json"

def carregar_user():
    try:
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_user(user):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(user, arquivo, indent=4)

def registrar_user(nome_user, senha):
    user = carregar_user()
    if nome_user in user:
        print("Nome de usuário já cadastrado")
    else:
        user[nome_user] = {"senha" : senha, "saldo": 0.0, "transações": []}
        salvar_user(user)
        print("Usuário registrado com sucesso")

def fazer_login(nome_user, senha):
    user = carregar_user()
    if nome_user in user and user[nome_user]["senha"] == senha:
        print("Login feito com sucesso!")
        return user[nome_user]
    else:
        print("Nome de usuário ou senha inválidos.")
        return None

def depositar(user, valor):
    if valor > 0:
        user["saldo"] += valor
        user["transações"].append(f"Deposito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido")

def sacar(user, valor):
    if valor > 0 and user["saldo"] >= valor:
        user["saldo"] -= valor
        user["transações"].append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    elif valor > 0:
        print("Saldo insuficiente")
    else:
        print("Valor inválido")

def exibir_detalhes(user):
    print(f"\nSaldo atual: R${user['saldo']:.2f}")
    print("Histórico de transações: ")
    for transacao in user["transações"]:
        print(f"- {transacao}")

def menu_principal():
    while True:
        print("\nSistema bancário")
        print("1. Registrar novo usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            registrar_user(nome, senha)
        elif opcao == "2":
            nome = input("Nome de usuário: ")
            senha = input("Senha: ")
            user = fazer_login(nome, senha)
            if user:
                while True:
                    print("\nMenu")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Exibir saldo e transações")
                    print("4. Sair")
                    opcao_user = input("Escolha uma opção: ")
                    if opcao_user == "1":
                        valor = float(input("Valor do depósito: "))
                        depositar(user, valor)
                        salvar_user(carregar_user())
                    elif opcao_user == "2":
                        valor = float(input("Valor do saque: "))
                        sacar(user, valor)
                        salvar_user(carregar_user())
                    elif opcao_user == "3":
                        exibir_detalhes(user)
                    elif opcao_user == "4":
                        print("Saindo...")
                        break
                    else:
                        print("Opção inválida")
        elif opcao == "3":
            print("Saindo...")
            break
        else: 
            print("Opção inválida")

menu_principal()
