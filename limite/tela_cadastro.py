class TelaCadastro:
    def tela_opcoes(self):
        self.exibe_menu()
        opcao = int(input("\nEscolha a opção: "))
        while opcao not in [0,1,2]:
            self.exibe_menu()
            opcao = int(input("\nEscolha a opção: "))
        return opcao

    def exibe_menu(self):
        print("\n-------- Área de Cadastros ---------\n")
        print("Escolha o cadastro que deseja gerenciar: ")
        print("1 - Gerenciar Pessoas")
        print("2 - Gerenciar Contas")
        print("0 - Retornar para o menu anterior")