class TelaOperacao:
    def tela_opcoes(self):
        self.exibe_menu()
        opcao = int(input("\nEscolha a opção: "))
        while opcao not in [0,1,2,3,4,5,6]:
            self.exibe_menu()
            opcao = int(input("\nEscolha a opção: "))
        return opcao

    def exibe_menu(self):
        print("\n-------- Área de Operações ---------\n")
        print("Escolha a operação que deseja efetuar: ")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Transferência Bancaria")
        print("4 - Transferência PIX")
        print("5 - Consultar Extrato")
        print("6 - Consultar Saldo")
        print("0 - Retornar para o menu anterior")