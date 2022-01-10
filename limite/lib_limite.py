def valida_opcao(opcoesValidas):
    opcao = int(input("\nEscolha a opção: "))
    while opcao not in opcoesValidas:
        print("A opção escolhida é invalida, por favor, tente novamente!")
        opcao = int(input("\nEscolha uma nova opção: "))
    return opcao