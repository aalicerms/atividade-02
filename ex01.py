import json
from datetime import datetime

FILE_PATH = "tarefa.json"

def carregar_tarefas():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar(tarefas):
    with open(FILE_PATH, "w") as file:
        json.dump(tarefas, file, indent=4)

def add(descricao, prazo):
    tarefas = carregar_tarefas()
    tarefas.append({"descricao": descricao, "prazo": prazo, "concluida": False})
    salvar(tarefas)

def mostrar():
    tarefas = carregar_tarefas()
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i + 1}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - Status: {status}")

def concluidas(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar(tarefas)

while True:
    print("\nMenu")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da tarefa: ")
        prazo = input("Prazo (YYYY-MM-DD): ")
        try:
            datetime.strptime(prazo, "%Y-%m-%d") 
            add(descricao, prazo)
            print("Tarefa adicionada com sucesso!")
        except ValueError:
            print("Formato de data inválido. Use o formato YYYY-MM-DD.")
    elif opcao == "2":
        mostrar()
    elif opcao == "3":
        mostrar()
        try:
            indice = int(input("Informe o número da tarefa que deseja concluir: ")) - 1
            concluidas(indice)
        except ValueError:
            print("Por favor, insira um número válido.")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
