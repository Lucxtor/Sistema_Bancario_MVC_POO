def valida_opcao(opcoesValidas):
    while True:
        try:
            opcao = int(input("\nEscolha a opção: "))
        except:
            print("A opção digitada é invalida, por favor, tente novamente!")
        else:
            while opcao not in opcoesValidas:
                print("A opção escolhida é invalida, por favor, tente novamente!")
                opcao = int(input("\nEscolha uma nova opção: "))
            return opcao