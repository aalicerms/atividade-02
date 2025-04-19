import json

ARQUIVO_CONTATO = "contatos.json"
def carregar_contatos():
    try:
        with open(ARQUIVO_CONTATO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_contato(contatos):
    with open(ARQUIVO_CONTATO, "w") as arquivo:
        json.dump(contatos, arquivo, indent=4)

def add_contato(nome, telefone, email):
    contatos = carregar_contatos()
    if nome in contatos:
        print(f"O contato '{nome}' já existe.")
    else: 
        contatos[nome] = {"telefone": telefone, "email": email}
        salvar_contato(contatos)
        print(f"Contato {nome} adicionado com sucesso!")

def buscar_contato(nome):
    contatos = carregar_contatos()
    if nome in contatos:
        print(f"Nome: {nome}")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print("Contato não encontrado.")

while True:
    print("\nMenu")
    print("1. Adicionar contato")
    print("2. Buscar Contato")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Número de telefone: ")
        email = input("Adicione o email: ")
        add_contato(nome, telefone, email)
    elif opcao == "2":
        nome = input("Nome: ")
        buscar_contato(nome)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente")
