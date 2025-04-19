def criar_mapa(linhas, colunas):
    return[["Disponível" for _ in range(colunas)] for _ in range(linhas)]

def exibir_mapa(mapa):
    print("\nMapa de Assentos: ")
    for i, linha in enumerate(mapa):
        print(f"Linha {i+1}: ", end = "")
        for assento in linha:
            print(assento, end=" ")
        print()

def reservar(mapa, linha, coluna):
    if mapa[linha-1][coluna - 1] == "Disponível":
        mapa[linha - 1][coluna-1] = "Reservado"
        print(f"Assento na linha {linha}, coluna {coluna} reservado com sucesso.")
    else:
        print("O assento já esta reservado")

def cancelar(mapa, linha, coluna):
    if mapa[linha-1][coluna - 1] == "Reservado":
        mapa[linha - 1][coluna-1] = "Disponível"
        print(f"Reserva do assento na linha {linha}, coluna {coluna} foi cancelada.")
    else:
        print("O assento já esta disponível")

linhas, colunas = 5, 5
mapa = criar_mapa(linhas, colunas)

while True:
    print("\nMenu")
    print("1. Visualizar mapa de assentos")
    print("2. Reservar assento")
    print("3. Cancelar uma Reserva")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        exibir_mapa(mapa)
    elif opcao == "2":
        linha = int(input("Digite a linha do assento: "))
        coluna = int(input("Digite a coluna do assento: "))
        reservar(mapa, linha, coluna)
    elif opcao == "3":
        linha = int(input("Digite a linha do assento: "))
        coluna = int(input("Digite a coluna do assento: "))
        cancelar(mapa, linhas, colunas)
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente")
