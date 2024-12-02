def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Listar todas as tarefas")
    print("5. Pesquisar tarefa pelo nome")
    print("6. Sair")

tarefas = []
estados = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite o nome da tarefa: ")
        tarefas.append(tarefa)
        estados.append("Pendente")
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif opcao == "2":
        tarefa = input("Digite o nome da tarefa a marcar como concluída: ")
        if tarefa in tarefas:
            indice = tarefas.index(tarefa)
            estados[indice] = "Concluída"
            print(f"Tarefa '{tarefa}' marcada como concluída.")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    elif opcao == "3":
        tarefa = input("Digite o nome da tarefa a remover: ")
        if tarefa in tarefas:
            indice = tarefas.index(tarefa)
            tarefas.pop(indice)
            estados.pop(indice)
            print(f"Tarefa '{tarefa}' removida com sucesso!")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa encontrada.")
        else:
            print("\nTarefas:")
            for i in range(len(tarefas)):
                print(f"- {tarefas[i]} ({estados[i]})")

    elif opcao == "5":
        tarefa = input("Digite o nome da tarefa a pesquisar: ")
        if tarefa in tarefas:
            indice = tarefas.index(tarefa)
            print(f"Tarefa encontrada: {tarefas[indice]} ({estados[indice]})")
        else:
            print(f"Tarefa '{tarefa}' não encontrada.")

    elif opcao == "6":
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
