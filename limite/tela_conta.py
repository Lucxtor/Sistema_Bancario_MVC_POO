class TelaConta:
    def tela_opcoes(self):
        self.exibe_menu()
        opcao = int(input("\nEscolha a opção: "))
        while opcao not in [0,1,2,3]:
            self.exibe_menu()
            opcao = int(input("\nEscolha a opção: "))
        return opcao

    def exibe_menu(self):
        print("\n-------- Gerenciamento de conta ---------\n")
        print("Escolha como deseja gerenciar a conta: ")
        print("1 - Cadastrar nova conta")
        print("2 - Excluir conta")
        print("3 - Listar informações")
        print("0 - Retornar para o menu anterior")