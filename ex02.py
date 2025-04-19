import json

ARQUIVO_ESTOQUE = "estoque.json"

def carregar_estoque():
    try:
        with open(ARQUIVO_ESTOQUE, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return[]

def salvar(estoque):
    with open(ARQUIVO_ESTOQUE, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def add_produto(nome, quantidade, preco):
    estoque = carregar_estoque
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    salvar(estoque)
    print(f"Produto '{nome}' adicionado ao estoque.")

def mostrar_estoque():
    estoque = carregar_estoque()
    if not estoque:
        print("O estoque está vazio.")
        return
    valor_tot = 0
    print("Produdos cadastrados:")
    for produto in estoque:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")
        valor_tot += produto['quantidade'] * produto['preco']
    print(f"Valor total do estoque: R$ {valor_tot:.2f}")

while True:
    print("\nMenu")
    print("1. Adicionar Produto: ")
    print("2. Exibir estoque")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Qual o nome do produto?: ")
        quantidade = int(input("Quantidade do produto: " ))
        preco = float(input("Preço do produto: "))
        add_produto(nome, quantidade, preco)
    elif opcao == "2":
        mostrar_estoque()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
