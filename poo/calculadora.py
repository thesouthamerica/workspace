
while True:
    print("\nEscolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    
    opcao = int(input("Digite o número da operação desejada: "))

    if opcao in [1, 2, 3, 4]:
        break  
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def formatar_resultado(resultado):
    if resultado.is_integer():
        return f"{int(resultado)}"  
    else:
        return f"{resultado:.2f}"  

if opcao == 1:
    # Adição
    resultado = num1 + num2
    print(f"O resultado da adição é: {formatar_resultado(resultado)}")

elif opcao == 2:
    # Subtração
    resultado = num1 - num2
    print(f"O resultado da subtração é: {formatar_resultado(resultado)}")

elif opcao == 3:
    # Multiplicação
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {formatar_resultado(resultado)}")

elif opcao == 4:
    # Divisão
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {formatar_resultado(resultado)}")
    else:
        print("Erro: Divisão por zero não é permitida.")
