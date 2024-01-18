def main():
    # Receber valores do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Selecionar a operação desejada
    print("Selecione o tipo de operação")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    # Realizar a operação matemática correspondente
    if escolha == '1':
        resultado = num1 + num2
    elif escolha == '2':
        resultado = num1 - num2
    elif escolha == '3':
        resultado = num1 * num2
    elif escolha == '4':
        resultado = num1 / num2
    else:
        print("Opção inválida")

    # Exibir o resultado ao usuário
    print("O resultado é:", resultado)

if __name__ == '__main__':
    main()
